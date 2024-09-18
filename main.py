import weather as w
import sys
import tkinter as tk
from tkinter import *
import customtkinter as ctk
from datetime import datetime
import time
import timePy
import asyncio
import imagetk
from PIL import Image, ImageTk

#REMEMBER TO UPDATE PIP IF NOT ALREADY DONE

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def show_frame(frame_to_show):
    for frame in frames:
        frame.pack_forget()
    frame_to_show.pack(fill="both", expand=True)


def update_time():
    # Get only the hours and minutes (HH:MM) and strip any unwanted characters
    current_time = time.strftime("%H:%M", time.localtime())
    current_seconds = time.strftime("%S", time.localtime())

    # Update the label
    timeLabel.configure(text=current_time)
    timeLabelCtrl.configure(text=current_time)
    timeLabelWthr.configure(text=current_time)
    timeLabelClk.configure(text=current_time)

     #Call this function again after 1000 ms (1 second)
    root.after(1000, update_time)






#def update_hours():
    #current_hours = time.strftime("%H", time.localtime())
   #hourLabel.configure(text=current_hours)
    #root.after(1000, update_hours)

root = ctk.CTk()
root.geometry("800x480")



currentTemp = round(w.current_temperature_2m)
currentAppTemp = round(w.current_apparent_temperature)

cloudyIconIm = Image.open("C:/Users/jskor/PycharmProjects/jarps/cloud.png")
cloudyIcon = ImageTk.PhotoImage(cloudyIconIm)
settingsIconIm = Image.open("C:/Users/jskor/PycharmProjects/jarps/settings.png")
settingsIcon = ImageTk.PhotoImage(settingsIconIm)
clockIconIm = Image.open("C:/Users/jskor/PycharmProjects/jarps/clock.png")
clockIcon = ImageTk.PhotoImage(clockIconIm)
musicIconIm = Image.open("C:/Users/jskor/PycharmProjects/jarps/music.png")
musicIcon = ImageTk.PhotoImage(musicIconIm)
controlIconIm = Image.open("C:/Users/jskor/PycharmProjects/jarps/sliders.png")
controlIcon = ImageTk.PhotoImage(controlIconIm)
gridIconIm = Image.open("C:/Users/jskor/PycharmProjects/jarps/grid.png")
gridIcon = ImageTk.PhotoImage(gridIconIm)
youtubeIconIm = Image.open("C:/Users/jskor/PycharmProjects/jarps/youtube.png")
youtubeIcon = ImageTk.PhotoImage(youtubeIconIm)
usersIconIm = Image.open("C:/Users/jskor/PycharmProjects/jarps/users.png")
usersIcon = ImageTk.PhotoImage(usersIconIm)
monitorIconIm = Image.open("C:/Users/jskor/PycharmProjects/jarps/monitor.png")
monitorIcon = ImageTk.PhotoImage(monitorIconIm)
homeIconIm = Image.open("C:/Users/jskor/PycharmProjects/jarps/smallHome.png")
homeIcon = ImageTk.PhotoImage(homeIconIm)

#home frame
homeFrame = ctk.CTkFrame(root)

controlButton = ctk.CTkButton(homeFrame, text="", image=controlIcon, height=150, width=170, font=("segoe ui light", 40), command=lambda:show_frame(controlFrame))
controlButton.place(relx = 0.275, rely = 0.38, anchor=CENTER)
weatherButton = ctk.CTkButton(homeFrame, image=cloudyIcon, text="", height=150, width=170,font=("segoe ui light", 40), command=lambda:show_frame(weatherFrame))
weatherButton.place(relx = 0.5, rely = 0.38, anchor=CENTER)
settingsButton = ctk.CTkButton(homeFrame, text="", image=settingsIcon, height=150,width=170, font=("segoe ui light", 40), command=lambda:show_frame(settingsFrame))
settingsButton.place(relx = 0.725, rely = 0.38, anchor=CENTER)
alarmButton = ctk.CTkButton(homeFrame, text="", image=clockIcon, height=150,width=170, font=("segoe ui light", 40), command=lambda:show_frame(clockFrame))
alarmButton.place(relx = 0.725, rely = 0.72, anchor=CENTER)
musicButton = ctk.CTkButton(homeFrame, text="", image=musicIcon, height=150,width=170, font=("segoe ui light", 40))
musicButton.place(relx = 0.5, rely = 0.72, anchor=CENTER)
appsButton = ctk.CTkButton(homeFrame, text="", image=gridIcon, height=150,width=170, font=("segoe ui light", 40), command=lambda:show_frame(appsFrame))
appsButton.place(relx = 0.275, rely = 0.72, anchor=CENTER)
weatherLabel = ctk.CTkLabel(homeFrame, text=str(currentTemp) + "°", font=("segoe ui light", 60))
weatherLabel.place(relx = 0.085, rely = 0.1, anchor="c")
timeLabel = ctk.CTkLabel(homeFrame, text="", font=("segoe ui light", 30))
timeLabel.place(relx=0.9, rely=0.1, anchor="c")

