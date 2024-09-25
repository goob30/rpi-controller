import weather as w
from tkinter import *
import customtkinter as ctk
import time
from PIL import Image, ImageTk
#REMEMBER TO UPDATE PIP IF NOT ALREADY DONE

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def update_time():
    # Get only the hours and minutes (HH:MM) and strip any unwanted characters
    current_time = time.strftime("%H:%M", time.localtime())
    current_seconds = time.strftime("%S", time.localtime())

    # Update the label


     #Call this function again after 1000 ms (1 second)
    app.after(1000, update_time)

rainy = False
drizzle = False
cloudy = False
sunny = False


currentTemp = round(w.current_temperature_2m)
currentAppTemp = round(w.current_apparent_temperature)





def updateWeather():
    rainy = False
    drizzle = False
    cloudy = False
    clear = False
    if w.current_cloud_cover < 50:
        clear = True
    elif w.current_cloud_cover > 50:
        cloudy = True
    elif w.current_rain < 0.1:
        drizzle = True
    elif w.current_rain > 0.1:
        rainy = True
    print(rainy, drizzle, cloudy, clear)

    if clear:
        weatherIconIm = Image.open("icon/sun.png")
        weatherIcon = ImageTk.PhotoImage(weatherIconIm)
    if cloudy:
        weatherIconIm = Image.open("icon/cloud.png")
        weatherIcon = ImageTk.PhotoImage(weatherIconIm)
    if drizzle:
        weatherIconIm = Image.open("icon/cloud-drizzle.png")
        weatherIcon = ImageTk.PhotoImage(weatherIconIm)
    if rainy:
        weatherIconIm = Image.open("icon/cloud-rain.png")
        weatherIcon = ImageTk.PhotoImage(weatherIconIm)

