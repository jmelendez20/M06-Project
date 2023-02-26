import tkinter as tk
from tkinter import messagebox
# Functions to convert certain measurements

## Function 1 = Cups to ounces OR ounces to cups
### def CupTOounces():
    # Get the cups from the user
    ###cup = float(cupEntry.get())
    
    # Convert cups to ounces
    ###ounces = 8 * cup
    
    # Display the result
    ###ounceResult.config(text=str(cup) "ounces")

    
# Create the main window
window1 = tk.Tk()
window1.title("Measurement Converter")
window1.geometry("600x300")

# Creating a introduction/greeting
greeting1 = tk.Label(window1, text = "Hello!\nWelcome to the measurement converter!",
    fg = "white",
    bg = "#FDB4A6",
    width = "50",
    font = ("Impact", 20)
)
greeting1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

# Creating a entry widget to explain what this program does

introduction = tk.Label(window1, text = "This program is created to simplify anyones life when it comes\n to converting measurements to other measurements, \nThis program will convert it to its most accurate conversion.",
        fg = "white",
    bg = "#FDB4A6",
    width = "50",
    font = ("Impact", 15)
)
introduction.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

    
# Creating a way to guide the user to which conversion they would like to use
def popup1(CupToOunces):
    messagebox.showinfo("This is a popup", "This will be the conversion!")
    
button1 = tk.Button(window1, text = "Cups to Ounces",
        command = popup1,           
        fg = "white",
        bg = "#FDB4A6",
        width = "50",
        font = ("Impact", 15)   
    )
button1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
def popup2():
    messagebox.showinfo("This is a popup", "This will be the conversion!")
    
button2 = tk.Button(window1, text = "Ounces to Cups",
        command = popup2,           
        fg = "white",
        bg = "#FDB4A6",
        width = "50",
        font = ("Impact", 15)   
    )
button2.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    
# Run the main loop
window1.mainloop()