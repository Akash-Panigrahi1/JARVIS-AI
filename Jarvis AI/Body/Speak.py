import pyttsx3
from time import sleep
def Speak(Text):
    engine=pyttsx3.init("sapi5")
    voice=engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    engine.setProperty('rate',130)
    lengthoftext =len(str(Text))
    if lengthoftext==0:
        pass
    else:
        print("")
        print(f"you : {Text}.")
        print("")
        engine.say(Text)
        engine.runAndWait()
        if lengthoftext>=30:
            sleep(4)
        elif lengthoftext>=40:
            sleep(6)
        elif lengthoftext>=55:
            sleep(8)
        elif lengthoftext>=70:
            sleep(10)
        elif lengthoftext>=100:
            sleep(13)
        elif lengthoftext>=120:
            sleep(14)
        else:
            sleep
Speak("Gourav Magia")