class app(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x480")
        self.show_frame(homeFrame1)
    update_time()
    updateWeather()
    def show_frame(self, frame_to_show):
        for frame in frames:
            frame.pack_forget()
        frame_to_show.pack(fill="both", expand=True)

weatherIconIm = Image.open("icon/cloud-rain.png")
weatherIcon = ImageTk.PhotoImage(weatherIconIm)
settingsIconIm = Image.open("icon/settings.png")
settingsIcon = ImageTk.PhotoImage(settingsIconIm)
clockIconIm = Image.open("icon/clock.png")
clockIcon = ImageTk.PhotoImage(clockIconIm)
musicIconIm = Image.open("icon/music.png")
musicIcon = ImageTk.PhotoImage(musicIconIm)
controlIconIm = Image.open("icon/sliders.png")
controlIcon = ImageTk.PhotoImage(controlIconIm)
gridIconIm = Image.open("icon/grid.png")
gridIcon = ImageTk.PhotoImage(gridIconIm)
youtubeIconIm = Image.open("icon/youtube.png")
youtubeIcon = ImageTk.PhotoImage(youtubeIconIm)
usersIconIm = Image.open("icon/users.png")
usersIcon = ImageTk.PhotoImage(usersIconIm)
monitorIconIm = Image.open("icon/monitor.png")
monitorIcon = ImageTk.PhotoImage(monitorIconIm)
homeIconIm = Image.open("icon/smallHome.png")
homeIcon = ImageTk.PhotoImage(homeIconIm)

class homeFrame(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        hFrame = ctk.CTkFrame(root)

        controlButton = ctk.CTkButton(hFrame, text="", image=controlIcon, height=150, width=170,
                                      font=("segoe ui light", 40),
                                      command=lambda: (app.show_frame(controlFrame), updateWeather()))
        controlButton.place(relx=0.275, rely=0.38, anchor=CENTER)
        weatherButton = ctk.CTkButton(hFrame, image=weatherIcon, text="", height=150, width=170,
                                      font=("segoe ui light", 40),
                                      command=lambda: (app.show_frame(weatherFrame), updateWeather()))
        weatherButton.place(relx=0.5, rely=0.38, anchor=CENTER)
        settingsButton = ctk.CTkButton(hFrame, text="", image=settingsIcon, height=150, width=170,
                                       font=("segoe ui light", 40),
                                       command=lambda: (app.show_frame(settingsFrame), updateWeather()))
        settingsButton.place(relx=0.725, rely=0.38, anchor=CENTER)
        alarmButton = ctk.CTkButton(hFrame, text="", image=clockIcon, height=150, width=170,
                                    font=("segoe ui light", 40),
                                    command=lambda: (app.show_frame(clockFrame), updateWeather()))
        alarmButton.place(relx=0.725, rely=0.72, anchor=CENTER)
        musicButton = ctk.CTkButton(hFrame, text="", image=musicIcon, height=150, width=170,
                                    font=("segoe ui light", 40))
        musicButton.place(relx=0.5, rely=0.72, anchor=CENTER)
        appsButton = ctk.CTkButton(hFrame, text="", image=gridIcon, height=150, width=170,
                                   font=("segoe ui light", 40),
                                   command=lambda: (app.show_frame(appsFrame), updateWeather()))
        appsButton.place(relx=0.275, rely=0.72, anchor=CENTER)
        weatherLabel = ctk.CTkLabel(hFrame, text=str(currentTemp) + "°", font=("segoe ui light", 60))
        weatherLabel.place(relx=0.085, rely=0.1, anchor="c")
        self.timeLabel = ctk.CTkLabel(hFrame, text="", font=("segoe ui light", 30))
        self.timeLabel.place(relx=0.9, rely=0.1, anchor="c")

homeFrame1 = homeFrame(app)

class controlFrame(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        controlFrame = ctk.CTkFrame(root)
        timeLabelCtrl = ctk.CTkLabel(controlFrame, text="", font=("segoe ui light", 30))
        timeLabelCtrl.place(relx=0.9, rely=0.1, anchor="c")
        homeButtonCtrl = ctk.CTkButton(controlFrame, image=homeIcon, text="", height=52, width=52,
                                       command=lambda: (app.show_frame(homeFrame), updateWeather()))
        homeButtonCtrl.place(relx=0.06, rely=0.1)

controlFrame1 = controlFrame(app)

class weatherFrame(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        wFrame = ctk.CTkFrame(root)
        timeLabelWthr = ctk.CTkLabel(wFrame, text="", font=("segoe ui light", 30))
        timeLabelWthr.place(relx=0.9, rely=0.1, anchor="c")
        tempLabelWthr = ctk.CTkLabel(wFrame, text=str(currentTemp) + "°", font=("segoe ui light", 100))
        tempLabelWthr.place(relx=0.06, rely=0.425, anchor="w")
        appTempLabel = ctk.CTkLabel(wFrame, text=f"Feels like {currentAppTemp}°", font=("segoe ui light", 30),
                                    text_color="#e0e0e0")
        appTempLabel.place(relx=0.06, rely=0.575, anchor="w")
        homeButtonWthr = ctk.CTkButton(wFrame, text="", image=homeIcon, height=52, width=52,
                                       command=lambda: app.show_frame(homeFrame))
        homeButtonWthr.place(relx=0.06, rely=0.1)

weatherFrame1 = weatherFrame(app)

settingsFrame = ctk.CTkFrame(app)

homeButtonStgs = ctk.CTkButton(settingsFrame, text="", image=homeIcon, height=52, width=52, command=lambda:app.show_frame(homeFrame))
homeButtonStgs.place(relx = 0.06, rely = 0.1)

class appsFrame(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        aFrame = ctk.CTkFrame(root)
        homeButtonApps = ctk.CTkButton(aFrame, text="", image=homeIcon, height=52, width=52,command=lambda: app.show_frame(homeFrame))
        homeButtonApps.place(relx=0.06, rely=0.1)
        guestModeButton = ctk.CTkButton(aFrame, text="", image=usersIcon, height=150, width=150)
        guestModeButton.place(relx=0.275, rely=0.175, anchor=CENTER)
        desktopModeButton = ctk.CTkButton(aFrame, text="", image=monitorIcon, height=150, width=150)
        desktopModeButton.place(relx=0.5, rely=0.175, anchor=CENTER)
        youtubeButton = ctk.CTkButton(aFrame, text="", image=youtubeIcon, height=150, width=150)
        youtubeButton.place(relx=0.725, rely=0.175, anchor=CENTER)
        musicButtonApps = ctk.CTkButton(aFrame, text="", image=musicIcon, height=150, width=150)
        musicButtonApps.place(relx=0.275, rely=0.5, anchor=CENTER)

appsFrame1 = appsFrame(app)

appsScrollFrame = ctk.CTkScrollableFrame

clockFrame = ctk.CTkFrame(app)
timeLabelClk = ctk.CTkLabel(clockFrame, text="", font=("segoe ui light",180))
timeLabelClk.place(relx = 0.5, rely = 0.3, anchor=CENTER)
homeButtonClk = ctk.CTkButton(clockFrame, text="", image=homeIcon, height=52, width=52, command=lambda:app.show_frame(homeFrame))
homeButtonClk.place(relx = 0.06, rely = 0.1)

frames = [homeFrame1, controlFrame1, weatherFrame1, appsFrame1,]

if __name__ == "__main__":
    app = app()
    app.mainloop()

