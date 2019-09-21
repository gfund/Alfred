# by Gunnar Funderburk 2019
import math
#import speech_recognition as sr     # import the library
import keyboard
import win32
import os
import re
import turtle
import urllib
import time
import datetime
import webbrowser
import random
import pyttsx3
import pyfiglet
import pygame
import turtle
import smtpd
import smtplib
#import speech_recognition
import sounddevice
from pygame import mixer
import urllib
import string
from time import sleep
from winsound import Beep
from msvcrt import getch


run="Yes"
while run=="Yes":
 try:
 
     
    def speak(text:str):
     alfred=pyttsx3.init()
     alfred.say(text)
     alfred.setProperty('rate',200)
     alfred.setProperty('volume', 1.0)
     alfred.runAndWait()
    def display(darg):
         
        screen = turtle.Screen()
        image = "C:/Users/gfund/Documents/MyPythonFiles/newalf.gif"
        screen.addshape(image)
        turtle.shape(image)
       
        turtle.write(darg, move=False,align="center",font=("Arial", 20, "normal"))
        
        pass

    #display(" ")
    mathr="The result is:"
    timer="The time is:"
    timesett="v" #Set to "mil" if you want military time
    a=0
    b=0
    handled=0
    
    checkuser=[]
    checksys=[]
    
    name="Gunnar" #Write what you want to be called here'
    speak("Hello Gunner, what do you want me to do for you?")
    #display("Hello Gunnar, what do you want me to do for you?")
    request=input(("Hello {0}, what do you want me to do for you?").format(name))
    speak(request)
    cmds=["add","subtract","multiply","divide","time","name","web","stop","find","code","tea","capabilites"]
    usercmds=["add","subtract","multiply","divide","my name","open","actions","stop","tea"]
    cmdsds=["","","", "", "tell you the","tell you your","open the",""]

    for i in cmds:
     if i in request:
        arg=request.split(i)
        argg=arg[1]
        if ("and" in argg) or ("by" in argg):
            argg=argg.replace("and","")
            argg=argg.replace("by","")
            argg=argg.replace(" ","",2)
            argg=argg.split(" ")
            
    #speak("ARGG",argg)            
    def add(nums:list):
     return (mathr+" "+str(int(nums[0])+int(nums[1])))

    def sub(nums:list):
     return (mathr+" "+str(int(nums[0])-int(nums[1])))
    def mul(nums:list):
     return (mathr+" "+str(int(nums[0])*int(nums[1])))
    def div(nums:list):

     return (mathr+" "+str(int(nums[0])/int(nums[1])))
    def tim():
     currentDT=datetime.datetime.now()
     strcurrentDT=str(currentDT)
     strcurrentDT=strcurrentDT.split(" ")
     military=strcurrentDT[1]
     normaltimesplit=military.split(":")
     hour=normaltimesplit[0]
     if int(hour)>12:
        timesuffx="pm" 
        hour=str(int(hour)-12)

     else:
        timesuffx="am"
     minute=normaltimesplit[1]
     seconds=normaltimesplit[2]
     secondl=seconds.split(".")
     seconds=secondl[0]
     normaltime=hour+":"+minute+":"+seconds
     if timesett=="mil":
      return(timer+" " +military)
     else:
        return (timer+" " +normaltime+" "+timesuffx)
    def email(recipient,msg):
        
        fromaddr="alfred.pysemail@gmail.com"
        toadrr=recipient
        username="alfred.pysemail@gmail.com"
        password="GF12Alfred!"
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr,toadrr,msg)
        server.quit()
    def names():
         return("You are "+name)
    def web():

        webbrowser.open_new_tab('http://www.google.com/search')
    def cap():
     
        c=0
        for z in cmds:
         
          if z !="capabilites":
    
            speak("I can "+cmdsds[c]+" "+z)
            print("I can "+cmdsds[c]+" "+z)
          c=c+1
    def find(name,path):
 
     """
     for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name) 
     """  
    def joke():
        jokes=(   "Q: What did the duck say when he bought lipstick? A: Put it on my bill.","My friend thinks he is smart. He told me an onion is the only food that makes you cry, so I threw a coconut at his face.","Q: Why did the banana go to the Doctor? A: Because it was not peeling well","Teacher: Which book has helped you the most in your life? Student: My father’s check book!","Q: What happens to a frog’s car when it breaks down?  A: It gets toad away.","Q: What never asks questions but receives a lot of answers? A: The Telephone","Q: What do you call sad coffee? A: Despresso." )
        jokepick=random.choice(jokes)
        return(jokepick)
    def playmusic():
        
      pygame.init()
      song = pygame.mixer.Sound("sitar.ogg")
      clock = pygame.time.Clock()
      song.play()
      while True:
       clock.tick(60)
      pygame.quit()
    def banner(text):
        
        ascii_banner = pyfiglet.figlet_format(text)
        print(ascii_banner)
    def aboutcmptr():
        string = os.getenv('COMPUTERNAME') 
        user=os.getlogin()
        #handled=1
        return("Computer Name:"+string+" "+"User:"+user)
     
    def globe():
      
       webbrowser.open("C:/Users/gfund/Documents/MyPythonFiles/alfMap.html")
    def music():
        songlist=("Meet the Flinstones","Despacito","Never Going to Give You Up","Rasputin","I Want to Break Free","Iron Man")
        # songlist={"Meet the Flinstones":"b.mp3","Despacito":"d.mp3","Never Going to Give You Up":"e.mp3","Rasputin":"c.mp3"}
        print(songlist)
        track=input("What song?")
      
       
        if track=="Meet the Flinstones":
            songn="b"
        if track=="Despacito":
            songn="d"
        if track=="Never Going to Give You Up":
            songn="e"
        if track=="Rasputin":
            songn="c"
        if track=="I Want to Break Free":
            songn="a"
        if track =="Iron Man":
            songn="g"
        mixer.init()

        pygame.mixer

        pygame.mixer.music.load(songn+".mp3")

        pygame.mixer.music.play()

        time.sleep(10)
  
    def speechin():
         
       r = sr.Recognizer()                 # initialize recognizer
       with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)        # listen to the source
       try:
        text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
        print("You said : {}".format(text))
       except:
        print("Sorry could not recognize your voice")    # In case of voice not recognized 
       keyboard.write(text)
       keyboard.press_and_release("enter")
  

    if "add" in request.lower():
     speak(add(argg))
     print(add(argg))
     handled=1
     

    if "subtract" in request.lower() :
     speak(sub(argg))
     print(sub(argg))
     handled=1
    if "multiply" in request.lower():
     speak(mul(argg))
     print(mul(argg))
     handled=1
    if "divide" in request.lower():
     speak(div(argg))
     print(div(argg))
     handled=1
    if "time" in request.lower():
     speak(tim())
     print(tim())
     handled=1
    if "my name" in request.lower():
     speak(names())
     print(names())
     handled=1
    if "open" in request.lower():
        #Defaultly google
       webbrowser.open_new_tab('http://www.google.com/search')
       handled=1
    if "actions" in request.lower():
        cap()
        handled=1
    if "help" in request.lower():
        speak("You can use these commands to control me:")
        print("You can use these commands to control me:")
        speak(usercmds)
        print(usercmds)
        handled=1
    if "stop" in request.lower():
        run="no"
        handled=1
    if "find"in request.lower():
       speak("This function does not work yet!")
       print("This function does not work yet!")
        #nam=input("Name of File:")
        #pat=input("Path")
        #find(nam,pat)
       handled=1
    if "mimosa" in request.lower():
        speak("Right away," + " "+"Gunner") #name hard coded here because of pronounciation
        print("Right away," + " "+ name)
        handled=1
    if "tell me a joke" in request.lower():
        speak(joke())
        
        handled=1
    if "play music" in request.lower():
       music()
       handled=1
       keyboard.wait('esc')
    if "banner" in request.lower():
         btext=input("Text:")
         banner(btext)
         handled=1
    if "about computer" in request.lower():
       speak(aboutcmptr())
       print(aboutcmptr())
       handled=1
    if "map" in request.lower():
        globe()
        handled=1
    if "say" in request.lower():
       word=request.split(" ") 
       wordsspeak=word[1:]
       for f in wordsspeak:
         speak(f)
       handled=1
    if "random color" in request.lower():
       lst=["red","blue","yellow","green"]
       speak(random.choice(lst))
       handled=1
    if "email" in request.lower():
        towhom=input("Who do you want to send the message to?")
        message=input("What's the message?")
        email(towhom,message)
        handled=1
    if "voicein" in request.lower():
        speechin()
    
    elif handled==0:
        speak("I can not do that sir")
        print("I can not do that sir") 
        print("My commands are")
       
        speak(usercmds)
        print(usercmds)
        """
        speak("Please contact gfunderburk@protonmail.com for additional functions")
        print("Please contact gfunderburk@protonmail.com for additional functions")
        """

 except :
     speak("You tryed to do something invalid.")
     print("You tryed to do something invalid.")
     #Section for code that is not working yet
     #Bible Functionality(Under work)

"""   
    if "bible" in request.lower():
        verse=input("What Verse do you want to go to")
        for line in Bible.txt:
            if verse in line:
                print(line)
"""


"""        
    def maze():
        

 

      def draw():
     "Draw maze."
      color('black')
    width(5)

    for x in range(-200, 200, 40):
        for y in range(-200, 200, 40):
            if random() > 0.5:
                line(x, y, x + 40, y + 40)
            else:
                line(x, y + 40, x + 40, y)

    update()

def tap(x, y):
    "Draw line and dot for screen tap."
    if abs(x) > 198 or abs(y) > 198:
        up()
    else:
        down()

    width(2)
    color('red')
    goto(x, y)
    dot(4)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
draw()
onscreenclick(tap)
done()
"""


