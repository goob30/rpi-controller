import weather as w
from tkinter import *
import customtkinter as ctk
import time
import rpi
from PIL import Image, ImageTk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def update_time():
    current_time = time.strftime("%H:%M", time.localtime())
    current_seconds = time.strftime("%S", time.localtime())
    app.after(1000, update_time)


rainy = False
drizzle = False
cloudy = False
sunny = False

font = "segoeuil"

heaterMotorPos = 4
controlFrameHeaterText = ""

def heaterMotor():
    global heaterMotorPos
    global controlFrameHeaterText
    heaterMotorPos += 1
    heaterMotorPos = heaterMotorPos % 4

    controlFrameHeaterText = f"Heater\n{heaterMotorPos}"
    print(controlFrameHeaterText)

heaterMotor()

currentTemp = round(w.current_temperature_2m)
currentAppTemp = round(w.current_apparent_temperature)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x480")
        self.frames = {}  # Store frames

        # Load icons here, after the main window is created
        self.load_icons()

        for F in (HomeFrame, ControlFrame, lightControlFrame, roomControlFrame, climControlFrame, WeatherFrame, AppsFrame, SettingsFrame):
            frame = F(self)  # Pass app instance
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)  # Use place for layout management

        self.show_frame(HomeFrame)  # Show the home frame by default

    def load_icons(self):
        global homeIcon, controlIcon, weatherIcon, settingsIcon
        global clockIcon, musicIcon, gridIcon, youtubeIcon, usersIcon, monitorIcon, sunIcon, cloudyIcon, drizzleIcon, rainIcon, thermIcon

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
        sunIcon = ImageTk.PhotoImage(Image.open("icon/sun.png"))
        cloudyIcon = ImageTk.PhotoImage(Image.open("icon/cloud.png"))
        drizzleIcon = ImageTk.PhotoImage(Image.open("icon/cloud-drizzle.png"))
        rainIcon = ImageTk.PhotoImage(Image.open("icon/cloud-rain.png"))
        thermIcon = ImageTk.PhotoImage(Image.open("icon/thermometer.png"))

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()  # Bring the selected frame to the front

def updateWeather():
    global rainy, drizzle, cloudy, clear
    global weatherIcon
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
        weatherIcon = sunIcon
    elif cloudy:
        weatherIcon = cloudyIcon
    elif drizzle:
        weatherIcon = drizzleIcon
    elif rainy:
        weatherIcon = rainIcon

    print(clear, cloudy, drizzle, rainy)

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

        settingsButton = ctk.CTkButton(self, text="", image=settingsIcon, height=150, width=170,
                                       font=("segoe ui light", 40),
                                       command=lambda: (app.show_frame(SettingsFrame), updateWeather()))
        settingsButton.place(relx=0.725, rely=0.38, anchor=CENTER)

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

        global controlFrameHeaterText

        self.homeButton = ctk.CTkButton(self, image=homeIcon, text="", height=52, width=52,
                                        command=lambda: (app.show_frame(HomeFrame)))
        self.homeButton.place(relx=0.06, rely=0.1)

        self.lightButton = ctk.CTkButton(self, text="", image=sunIcon, height = 400, width=170, command=lambda:(app.show_frame(lightControlFrame)))
        self.lightButton.place(relx = 0.275, rely = 0.5, anchor=CENTER)

        self.roomButton = ctk.CTkButton(self, text="", image=controlIcon, height = 400, width=170, command=lambda:(app.show_frame(roomControlFrame)))
        self.roomButton.place(relx = 0.5, rely = 0.5, anchor=CENTER)

        self.climButton = ctk.CTkButton(self, text="", image=thermIcon, height=400, width=170, command=lambda:(app.show_frame(climControlFrame)))
        self.climButton.place(relx=0.725, rely=0.5, anchor=CENTER)

        #
        # self.potLightButton = ctk.CTkButton(self, text="Pot\nLights", height=150, width=170,
        #                                     font=("segoe ui light", 40),
        #                                     command=lambda: ())
        # self.potLightButton.place(relx=0.275, rely=0.38, anchor=CENTER)
        #
        # self.ledButton = ctk.CTkButton(self, text="Room\nLED", height=150, width=170,
        #                                font=("segoe ui light", 40),
        #                                command=lambda: (updateWeather()))
        # self.ledButton.place(relx=0.5, rely=0.38, anchor=CENTER)
        #
        # self.fanButton = ctk.CTkButton(self, text="Fan\nControl", height=150, width=170,
        #                                font=("segoe ui light", 40),
        #                                command=lambda: (updateWeather()))
        # self.fanButton.place(relx=0.725, rely=0.38, anchor=CENTER)
        #
        # self.heaterButton = ctk.CTkButton(self, text=controlFrameHeaterText, height=150, width=170,
        #                                   font=("segoe ui light", 40),
        #                                   command=lambda: (heaterMotor()))
        # self.heaterButton.place(relx=0.725, rely=0.72, anchor=CENTER)
        #
        # self.projectorButton = ctk.CTkButton(self, text="Toggle\nProjector", height=150, width=170,
        #                                      font=("segoe ui light", 40))
        # self.projectorButton.place(relx=0.5, rely=0.72, anchor=CENTER)
        #
        # self.bedLightButton = ctk.CTkButton(self, text="Bed\nLights", height=150, width=170,
        #                                     font=("segoe ui light", 40),
        #                                     command=lambda: ())
        # self.bedLightButton.place(relx=0.275, rely=0.72, anchor=CENTER)

