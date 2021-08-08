import pyttsx3                      #text to speech conversion
import speech_recognition as sr     #speech to text conversion
import datetime                     #date time data
import wikipedia                    #wikipedia searches
import webbrowser                   #opening web pages
import os                           #opening apps and files
import requests                     #for web searches
from googlesearch import search     #for google searches
from textblob import TextBlob       #for language translation 



def speak(audio) :
     engine.say(audio)
     engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)   
    if hour>=0 and hour<12 :
        speak("Good Morning !")
    elif hour>=12 and hour<18 :
        speak("Good Afternoon!")
    else :
        speak("Good Evening")    

def introduction():
    speak("Hello sir!. I am Nattasha . How can i help you? ")      

def takecommand() :
    r=sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold=4000
        audio = r.listen(source) 


    try :
        print("Recognizing....")
        query=r.recognize_google(audio,language= "en-in")
        print("User said : ",query)

    except Exception :
          
        print("Can you please repeat that?")
        speak("Can you please repeat that ?")
        return "None"
    return query    


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices') 
engine.setProperty('voice',voices[1].id)   


if ""="":
    wishme()
    introduction()
    while True : 
        query=takecommand().lower()  
        if "wikipedia" in query :
            speak("Searching in Wikipedia...")
            query=query.replace("wikipedia","")
            print(query)
            results=wikipedia.summary(query, sentences=2,auto_suggest=False)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif "search google" in query or "google search" in query :
             query=query.replace ("search google ","")
             speak("Surchng Google...")
            
             for j in  search(query, tld='com', lang='en-in', num=10, start=0, stop=2, pause=2.0):
                print(j)
             speak("These are the links that I found")

        elif query=="translate to chinese" :
             speak("What do you want to translate ?")
             
             sentence=takecommand()
             blob = TextBlob(sentence)
             ans=(blob.translate(to='zh-Hans'))
             print(ans)
             speak(ans)

    
        elif query=="translate to german" :
             speak("What do you want to translate ?")
             
             sentence=takecommand()
             blob = TextBlob(sentence)
             ans=(blob.translate(to='de'))
             print(ans)
             speak(ans)         

             
        elif query=="translate to spanish" :
             speak("What do you want to translate ?")
             
             sentence=takecommand()
             blob = TextBlob(sentence)
             ans=(blob.translate(to='es'))
             print(ans)
             speak(ans)

        elif query=="translate to hindi" :
             speak("What do you want to translate ?")
             
             sentence=takecommand()
             blob = TextBlob(sentence)
             ans=(blob.translate(to='hi'))
             print(ans)
             speak(ans)    

        elif query=="translate to arabic" :
             speak("What do you want to translate ?")
             
             sentence=takecommand()
             blob = TextBlob(sentence)
             ans=(blob.translate(to='ar'))
             print(ans)
             speak(ans)    


       
                 

        elif query=="open youtube"  :
            webbrowser.open("youtube.com")

        elif query=="open bling" :
            webbrowser.open("bling.com")

        elif query=="open google"  :
            webbrowser.open("google.com")

        elif query=="open yahoo"  :
            webbrowser.open("yahoo.com")

        elif query=="open gmail" :
            webbrowser.open("gmail.com")

        elif query=="are you there"  :
            speak("Always for you , sir!")

        elif query=="open facebook"  :
            webbrowser.open("facebook.com")

        elif query=="open amazon"  :
            webbrowser.open("amazon.in")

        elif query=="open twitter"  :
            webbrowser.open("twitter.com")

        elif query=="open reddit"  :
            webbrowser.open("reddit.com")

        elif query=="open instagram"  :
            webbrowser.open("instagram.com")

        elif query=="open microsoft"  :
            webbrowser.open("microsoft.com")
            
        elif query=="news" or query=="current news" :
             webbrowser.open("indiatimes.com")

        elif query=="open stackoverflow"  :
            webbrowser.open("stackflow.com")    

        

        elif query=='tell me the time' or query=="what is the time" or query=="the time" or query=="time" or query=="what's the time":
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
             
             
        elif query=="open chrome" or query=="open google chrome"  :                              
              path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"     
              os.startfile(path)
             
        
        


        elif query=="tell me about yourself" or query=="introduce yourself" :
             speak("Hello sir. I am Nattasha , your voice assistant . You can ask me your queries and I will search them on web . Also , I am capable of opening files , apps , and websites for you . I was created by my develepor Arjun and I was born on the thirty first of May two thousand nineteen. I am still in a very early stage and i will only get better with time like wine")
             

        

        

        elif query=="hi" or query=="hello"  or query=="hey nattasha" or query=="hi natasha":
             speak("Hello sir! It is a great pleasure to meet you !")

        elif query=="what's the weather" or query=="what is the weather" or query=="the weather" or query=="weather" :
             speak("finding the current weather.." )
             for j in  search("current weather", tld='in', lang='en-in', num=10, start=0, stop=2, pause=2.0):
                print(j)
             speak("You can use these links")
             

        elif query=="" or query==None:
             pass

        

        elif query=="play game" or query=="play a game" or query=="game" :
             secret_number = random.randrange(1,129)
             speak("Welcome to the number guessing game.")
             speak("Let's start")

             guess = 0
             speak("Guess a number 1 to 128 " )
             while guess != secret_number:
                 guess = (int) (input("Guess a number 1 to 128: "))
                 
                 if guess < secret_number:
                    print( "Your guess is too low." )
                    speak("your guess is Too low" )
                 elif guess > secret_number:
                    print( "Your guess is too high." )
                    speak("your gess is Too high")
             else:
                 print( guess,"is the correct answer!")
                 speak(guess)
                 speak("is the correct answer!")
                 speak("Thank you for playing this game ")
                 



           



        elif query=="quit" :
             speak("OK")
             quit()
             

        
        else :
             try :
                searchgoogle=query
                results=wikipedia.summary(query, sentences=2,auto_suggest=False)
                speak("According to wikipedia")
                print(results)
                speak(results)
                for j in  search(searchgoogle, tld='com', lang='en-in', num=10, start=0, stop=2, pause=4.0):
                   print(j)
                speak("These are the links I found on Google")

             except  Exception :
                  speak("Sorry,I couldn't get that " )

        
             

