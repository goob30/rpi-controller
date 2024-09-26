import weather as w
from tkinter import *
import customtkinter as ctk
import time
from PIL import Image, ImageTk

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Initialize app class
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x480")
        self.frames = {}  # Store frames
        self.frame_container = ctk.CTkFrame(self)
        self.frame_container.pack(fill="both", expand=True)

        # Create frames
        for F in (HomeFrame, ControlFrame, WeatherFrame, AppsFrame):
            frame = F(self.frame_container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomeFrame)  # Show the home frame by default

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()  # Bring the selected frame to the front

# Define individual frames
class HomeFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # Reference to the main app
        self.create_widgets()

    def create_widgets(self):
        controlButton = ctk.CTkButton(self, text="Control", command=lambda: self.controller.show_frame(ControlFrame))
        controlButton.pack(pady=20)

        weatherButton = ctk.CTkButton(self, text="Weather", command=lambda: self.controller.show_frame(WeatherFrame))
        weatherButton.pack(pady=20)

        appsButton = ctk.CTkButton(self, text="Apps", command=lambda: self.controller.show_frame(AppsFrame))
        appsButton.pack(pady=20)

class ControlFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        homeButton = ctk.CTkButton(self, text="Home", command=lambda: self.controller.show_frame(HomeFrame))
        homeButton.pack(pady=20)

        # Add more control-specific buttons as needed
        self.controlLabel = ctk.CTkLabel(self, text="Control Frame", font=("segoe ui light", 30))
        self.controlLabel.pack(pady=20)

class WeatherFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        homeButton = ctk.CTkButton(self, text="Home", command=lambda: self.controller.show_frame(HomeFrame))
        homeButton.pack(pady=20)

        self.weatherLabel = ctk.CTkLabel(self, text="Weather Frame", font=("segoe ui light", 30))
        self.weatherLabel.pack(pady=20)

class AppsFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        homeButton = ctk.CTkButton(self, text="Home", command=lambda: self.controller.show_frame(HomeFrame))
        homeButton.pack(pady=20)

        self.appsLabel = ctk.CTkLabel(self, text="Apps Frame", font=("segoe ui light", 30))
        self.appsLabel.pack(pady=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()