class lightControlFrame(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.homeButton = ctk.CTkButton(self, text="", image=homeIcon, height=52, width=52,
                                       command=lambda: app.show_frame(HomeFrame))
        self.homeButton.place(relx=0.06, rely=0.1)


class roomControlFrame(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.homeButton = ctk.CTkButton(self, text="", image=homeIcon, height=52, width=52,
                                        command=lambda: app.show_frame(HomeFrame))
        self.homeButton.place(relx=0.06, rely=0.1)

class climControlFrame(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.homeButton = ctk.CTkButton(self, text="", image=homeIcon, height=52, width=52,
                                        command=lambda: app.show_frame(HomeFrame))
        self.homeButton.place(relx=0.06, rely=0.1)


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

        # Create a scrollable frame for settings
        self.scrollable_frame = ctk.CTkScrollableFrame(self, height=400)
        self.scrollable_frame.pack(fill="both", expand=True)

        # Add toggle switches to the scrollable frame
        self.toggle_var1 = ctk.StringVar(value="off")
        self.toggle_var2 = ctk.StringVar(value="off")
        self.toggle_var3 = ctk.StringVar(value="off")

        # Toggle Switch 1
        self.toggle1 = ctk.CTkSwitch(self.scrollable_frame, text="Setting 1", variable=self.toggle_var1,
                                     font=("segoe ui light", 30)
                                     , width=30)
        self.toggle1.pack(pady=10)

        # Toggle Switch 2
        self.toggle2 = ctk.CTkSwitch(self.scrollable_frame, text="Setting 2", variable=self.toggle_var2,
                                     font=("segoe ui light", 30)
                                     , width=30)
        self.toggle2.pack(pady=10)

        # Toggle Switch 3
        self.toggle3 = ctk.CTkSwitch(self.scrollable_frame, text="Setting 3", variable=self.toggle_var3,
                                     font=("segoe ui light", 30)
                                     , width=30)
        self.toggle3.pack(pady=10)

        # Add a home button
        homeButtonStgs = ctk.CTkButton(self.scrollable_frame, text="", image=homeIcon, height=52, width=52,
                                       command=lambda: app.show_frame(HomeFrame))
        homeButtonStgs.pack(side="top", anchor="nw", padx=10, pady=10)

    def start_scroll(self, event):
        """Store the initial position when mouse button is pressed."""
        self.prev_y = event.y

    def do_scroll(self, event):
        """Scroll the frame based on mouse movement."""
        if self.prev_y is not None:
            delta_y = self.prev_y - event.y
            self.scrollable_frame.yview_scroll(int(delta_y / 20), "units")  # Adjust the divisor for scroll speed
            self.prev_y = event.y

    def end_scroll(self, event):
        """Reset the previous y position when mouse button is released."""
        self.prev_y = None


class AppsFrame(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        homeButtonApps = ctk.CTkButton(self, text="", image=homeIcon, height=52, width=52,
                                       command=lambda: app.show_frame(HomeFrame))
        homeButtonApps.place(relx=0.06, rely=0.1)

        guestModeButton = ctk.CTkButton(self, text="", image=usersIcon, height=150, width=150, command=lambda: (exit()))
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
