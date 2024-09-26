import weather as w
from tkinter import *
import customtkinter as ctk
import time
from PIL import Image, ImageTk

from main2notused import settingsIcon

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def update_time():
    current_time = time.strftime("%H:%M", time.localtime())
    current_seconds = time.strftime("%S", time.localtime())
    app.after(1000, update_time)


# Weather conditions
rainy = False
drizzle = False
cloudy = False
sunny = False

currentTemp = round(w.current_temperature_2m)
currentAppTemp = round(w.current_apparent_temperature)


def updateWeather():
    global rainy, drizzle, cloudy, clear
    rainy = drizzle = cloudy = clear = False
    if w.current_cloud_cover < 50:
        clear = True
    elif w.current_cloud_cover > 50:
        cloudy = True
    elif w.current_rain < 0.1:
        drizzle = True
    elif w.current_rain > 0.1:
        rainy = True

    if clear:
        weatherIconIm = Image.open("icon/sun.png")
    elif cloudy:
        weatherIconIm = Image.open("icon/cloud.png")
    elif drizzle:
        weatherIconIm = Image.open("icon/cloud-drizzle.png")
    elif rainy:
        weatherIconIm = Image.open("icon/cloud-rain.png")

    global weatherIcon
    weatherIcon = ImageTk.PhotoImage(weatherIconIm)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x480")
        self.frames = {}  # Store frames

        # Load icons here, after the main window is created
        self.load_icons()

        for F in (HomeFrame, ControlFrame, WeatherFrame, AppsFrame):
            frame = F(self)  # Pass app instance
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)  # Use place for layout management

        self.show_frame(HomeFrame)  # Show the home frame by default

    def load_icons(self):
        global homeIcon, controlIcon, weatherIcon, settingsIcon
        global clockIcon, musicIcon, gridIcon, youtubeIcon, usersIcon, monitorIcon

        homeIcon = ImageTk.PhotoImage(Image.open("icon/smallHome.png"))
        controlIcon = ImageTk.PhotoImage(Image.open("icon/sliders.png"))
        weatherIcon = ImageTk.PhotoImage(Image.open("icon/cloud-rain.png"))
        settingsIcon = ImageTk.PhotoImage(Image.open("icon/settings.png"))
        clockIcon = ImageTk.PhotoImage(Image.open("icon/clock.png"))
        musicIcon = ImageTk.PhotoImage(Image.open("icon/music.png"))
        gridIcon = ImageTk.PhotoImage(Image.open("icon/grid.png"))
        youtubeIcon = ImageTk.PhotoImage(Image.open("icon/youtube.png"))
        usersIcon = ImageTk.PhotoImage(Image.open("icon/users.png"))
        monitorIcon = ImageTk.PhotoImage(Image.open("icon/monitor.png"))

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()  # Bring the selected frame to the front


class HomeFrame(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        controlButton = ctk.CTkButton(self, text="", image=controlIcon, height=150, width=170,
                                      font=("segoe ui light", 40),
                                      command=lambda: (app.show_frame(ControlFrame), updateWeather()))
        controlButton.place(relx=0.275, rely=0.38, anchor=CENTER)

        weatherButton = ctk.CTkButton(self, text="", image=weatherIcon, height=150, width=170,
                                      font=("segoe ui light", 40),
                                      command=lambda: (app.show_frame(WeatherFrame), updateWeather()))
        weatherButton.place(relx=0.5, rely=0.38, anchor=CENTER)

          # Removed this line or comment it out


        alarmButton = ctk.CTkButton(self, text="", image=clockIcon, height=150, width=170,
                                    font=("segoe ui light", 40),
                                    command=lambda: app.show_frame(ClockFrame))
        alarmButton.place(relx=0.725, rely=0.72, anchor=CENTER)

        musicButton = ctk.CTkButton(self, text="", image=musicIcon, height=150, width=170,
                                    font=("segoe ui light", 40))
        musicButton.place(relx=0.5, rely=0.72, anchor=CENTER)

        appsButton = ctk.CTkButton(self, text="", image=gridIcon, height=150, width=170,
                                   font=("segoe ui light", 40),
                                   command=lambda: (app.show_frame(AppsFrame), updateWeather()))
        appsButton.place(relx=0.275, rely=0.72, anchor=CENTER)

        weatherLabel = ctk.CTkLabel(self, text=str(currentTemp) + "°", font=("segoe ui light", 60))
        weatherLabel.place(relx=0.085, rely=0.1, anchor="c")

        self.timeLabel = ctk.CTkLabel(self, text="", font=("segoe ui light", 30))
        self.timeLabel.place(relx=0.9, rely=0.1, anchor="c")


class ControlFrame(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        homeButtonCtrl = ctk.CTkButton(self, image=homeIcon, text="", height=52, width=52,
                                       command=lambda: app.show_frame(HomeFrame))
        homeButtonCtrl.place(relx=0.06, rely=0.1)

        self.controlLabel = ctk.CTkLabel(self, text="Control Frame", font=("segoe ui light", 30))
        self.controlLabel.place(relx=0.5, rely=0.5, anchor="center")


class WeatherFrame(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        homeButtonWthr = ctk.CTkButton(self, text="", image=homeIcon, height=52, width=52,
                                       command=lambda: app.show_frame(HomeFrame))
        homeButtonWthr.place(relx=0.06, rely=0.1)

        tempLabelWthr = ctk.CTkLabel(self, text=str(currentTemp) + "°", font=("segoe ui light", 100))
        tempLabelWthr.place(relx=0.06, rely=0.425, anchor="w")

        appTempLabel = ctk.CTkLabel(self, text=f"Feels like {currentAppTemp}°", font=("segoe ui light", 30),
                                    text_color="#e0e0e0")
        appTempLabel.place(relx=0.06, rely=0.575, anchor="w")

class SettingsFrame(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        homeButtonStgs = ctk.CTkButton(self, text="", image=settingsIcon, height=52, width=52, command=lambda:app.show_frame(HomeFrame))
        homeButtonStgs.place(relx = 0.06, rely=0.1, anchor=CENTER)

class AppsFrame(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        homeButtonApps = ctk.CTkButton(self, text="", image=homeIcon, height=52, width=52,
                                       command=lambda: app.show_frame(HomeFrame))
        homeButtonApps.place(relx=0.06, rely=0.1)

        guestModeButton = ctk.CTkButton(self, text="", image=usersIcon, height=150, width=150)
        guestModeButton.place(relx=0.275, rely=0.175, anchor=CENTER)

        desktopModeButton = ctk.CTkButton(self, text="", image=monitorIcon, height=150, width=150)
        desktopModeButton.place(relx=0.5, rely=0.175, anchor=CENTER)

        youtubeButton = ctk.CTkButton(self, text="", image=youtubeIcon, height=150, width=150)
        youtubeButton.place(relx=0.725, rely=0.175, anchor=CENTER)

        musicButtonApps = ctk.CTkButton(self, text="", image=musicIcon, height=150, width=150)
        musicButtonApps.place(relx=0.275, rely=0.5, anchor=CENTER)


class ClockFrame(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        homeButtonClock = ctk.CTkButton(self, text="", image=homeIcon, height=52, width=52,
                                        command=lambda: app.show_frame(HomeFrame))
        homeButtonClock.place(relx=0.06, rely=0.1)

        self.clockLabel = ctk.CTkLabel(self, text="Clock Frame", font=("segoe ui light", 30))
        self.clockLabel.place(relx=0.5, rely=0.5, anchor="center")


if __name__ == "__main__":
    app = App()
    update_time()  # Start updating time
    app.mainloop()
