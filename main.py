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
  wb = openpyxl.load_workbook('server-player-list.xlsx')
  sheet = wb.active
  sheet["A1"] = "Player name"
  sheet["B1"] = "Leave/Join"
  sheet["C1"]="Time"

  for row in data:
    sheet.append(row)
    wb.save('server-player-list.xlsx')
    

def data_to_csv(data):
  filename = 'aternos-player-list.csv'
  header=['Player Name','Leave/Join','Time']
  csvwriter.writerow(header) 
  with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file) 
    csvwriter.writerows(data) 

def check_player():
  
  time = []
  leave_join = []
  playername = []

  #Update your aternos credentials in the .env file
  
  api = Client.from_credentials(os.getenv('ATERNOS_USERNAME'), os.getenv('ATERNOS_PASSWORD'))
  servers = api.list_servers()
  server = servers[2]
  orgi_player_list = set(server.players_list)
  while True:
    sleep(10)
    server.fetch()
    current_player_list = set(server.players_list)
    new_players = list(current_player_list - orgi_player_list)
    left_players = list(orgi_player_list - current_player_list)
    if new_players:
      print(f'New player joined {new_players} at {currentTime()}')
      time.append(currentTime())
      playername.append(''.join(new_players))
      leave_join.append('Joined')
      orgi_player_list = current_player_list
      data = list(zip(playername, leave_join, time))  
      data_to_sheet(data)
      data_to_csv(data)
    elif left_players:
      print(f'Player left: {left_players} at {currentTime()}')
      time.append(currentTime())
      playername.append(''.join(left_players))
      leave_join.append('Left')
      orgi_player_list = current_player_list
      data = list(zip(playername, leave_join, time))
      data_to_sheet(data)
      data_to_csv(data)

check_player()