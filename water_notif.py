from tkinter import *
from playsound import playsound
import schedule
import time

def drink():
    playsound('cool.wav')
    window = Tk()
    button = Button(
        text="Take A Sip",
        width=25,
        height=5,
        bg="IndianRed",
        command=window.destroy)

    button.pack()

    window.title("Drink Water!!!")
    window.geometry('+1950+100')

    window.mainloop()

schedule.every(30).minutes.do(drink)

while True:
    schedule.run_pending()
    time.sleep(1)