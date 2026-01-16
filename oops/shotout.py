import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

speaker.speak("hello master")

print("shotout of my frnds:~")

l = [ "anjali" , "soni" , "keshvi" , "priya" , "riya",
       "neha" , "khusboo" , "prachi" , "khushi" , "sweety"]
speaker.speak(" shotout is start ")

for name in l :
    
    speaker.speak(f"well done {name}")

print("done shotout !")
speaker.speak(" every name had been called master !")
