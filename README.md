# Minecraft Player List Tracker

This script is designed to monitor changes to the player list on an Aternos Minecraft server, and record them in an Excel sheet and a CSV file. The script checks the player list every 10 seconds, and if a new player has joined or left the server, it updates the data in both the Excel sheet and the CSV file. Additionally, the script will send a PDF file of the day's player list as an email attachment at 8:00 PM every day.

## Prerequisites

To use this script, you will need:

- Python 3 installed on your machine
- Aternos account credentials to access your server's player list
- A Gmail account with 2-Step Verification enabled and an app password set up
- and another gmail account to recieve the day's player list data

## Installation

1. Clone this repository using `git clone https://github.com/siddvish21/aternos-excel-playerlist-updater.git`
2. Navigate to the cloned repository using `cd aternos-excel-playerlist-updater`
3. Install virtualenv using `pip install virtualenv`
4. Create a new virtual environment by running `python3 -m venv <Your virtual environment name>`
5. Activate the virtual environment by running `<Your virtual environment name>\Scripts\activate` (Windows) or `source env/bin/activate` (macOS/Linux)
6. Install the dependencies by running `pip install -r requirements.txt`
7. Rename the `.env.sample` file to `.env`
8. Update the Aternos credentials and Gmail account information in the `.env` file
9. Run the script using `python main.py`

## Usage
### VERY IMPORTANT:

- Do not give your Gmail account password in the `env` file.
- You need to log in to your Gmail account and enable 2-Step Verification first.
- Then, go to https://myaccount.google.com/apppasswords and log in to your Gmail account.
- Create an app password with any name you want and click on generate.
- Give the generated app password in the `.env` file under APPPASSWORD.


The script will continuously monitor the player list on the Aternos Minecraft server and update the Excel sheet and CSV file whenever a new player joins or an existing player leaves the server. The Excel sheet and CSV file will be updated with the following columns:

- Player name
- Leave/Join
- Time

Additionally, the script will send a PDF file of the day's player list as an email attachment at 8:00 PM every day.

## Acknowledgements

- [python-atemos](https://github.com/aternosorg/python-atemos) - Python library for Aternos API.
- [openpyxl](https://openpyxl.readthedocs.io/) - Python library to work with Excel files.
- [python-dotenv](https://github.com/theskumar/python-dotenv) - Python library to read variables from `.env` file.
- [csv](https://docs.python.org/3/library/csv.html) - Python library to work with CSV files.
- [schedule](https://schedule.readthedocs.io/en/stable/) - Python library to schedule recurring tasks.
- [smtplib](https://docs.python.org/3/library/smtplib.html) - Python library to send emails.
