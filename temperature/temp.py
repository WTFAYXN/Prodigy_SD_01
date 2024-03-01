# Import the necessary modules
from tkinter import Tk, Label, Button, Entry, StringVar

# Define the conversion functions
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def celsius_to_fahrenheit(celsius):
    return 9.0/5.0 * celsius + 32

# Define the TemperatureConverter class
class TemperatureConverter:
    def __init__(self, master):
        self.master = master
        master.title("Temperature Converter")

        # Set the window size to half the screen size
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        master.geometry(f"{screen_width//2}x{screen_height//2}")

        # Set the background color to black
        master.configure(bg='black')

        self.temp_var = StringVar()

        self.label = Label(master, text="Enter temperature:", bg='black', fg='white')
        self.label.pack()

        self.entry = Entry(master, textvariable=self.temp_var, bg='black', fg='white')
        self.entry.pack()

        self.f_to_c_button = Button(master, text="Fahrenheit to Celsius", command=self.f_to_c, bg='black', fg='white')
        self.f_to_c_button.pack()

        self.c_to_f_button = Button(master, text="Celsius to Fahrenheit", command=self.c_to_f, bg='black', fg='white')
        self.c_to_f_button.pack()

        self.result_label = Label(master, text="", bg='black', fg='white')
        self.result_label.pack()

    def f_to_c(self):
        fahrenheit = float(self.temp_var.get())
        celsius = fahrenheit_to_celsius(fahrenheit)
        self.result_label.config(text=f"{fahrenheit} Fahrenheit is {celsius} Celsius.")

    def c_to_f(self):
        celsius = float(self.temp_var.get())
        fahrenheit = celsius_to_fahrenheit(celsius)
        self.result_label.config(text=f"{celsius} Celsius is {fahrenheit} Fahrenheit.")

# Create a window and start the application
root = Tk()
my_converter = TemperatureConverter(root)
root.mainloop()
