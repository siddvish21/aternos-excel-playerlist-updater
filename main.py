import asyncio
import logging
import os
from dotenv import load_dotenv
from typing import Tuple, Dict, Any
load_dotenv()
from python_aternos import Client, Streams ,Status
from pytz import timezone
import datetime
import openpyxl
import csv
from daily_report import alert_check_time


user = os.getenv('ATERNOS_USERNAME')
pswd = os.getenv('ATERNOS_PASSWORD')

def data_to_sheet(data):
  excel_filename = 'resources/server-player-list.xlsx'
  wb = openpyxl.load_workbook(excel_filename)
  sheet = wb.active
  sheet["A1"] = "Player name"
  sheet["B1"] = "Leave/Join"
  sheet["C1"] = "Time"

  for row in data:
    sheet.append(row)
    wb.save(excel_filename)



def append_data(new_player, status):
  time = []
  leave_join = []
  playername = []
  time.append(currentTime())
  playername.append(''.join(new_player))
  leave_join.append(status)
  data = list(zip(playername, leave_join, time))
  data_to_sheet(data)
  data_to_csv(data)
  

def data_to_csv(data):
  csv_filename = 'resources/aternos-player-list.csv'
  header = ['Player Name', 'Leave/Join', 'Time']

  file_exists = os.path.isfile(csv_filename)

  with open(csv_filename, 'a', newline='') as file:
    csvwriter = csv.writer(file)

    if not file_exists:
      csvwriter.writerow(header)

    csvwriter.writerows(data)




def currentTime():
    tz = timezone("Asia/Kolkata")
    date = datetime.datetime.now(tz)
    return date.strftime("%d-%m-%Y %H:%M:%S")



logs = input('Show detailed logs? (y/n) ').strip().lower() == 'y'
if logs:
    logging.basicConfig(level=logging.DEBUG)

aternos = Client.from_credentials(user, pswd)

server = aternos.list_servers()[2]
socket = server.wss()

orgi_player_list = set(server.players_list)

@socket.wssreceiver(Streams.status, ('Server 1',))
async def state(msg: Dict[Any, Any], args: Tuple[str]) -> None:
    server._info = msg
    print(args[0], server.subdomain, 'is', server.status)
    print(args[0], 'players:', server.players_list)
    current_player_list = set(server.players_list)
    new_player = list(current_player_list - orgi_player_list)
    left_player = list(orgi_player_list - current_player_list)
    if new_player:
        print(f'New player joined {new_player} at {currentTime()}')
        append_data(new_player, 'Joined')
        orgi_player_list = current_player_list
    elif left_player:
        print(f'Player left: {left_player} at {currentTime()}')
        append_data(left_player, 'Left')
        orgi_player_list = current_player_list

async def main() -> None:
    if server.status_num != Status.on:
        server.start()
    await socket.connect()
    await asyncio.create_task(loop())

async def loop() -> None:
    while True:
        await asyncio.Future()


alert_check_time()
asyncio.run(main())
