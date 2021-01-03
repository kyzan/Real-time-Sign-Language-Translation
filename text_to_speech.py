import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 81)
engine.say("I will speak this text")
engine.runAndWait()



