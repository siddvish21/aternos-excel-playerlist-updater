import csv
import os
import datetime
import schedule
from csv2pdf import convert
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
from time import sleep
from threading import Thread

load_dotenv()

today = datetime.date.today().strftime('%d-%m-%Y')


def convert_to_pdf(csv_file_all):
    pdf_file=f'daily_report_{today}.pdf'
    destiny_pdf_file=f'resources/daily_report_{today}.pdf'
    destiny_csv_file=f'resources/daily_report_{today}.csv'
    
    with open(csv_file_all, 'r') as input_file, open(destiny_csv_file, 'w', newline='') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        header_row = next(reader)
        writer.writerow(header_row)

        for row in reader:
            row_date = datetime.datetime.strptime(row[2], "%d-%m-%Y %H:%M:%S").date().strftime('%d-%m-%Y')
            if row_date == today:
                writer.writerow(row)

    convert(destiny_csv_file, destiny_pdf_file)
    print('Converted')
    send_email(pdf_file,destiny_pdf_file)
        

csv_file_main = 'resources/aternos-player-list.csv'


def send_email(pdf_file,pdf_path):
    fromaddr = os.getenv("FROMADDRESS") #Enter the email address here in which you are going to send the mail though
    toaddr = os.getenv("TOADDRESS") # Enter the email address here in which you want to recieve the mail

    msg = MIMEMultipart()
  
    msg['From'] = fromaddr
  
    msg['To'] = toaddr
  
    msg['Subject'] = f"Daily Minecraft Server Reports {today}"
  
    body = f"{today} Player join/leave data"
  
    msg.attach(MIMEText(body, 'plain'))
  
    filename = pdf_file
    attachment = open(pdf_path, "rb")
  
    p = MIMEBase('application', 'octet-stream')
  
    p.set_payload((attachment).read())
  
    encoders.encode_base64(p)
   
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  
    msg.attach(p)
  
    s = smtplib.SMTP('smtp.gmail.com', 587)
  
    s.starttls()
  
    s.login(fromaddr, os.getenv('APPPASSWORD'))
  
    text = msg.as_string()
  
    s.sendmail(fromaddr, toaddr, text)
  
    s.quit()



schedule.every().day.at("20:00").do(convert_to_pdf,csv_file_all=csv_file_main)

def check_time():
    while True:
        schedule.run_pending()
        sleep(1)


def alert_check_time():
    thread = Thread(target=check_time)
    thread.start()
