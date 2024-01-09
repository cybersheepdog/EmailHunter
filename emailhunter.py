# ______     __    __     ______     __     __            __  __     __  __     __   __     ______   ______     ______    
#/\  ___\   /\ "-./  \   /\  __ \   /\ \   /\ \          /\ \_\ \   /\ \/\ \   /\ "-.\ \   /\__  _\ /\  ___\   /\  == \   
#\ \  __\   \ \ \-./\ \  \ \  __ \  \ \ \  \ \ \____     \ \  __ \  \ \ \_\ \  \ \ \-.  \  \/_/\ \/ \ \  __\   \ \  __<   
# \ \_____\  \ \_\ \ \_\  \ \_\ \_\  \ \_\  \ \_____\     \ \_\ \_\  \ \_____\  \ \_\\"\_\    \ \_\  \ \_____\  \ \_\ \_\ 
#  \/_____/   \/_/  \/_/   \/_/\/_/   \/_/   \/_____/      \/_/\/_/   \/_____/   \/_/ \/_/     \/_/   \/_____/   \/_/ /_/ 

# Imports
from configparser import ConfigParser
import logging
import keyring
import getpass

# Declare a list of 1 or more emails to monitor from the config file
monitored_emails = ['HOTMAIL', 'GMAIL1', 'GMAIL2']

def check_first_run(monitored_email):
    """Checks to see if this is the first time the program has been run.  
    If it is then it asks you to set the username for the email you want to monitor."""
    config_object = ConfigParser()
    try:
        config_object.read("config.ini")
    except:
        print("Error with config.ini")
    else:
        first_run = config_object[monitored_email]
        if first_run['first_run'] == 'True':
            #print("Initializing email from config file for " + monitored_email)
            initial_email_configuration(monitored_email)
            first_run = False
        else:
            #print("Run before.")
            #first_run = False
            pass
    
    #return first_run
            
def initial_email_configuration(monitored_email):
    """Uses config.ini to set the system and username fields for keyring.set_password.
    It will use the first_run variable (True = not saved, False = saved) to check if 
    the email password has previously been saved in the keyring.  
    Then uses getpass to allow the user to securely type their password and then store it
    using keyring. """
    config_object = ConfigParser()
    try:
        config_object.read("config.ini")
    except:
        print("Error with config.ini")
    else:
        email = config_object[monitored_email]
        if email['user']:
            username = email['user']
            print("\nInitializing email from config file for " + monitored_email)
            password = getpass.getpass("Type your password for " + username + ": ")
            keyring.set_password(monitored_email, username, password)
            configured_email = {
                'email': monitored_email,
                'username': username
            }
            print("Email configured.")
            
            config_object.set(monitored_email, 'first_run', 'False')
            with open('config.ini', 'w') as configfile:
                config_object.write(configfile)
            
        else:
            print("No user configured for email")
            configured_email = "False"
            
    return configured_email           

def email_configuration(monitored_email):
    """Uses config.ini to set the system and username fields for keyring.set_password.  
    Then uses getpass to allow the user to securely type their password and then store it
    using keyring"""
    config_object = ConfigParser()
    try:
        config_object.read("config.ini")
    except:
        print("Error with config.ini")
    else:
        email = config_object[monitored_email]
        if email['user']:
            username = email['user']
            configured_email = {
                'email': monitored_email,
                'username': username
            }
            print("Email configured.\n")
            
        else:
            print("No user configured for email")
            configured_email = "False"
            
    return configured_email   

def get_email_password(configured_email):
    """Gets email credentials from the keyring.  Requires the the 'configured_email' variable
    which is a dictionary containing the keys 'email' and 'username' to be passed to it"""
    password = keyring.get_password(configured_email['email'], configured_email['username'])
    return password
