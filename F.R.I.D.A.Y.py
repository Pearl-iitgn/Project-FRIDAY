import pyttsx3		#pip install pyttsx3
import time 		#already available
import random
import webbrowser
import speech_recognition as sr
import wikipedia
import os
#for using the pyttsx3 we need to have the pyaudio module installed
#I had some issues with it, so I had referred the following video to get the pyaudio
# https://www.youtube.com/watch?v=-3am_5jMzJ4&t=185s

#=========================================================================================

#sapi5 is inbuil voice (microsoft)
#I am working on windows 7 due to which I had only one voice "MS Anna"
#If its windows 10, then two voices David and Zara are available
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
rate = engine.getProperty("rate")
engine.setProperty("rate", 150)
volume = engine.getProperty("volume")
engine.setProperty("volume", 2)
#you can toggle between David(male voice) and Zara(female voice) by changing 0,1 the index of voices[].id
engine.setProperty("voice", voices[0].id)


#=========================================================================================
def speak(audio) :
    engine.say(audio)
    engine.runAndWait()

#this is the greeting line from friday to me
#due to windows 7 this sound might sound a bit cracking, but I guess it will work fine with David/Zara
def intro_1() :
    speak("Welcome Back Boss")

#=========================================================================================

#at this point I am using the speech recognition module
def inptCommd() :
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Initializing......")
        #this helps to minimise the background noise if any
        r.energy_threshold = 600
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try :
        print("Recognizing......")
        request = r.recognize_google(audio, language="en-in")
        print(f"User said : {request}\n")
        return request

    except :
        print("Please repeat that.....")
        #I have used this so I wont get error if it is unable to catch my voice
        return "None"

#==========================================================================================

intro_1() 

n = 3

#I have allowed it to execute for 3 times this can be changed later on by changing the value of n

for o in range(n):
    
    #making the request in lower is quite important, otherwise I will not be able to identify
    
    # the command (there will be issues for eg: Open Google and open google are not the same)
    
    request = inptCommd().lower()

    #this shows the list of the commands available
    
    #good thing about this is that you can say "open google for me" will be read as "open google"
    
    #so there is no harm to use some extra words
        
    availablecommd = ["hello friday","open google","wikipedia","open youtube","show campus"]
    z = ["open gmail","thanks friday","play my music","play music","play online music","help"]
        
    #I had introduced z only because availablecommd was way too long and exceeding the width of the screen
        
    availablecommd.extend(z)

    if "hello friday" in request :
            
        #I have used the time library to get the current time
            
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        
        #for the text to speech to speak the time in a way understandable i had used
        # slicing of the time in order to obtain minutes and hours separately
            
        a = current_time.split(":")
        hour = int(a[0])
            
            #I have divided the hours so that it wishes me as per the time
            
        if hour >=0 and hour < 12 :
            speak("Good Morning Boss Its "+str(hour)+" "+str(a[1])+"AM")
            print("Good Morning Boss Its "+str(hour)+":"+str(a[1])+"AM")
        elif hour == 12 :
            speak("Good afternoon Boss Its "+str(hour)+" "+str(a[1])+"PM")
            print("Good afternoon Boss Its "+str(hour)+":"+str(a[1])+"PM")
        elif hour>12 and hour < 18 :
            speak("Good afternoon Boss Its "+str(hour - 12)+" "+str(a[1])+"PM")
            print("Good afternoon Boss Its "+str(hour - 12)+":"+str(a[1])+"PM")
        else :
            speak("Good Evening Boss Its"+str(hour-12)+" "+str(a[1])+"PM")
            print("Good Evening Boss Its"+str(hour-12)+":"+str(a[1])+"PM")


#==========================================================================================

    elif "help" in request :

        #this will help in using friday
            
        speak("Check the commands available")
        for i in range(len(availablecommd)) :
            print(availablecommd[i])
                
            #I have used the sleep function from the time library so that the user is able to
            #see all the available commands properly
            
            time.sleep(3)
            
#==========================================================================================

    elif "play music" in request :
            
        #this might have some error because this directory is on my laptop and not on the users end
        #you can use the shared folder and paste the given folder in the same directory
        #and remember to use the double slash
            
        location = "D:\\Songs_Pearl"
        realmusic = os.listdir(location)
            
        #Random module used over here to play random songs in the folder
            
        os.startfile(os.path.join(location, realmusic[random.choice([0,1,2])]))
        quit()
        
    elif "play my music" in request :
            
        #this will play a specific music and again this might not work if its not present in
        #the required directory with the specififed name "Songs_Pearl"
            
        location = "D:\\Songs_Pearl"
        realmusic_2 = os.listdir(location)
        os.startfile(os.path.join(location, realmusic_2[1]))
        quit()
        
    elif "play online music" in request :
            
        #this will simply search the given link in the webbrowser
            
        webbrowser.open("https://www.youtube.com/watch?v=fHI8X4OXluQ")

        #remember that you can also speak "india wikipedia" or "search india in wikipedia"
        #it is the same and would give the same results
        
#==========================================================================================

    elif "wikipedia" in request :
            
        #here I have imported the wikipedia module and using its 
            
        speak("Looking up in Wikipedia.....")
        request = request.replace("search", "")
        request = request.replace("in", "")
        request = request.replace("wikipedia", "")
        
        #after this it will search the given command except "search", "in", "wikipedia"
        #directly in wikipedia
        
        results = wikipedia.summary(request, sentences = 3)
        
        #I have used the sentence argument to manage the number of sentences it 
        #would read
        
        print(results)
        speak("Boss, wiki says that"+results)
        
#===========================================================================================

    elif "thanks friday" in request :
        speak("My pleasure sir")
        quit()

#============================================================================================

    elif "open youtube" in request :
        webbrowser.open("https://www.youtube.com/")

#===========================================================================================

    elif "show campus" in request :
        webbrowser.open("https://www.youtube.com/watch?v=pKehMbvu-zs")

#===========================================================================================
 
    elif "open gmail" in request:
        
        #this might not work in the users pc if the you have not already logged in the 
        #gmail

        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

#===========================================================================================