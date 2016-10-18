import imaplib
import email
import time
import pyvona
import atexit
import os
from blinkt import set_clear_on_exit, set_all, set_pixel,show,set_brightness
 
def redon():

    set_all(128,0,0)
    set_brightness(0.8)
    show()

def fbon():

    set_all(49,49,224)
    set_brightness(0.8)
    show()

def twon():

    set_all(74,169,232)
    set_brightness(0.8)
    show()

def gron():

    set_all(90,232,74)
    set_brightness(0.8)
    show()

def clon():

    set_all(192, 192, 192)
    set_brightness(0.8)
    show()       

def sson():

    set_all(204, 102, 0)
    set_brightness(0.8)
    show()

def shon():

    set_all(128,128,128)
    set_brightness(0.8)
    show()

def cmon():

    set_all(102, 0, 204)
    set_brightness(0.8)
    show()   

def snon():

    set_all(204, 102, 0)
    set_brightness(0.8)
    show()   
      
def alloff():

    set_all (0,0,0)
    show()

def checkEmail():
        
    mail = imaplib.IMAP4_SSL('imap.gmail.com');
    mail.login('yournotificationgmailaddress@gmail.com','yourgmailpassword');
    mail.list();  # Gives list of folders or labels in gmail.
    v = pyvona.create_voice('YourIvonaAccessKey', 'YourIvonaSecretKey')    
    count = 0
    
    while count < 600:
        try:
            # Connect to inbox
            mail.select("inbox"); 
    
            # Search for an unread email from user's email address
            result, data = mail.search(None,'(UNSEEN FROM "yourIFTTTsendingaddress@gmail.com")');
    
            ids = data[0]   # data is a list
            id_list = ids.split() # ids is a space separated string

            latest_email_id = id_list[-1] # get the latest
            result, data = mail.fetch(latest_email_id, "(RFC822)");

            raw_email = data[0][1];

            recv_msg = email.message_from_string(raw_email)

            cl ="Cloudy"
            ss ="Sunset"
            sh ="Showers"
            cm ="Claire"
            fb ="facebook"
            tw ="twitter"
            yt ="youtube"
            sn ="Sunny"

            if fb in recv_msg['Subject']:

                print("Facebook Message")     
                print(recv_msg['Subject'])
                fbon()
                time.sleep(1)
                v.voice_name = 'Amy'
                v.region = 'eu-west'
                v.speak(recv_msg['Subject'])
                print "Release"
                time.sleep(1)
                alloff()
                
            elif tw in recv_msg['Subject']:

                print("Twitter Message")     
                print(recv_msg['Subject'])
                twon()
                time.sleep(1)
                v.voice_name = 'Amy'
                v.region = 'eu-west'
                v.speak(recv_msg['Subject'])
                print "Release"
                time.sleep(1)
                alloff()
                

            elif yt in recv_msg['Subject']:

                print("YouTube Message")     
                print(recv_msg['Subject'])
                redon()
                time.sleep(1)
                v.voice_name = 'Amy'
                v.region = 'eu-west'
                v.speak(recv_msg['Subject'])
                print "Release"
                time.sleep(1)
                alloff()

            elif cl in recv_msg['Subject']:

                print("Cloudy Message")     
                print(recv_msg['Subject'])
                clon()
                time.sleep(1)
                v.voice_name = 'Amy'
                v.region = 'eu-west'
                v.speak(recv_msg['Subject'])
                print "Release"
                time.sleep(1)
                alloff()

            elif ss in recv_msg['Subject']:

                print("Sunset Message")     
                print(recv_msg['Subject'])
                sson()
                time.sleep(1)
                v.voice_name = 'Amy'
                v.region = 'eu-west'
                v.speak(recv_msg['Subject'])
                print "Release"
                time.sleep(1)
                alloff()

            elif sh in recv_msg['Subject']:

                print("Showery Message")     
                print(recv_msg['Subject'])
                shon()
                time.sleep(1)
                v.voice_name = 'Amy'
                v.region = 'eu-west'
                v.speak(recv_msg['Subject'])
                print "Release"
                time.sleep(1)
                alloff()
                
            elif cm in recv_msg['Subject']:

                print("Wifely Message")     
                print(recv_msg['Subject'])
                cmon()
                time.sleep(1)
                v.voice_name = 'Amy'
                v.region = 'eu-west'
                v.speak(recv_msg['Subject'])
                print "Release"
                time.sleep(1)
                alloff()

                
            elif sn in recv_msg['Subject']:

                print("Sunny Message")     
                print(recv_msg['Subject'])
                snon()
                time.sleep(1)
                v.voice_name = 'Amy'
                v.region = 'eu-west'
                v.speak(recv_msg['Subject'])
                print "Release"
                time.sleep(1)
                alloff()
                
            else:

                print("Generic Message")     
                print(recv_msg['Subject'])
                gron()
                time.sleep(1)
                v.voice_name = 'Amy'
                v.region = 'eu-west'
                v.speak(recv_msg['Subject'])
                print "Release"
                time.sleep(1)
                alloff()
                
                count = 6

        except IndexError:
            time.sleep(30*1)
            if count < 5:
                count = count + 1
                continue
            else:
                print("Nothing to read here")
                count = 6             
checkEmail()
