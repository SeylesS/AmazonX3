#seyles
#import calendar
import csv
#import datetime
import pathlib
import shutil
import sys
import time
from datetime import datetime
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import system, name  # import only system from os
from os import path
from pathlib import Path
from smtplib import SMTP
from tempfile import NamedTemporaryFile
import base64
import smtplib



def clear():  # Clear the screen function
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

clear()  # now call function we defined above
#seyles

def menu():
        print("""         ****Amazon Reconcile Search Menu**** """)
        choice = input('''
        D: By Date        | C: By Item Total   |  I: By Order ID  | Q: Quit
                        Please make a selection
        ''')

        if choice.lower() == "d":
            clear()
            search_d()

        elif choice.lower() == "c":
            clear()
            search_c()

        elif choice.lower() == "i":
            clear()
            search_i()
            
        elif choice.lower() == "q":
            clear()
            sys.exit("Thanks for using Amazon Reconcile ")
              
        else:
            print("!!!!!!!!!!!!!* Please select a menu option. *!!!!!!!!!!!!!!!!!!!")
            time.sleep(2)
            clear()
        menu()  
            
  #seyles          
            
            
            

def search_d():
    search_for = input('Enter Order Date: ')

    with open('amazon.csv' , encoding='utf8', errors='ignore') as file:
        reader = csv.DictReader(file)
        print('\n *****'"****** Amazon Order Date Search Results ******", end='\n *****\n *')
        writer = csv.DictWriter(file, "Order Date")
        counting = 0
        for row in reader:
            if row["Order Date"] in search_for:
                print(row["Order Date"],row["Order ID"], row["Item Total"], row["Title"], end='\n\n ')
                counting+=1
        print ("The number of results:", counting, end='\n\n *')
                
#seyles
clear()

def search_i():
    search_for = input('Enter Order ID#: ')

    with open('amazon.csv' , encoding='utf8', errors='ignore') as file:
        reader = csv.DictReader(file)
        print('\n *****'"****** Amazon Order ID Search Results ******", end='\n *****\n *')
        writer = csv.DictWriter(file, "Order ID")
        counting = 0        
        for row in reader:
            if row['Order ID'] in search_for:
                print(row["Order ID"],row["Order Date"], row["Item Total"], row["Title"], end='\n\n ')
                #print(sorted(row, key=lambda i: i[0], reverse=True))
                counting+=1                
        print ("The number of results:", counting, end='\n\n *') 
#seyles
clear()

def search_c():
    search_for = input('Enter Item Total: ')

    with open('amazon.csv' , encoding='utf8', errors='ignore') as file:
        reader = csv.DictReader(file)
        print('\n *****'"****** Amazon Order Item Total Search ******", end='\n *****\n *')
        writer = csv.DictWriter(file, "Item Total")
        counting = 0
        for row in reader:
            if row['Item Total'] in search_for:
                print(row["Item Total"], row["Order Date"], row["Order ID"], row["Title"], end='\n\n ')
                counting+=1
        print ("The number of results:", counting, end='\n\n *')                
menu()
clear()

#seyles
