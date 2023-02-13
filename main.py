import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
 engine.say(audio)
 engine.runAndWait()

#user code
#user name
user_name = ['John','Tim','Paul']
print(user_name)
#def code
#you can change code as per your wish
scrcode=630243
#PRogram
greet = "Welcome Sir, How may I assist you ?"
stmt1 = "Enter Your Access Code"
stmt2 = "Get ready for your next task"
speak(stmt1)
code = input(stmt1)
print("Analyzing.....")
speak("Analyzing")
if code==scrcode:
    print(stmt2)
    speak(stmt2)
    print("if next task is set of characters, ensure that every character is small letter")
    speak("if next task is set of characters, ensure that every character is small letter")
else:
    speak("Security Breach")
    print("Get lost")
    exit(code)
code2 = input("Who is Founder of Google,Inc")
second_task = input(code2)
print(second_taskecond_task)
speak(second_task)
if second_task=="sundar pichai" :
    speak(greet)
    print(greet)
else:
   print("Security Breach")
   speak("Security Breach")
