from python_aternos import Client
import os
import openpyxl
import csv
import datetime
from time import sleep
from pytz import timezone
from dotenv import load_dotenv

load_dotenv()

def currentTime():
    #Change the timezone according to yours
    tz = timezone("Asia/Kolkata")
    date = datetime.datetime.now(tz)
    return date.strftime("%d-%m-%Y %H:%M:%S")


def data_to_sheet(data):
  excel_filename='server-player-list.xlsx'
  wb = openpyxl.load_workbook(excel_filename)
  sheet = wb.active
  sheet["A1"] = "Player name"
  sheet["B1"] = "Leave/Join"
  sheet["C1"]="Time"

  for row in data:
    sheet.append(row)
    wb.save(excel_filename)
    
def append_data(new_player,status):
  time = []
  leave_join = []
  playername = []
  time.append(currentTime())
  playername.append(''.join(new_player))
  leave_join.append(status)
  data = list(zip(playername, leave_join, time))  
  print(data)
  data_to_sheet(data)
  data_to_csv(data)


def data_to_csv(data):
    csv_filename = 'aternos-player-list.csv'
    header = ['Player Name', 'Leave/Join', 'Time']

    file_exists = os.path.isfile(csv_filename)

    with open(csv_filename, 'a', newline='') as file:
        csvwriter = csv.writer(file)

        if not file_exists:
            csvwriter.writerow(header)

        csvwriter.writerows(data)
    

def check_player():
      
  #Update your aternos credentials in the .env file
  api = Client.from_credentials(os.getenv('ATERNOS_USERNAME'), os.getenv('ATERNOS_PASSWORD'))
  servers = api.list_servers()
  server = servers[2]

  orgi_player_list = set(server.players_list)

  while True:
    sleep(10)
    server.fetch()
    current_player_list = set(server.players_list)
    new_player = list(current_player_list - orgi_player_list)
    left_player = list(orgi_player_list - current_player_list)
    if new_player:
      print(f'New player joined {new_player} at {currentTime()}')
      append_data(new_player,'Joined')
      orgi_player_list = current_player_list

    elif left_player:
      print(f'Player left: {left_player} at {currentTime()}')
      append_data(left_player,'Left')
      orgi_player_list = current_player_list

check_player()