#controlFrame
controlFrame = ctk.CTkFrame(root)
timeLabelCtrl = ctk.CTkLabel(controlFrame, text="", font=("segoe ui light", 30))
timeLabelCtrl.place(relx=0.9, rely=0.1, anchor="c")
homeButtonCtrl = ctk.CTkButton(controlFrame, image=homeIcon, text="", height=52,width=52, command=lambda:show_frame(homeFrame))
homeButtonCtrl.place(relx=0.06, rely=0.1)

weatherFrame = ctk.CTkFrame(root)
timeLabelWthr = ctk.CTkLabel(weatherFrame, text="", font=("segoe ui light", 30))
timeLabelWthr.place(relx=0.9, rely=0.1, anchor="c")
tempLabelWthr= ctk.CTkLabel(weatherFrame, text=str(currentTemp) + "°", font=("segoe ui light", 100))
tempLabelWthr.place(relx = 0.06, rely = 0.425, anchor="w")
appTempLabel = ctk.CTkLabel(weatherFrame, text=f"Feels like {currentAppTemp}°", font=("segoe ui light", 30), text_color="#e0e0e0")
appTempLabel.place(relx = 0.06, rely = 0.575, anchor="w")
homeButtonWthr= ctk.CTkButton(weatherFrame, text="", image=homeIcon, height=52, width=52, command=lambda:show_frame(homeFrame))
homeButtonWthr.place(relx = 0.06, rely = 0.1)


settingsFrame = ctk.CTkFrame(root)

homeButtonStgs = ctk.CTkButton(settingsFrame, text="", image=homeIcon, height=52, width=52, command=lambda:show_frame(homeFrame))
homeButtonStgs.place(relx = 0.06, rely = 0.1)

appsFrame = ctk.CTkFrame(root)
guestModeButton = ctk.CTkButton(appsFrame, text="", image=usersIcon, height=150, width=150)
guestModeButton.place(relx = 0.275, rely=0.3, anchor=CENTER)
desktopModeButton = ctk.CTkButton(appsFrame, text="", image=monitorIcon, height=150, width=150)
desktopModeButton.place(relx = 0.5, rely=0.3, anchor=CENTER)
youtubeButton = ctk.CTkButton(appsFrame, text="", image=youtubeIcon, height=150, width=150)
youtubeButton.place(relx = 0.725, rely=0.3, anchor=CENTER)
homeButtonApps = ctk.CTkButton(appsFrame, text="", image=homeIcon, height=52, width=52, command=lambda:show_frame(homeFrame))
homeButtonApps.place(relx = 0.06, rely = 0.1)


clockFrame = ctk.CTkFrame(root)
timeLabelClk = ctk.CTkLabel(clockFrame, text="", font=("segoe ui light",180))
timeLabelClk.place(relx = 0.5, rely = 0.3, anchor=CENTER)
homeButtonClk = ctk.CTkButton(clockFrame, text="", image=homeIcon, height=52, width=52, command=lambda:show_frame(homeFrame))
homeButtonClk.place(relx = 0.06, rely = 0.1)

update_time()

frames = [homeFrame, controlFrame, weatherFrame, settingsFrame, appsFrame, clockFrame]

# Initially show Frame 1
show_frame(homeFrame)

root.mainloop()

