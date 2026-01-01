import pyttsx3
import random
import webbrowser
import speech_recognition as sr
import time 
import datetime as dt
import openai
import os
openai.api_key = os.getenv("YOU_API_HERE")

#Project Simple (13/06/2025)
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
# program agar speech to word dengan antisipasi noise
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        try:
            audio = r.listen(source)
            command = r.recognize_google(audio)
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None
     


def option_word(user):
     if "who are you" in user:
              speak("I'm Mayo AI")
              
     elif "time" in user:
         now = dt.datetime.now()
         hari_apa = f"Year:{now.year}|Month:{now.month}|Day:{now.day}"
         real_time= now.strftime("%H:%M:%S")
         print(f"⌚:{real_time}")
         print(f"📅:{hari_apa}")
         speak(hari_apa)
         speak(real_time)
         time.sleep(1)
              
     elif "joke" in user:
         joke=["Why you gettin bullied in school? Because You're Black",
               "Do You Know What Favorite Police Suspect? Black Man",
               "Do You Know What I Hate So Much? Wait,Black People?,Nah Gay People Its Correct"
               ]
         speak(random.choice(joke))
         
     elif "music" in user:
         speak("What Song Do You Want To Hear?")
         name_song= listen()
         if name_song:
             speak(f"Searching Name Song Of {name_song}")
             url_song= f"https://www.youtube.com/results?search_query={name_song}"
             webbrowser.open(url_song)
         else:
            speak("Sorry I Can't Find It")
            
     elif "open" in user:
         speak("What Do You Want To Open")
         name_browser= listen()
         if name_browser:
             speak(f"Okay I Will Open {name_browser} ")
             url_browser=f"https://www.google.com/search?q={name_browser}"
             print(f"Opening {name_browser}")
             speak(f"Opening a {name_browser}")
             webbrowser.open(url_browser) 
         else:
             speak("Sorry I Cant Find It")
             
     elif "create" in user:
         speak("I Was Created By Given Glorious,He Build This At 16 Years Old")
        
          
     elif "help" in user:
         speak("Just Say")
         
                
     elif "hello" in user:
              speak("Hello How Can I Help You Today?")
      
              
     #It's works a little i think (A Libary can't detect what i say,i think my pronounce is bad or its a lame libary)     
     if "game" in user: 
         speak("guess a number between 1-10")
         angka = random.randint(10,50)
         while True:
            speak ("Go Guess A Number")
        
            tebakan_str = listen()
            
            if tebakan_str < angka:
                    speak("Too Low")
            elif tebakan_str > angka:
                    speak("Too High")
            if tebakan_str == angka:
                    speak("Congrast You Winnn")
                    break
                
            if tebakan_str is None:
                speak("Sorry You Dont Speak Any Thing")
                continue
            if tebakan_str.lower() == 'stop':
                speak("Good Bye")
                break
         speak("Thank You For Playing")
         
     if "chat" in user:
        speak('What do you need,just say it')
        prompt = listen()
        if not prompt:
            return "Sorry, I can't catch it"
     
        response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

        return response.choices[0].message.content
            

        

        
if __name__ == "__main__":
    
    speak("Hello I Was A Voice Assistant,May I Help You today")
    
    while True:
        user = listen()
        print("Chatbot is thinking")
        
        if user:
             user = user.lower()
             if user == "stop":
                speak("Good Bye")
                break
             else:
                 speak("You said:" + user)
                 option_word(user)
            
            
                
              
        
