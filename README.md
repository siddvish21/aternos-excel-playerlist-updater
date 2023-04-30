# Minecraft Player List Tracker

This script is designed to monitor changes to the player list on an Aternos Minecraft server, and record them in an Excel sheet. The script checks the player list every 10 seconds, and if a new player has joined or left the server, it updates the data in the Excel sheet.

## Prerequisites

To use this script, you will need:

- Python 3 installed on your machine
- Aternos account credentials to access your server's player list
- An Excel sheet to record the player list data




## Installation

1. Clone this repository using `git clone https://github.com/siddvish21/minecraft-player-list-tracker.git`
2. Navigate to the cloned repository using `cd minecraft-player-list-tracker`
3. Install virtualenv using `pip install virtualenv`
4. Create a new virtual environment by running `python3 -m venv <Your virtual environment name>`
5. Activate the virtual environment by running `<Your virtual environment name>\Scripts\activate` (Windows) or `source env/bin/activate` (macOS/Linux)
6. Install the dependencies by running `pip install -r requirements.txt`
7. Rename the `.env.sample` file  to `.env`
8. Update the Aternos credentials in the `.env` file
8. Run the script using `python main.py`

## Usage

The script will continuously monitor the player list on the Aternos Minecraft server and update the Excel sheet whenever a new player joins or an existing player leaves the server. The Excel sheet will be updated with the following columns:

- Player name
- Leave/Join
- Time


## Acknowledgements

- [python-atemos](https://github.com/aternosorg/python-atemos) - Python library for Aternos API.
- [openpyxl](https://openpyxl.readthedocs.io/) - Python library to work with Excel files.
- [python-dotenv](https://github.com/theskumar/python-dotenv) - Python library to read variables from `.env` file.
