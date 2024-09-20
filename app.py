import time
import subprocess
import tkinter as tk
from tkinter import ttk
from threading import Thread

def notify(title, message):
    try:
        print(f"Sending notification: {title} - {message}")  # Debugging output
        subprocess.run(["notify-send", title, message], check=True)
        # Uncomment if you want to include sound
        # subprocess.run(["paplay", "/usr/share/sounds/freedesktop/stereo/message.oga"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error sending notification: {e}")

def start_timer():
    try:
        break_interval_minutes = int(interval_choice.get())
        break_duration_minutes = int(break_duration.get())
        
        print(f"Break interval set to: {break_interval_minutes} minutes")  # Debugging output
        print(f"Break duration set to: {break_duration_minutes} minutes")  # Debugging output
        
        button_start.config(state=tk.DISABLED)
        
        def timer():
            while True:
                print("Waiting for break interval...")  # Debugging output
                time.sleep(break_interval_minutes * 60)
                notify("Time to rest your eyesight!", f"Take a {break_duration_minutes}-minute break.")
                
                print("Break period ended, waiting for next interval...")  # Debugging output
                time.sleep(break_duration_minutes * 60)
                notify("Break Over", "Your break is over, let's get back to work!")
        
        Thread(target=timer, daemon=True).start()
    except ValueError as e:
        print(f"Error in timer settings: {e}")

root = tk.Tk()
root.title("Medusa")
root.geometry("300x200")

label_interval = tk.Label(root, text="Choose the interval between breaks (in minutes):")
label_interval.pack(pady=10)

interval_choice = ttk.Combobox(root, values=[30, 45, 60, 90])
interval_choice.set(30)  # Set default value
interval_choice.pack(pady=10)

label_break = tk.Label(root, text="Choose the duration of your break (in minutes):")
label_break.pack(pady=10)

break_duration = ttk.Combobox(root, values=[5, 10])
break_duration.set(5)  # Set default value
break_duration.pack(pady=10)

button_start = tk.Button(root, text="Start Timer", command=start_timer)
button_start.pack(pady=10)

root.mainloop()
