import tkinter as tk
import time
from datetime import date

def clock():
    current_time = time.strftime("%I:%M:%S %p")
    current_date = date.today().strftime("%B %d, %Y")
    current_day = date.today().strftime("%A")
    clock_label.config(text=current_time)
    date_label.config(text=current_date)
    day_label.config(text=current_day)
    clock_label.after(900, clock)

# Create the main window
window = tk.Tk()
window.title("Digital Clock")
window.geometry("500x250")
window.resizable(False, False)
window.configure(bg="white")

# Create clock label
clock_label = tk.Label(window, font=("Arial Rounded MT Bold", 50), fg="black", bg="pink")
clock_label.pack(pady=5)
# Create date label
date_label = tk.Label(window, font=("Arial Rounded MT Bold", 30), fg="black", bg="pink")
date_label.pack()

# Create day label
day_label = tk.Label(window, font=("Arial Rounded MT Bold", 30), fg="black", bg="pink")
day_label.pack()

# Update the clock display
clock()

# Start the main loop
window.mainloop()