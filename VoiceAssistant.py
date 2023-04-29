import pyttsx3
import datetime
import speech_recognition as sr  
import wikipedia
import webbrowser
import os
import pywhatkit  

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
       Hour=int(datetime.datetime.now().hour) 
       if Hour>=0 and Hour<12:
           speak("Good Morning") 
       elif Hour>=12 and Hour<18:
           speak("Good Afternoon")
       else:
           speak("Good Evening") 
       speak("Hi I am Rebecca Please tell me how may I help you")  
 
def takecommand():
    #take microphone as user input 
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=0.2)#listen for 5 seconds and create the ambient noise energy level   
        r.energy_threshold = 400 #It help to re-adjust noise in environment and  try to match environment based noise level at the same time 
        r.pause_threshold=1 #The number of sec system will take to recongize the voice after user has completed thier sentence.
        audio=r.listen(source) 
    try:
        print("Recognizing...") 
        query=r.recognize_google(audio,language='en-in')
        print("User said:",query) 
        speak(query)
    except Exception as e:
        print("Say that again plz...") 
        return"None"
    return query

#main function start  
if __name__=="__main__":
    wishMe()
    while True:
      query=takecommand().lower()
 
   #logic for executing task.
      if 'wikipedia' in query:
          speak('Searching wikipedia....') 
          query=query.replace("wikipedia search for","") 
          results=wikipedia.summary(query,sentences=2)
          speak("According to wikipidia..")
          print(results)
          speak(results) 
          
    #open yt       
      elif 'open youtube' in query:
          webbrowser.open("youtube.com")
          
    #search on yt for query
      elif 'search youtube' in query:
          results=query.replace("search  youtube for","")
          webbrowser.open("https://www.youtube.com//results?search_query="+results) 
          pywhatkit.playonyt(results)
          speak("This what I found for you")
          
    #open google
      elif 'open google' in query:
         webbrowser.open("google.com") 
    
    #search on google for query
      elif 'search google' in query:
          text=query.replace("search google for","") 
          webbrowser.open("https://www.google.com/search?q="+text)
          pywhatkit.search(text)
          speak("This what I found for you")
          
    #open onfosys springboard      
      elif 'open infosys springboard' in query:
          webbrowser.open("https://infyspringboard.onwingspan.com/web/en/login") 
          
    #play music
      elif 'play music' in query:
          music_dir='C:\\Users\\Renuka\\Music'
          songs=os.listdir(music_dir) 
          os.startfile(os.path.join(music_dir,songs[7]))
    
    #tells the current time 
      elif 'the time' in query:
          strTime=datetime.datetime.now().strftime("%H:%M:%S") 
          print(strTime)
          speak(f"The time is {strTime}") 
          
    #open vs code
      elif 'open vs code' in query:
          codePath="C:\\Users\\Renuka\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
          os.startfile(codePath)
      
          
    #exit the program 
      elif 'quit' in query or 'exit' in query or 'close' in query:
           speak("Hope I have helped you Thanks you for using me")
           exit() 
           