from win11toast import toast
import time
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")




# Display a simple notification
speaker.speak("you work hard . take some break")
toast('you work hard . take some break')
print("Notification displayed (done)")
time.sleep(2) #set slepp time a/c to you

