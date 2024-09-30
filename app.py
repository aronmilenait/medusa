import tkinter as tk
from tkinter import ttk
from threading import Thread
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from timer_logic import *

root = ttk.Window(themename="minty")
root.title("Medusa")
root.geometry("400x300")

def on_start_button_click():
    try:
        break_interval_minutes = int(interval_minutes_entry.get())
        break_duration_minutes = int(break_duration_minutes_entry.get())
        
        for widget in root.winfo_children():
            widget.pack_forget()
            
        message = f"You set up the timer to notify you to rest your eyes every {break_interval_minutes} minutes. Please, don't close the window."
        label_message = tk.Label(root, text=message, wraplength=300, justify=tk.CENTER)
        label_message.pack(pady=10)

        button_start.config(state=tk.DISABLED)
        start_timer(break_interval_minutes, break_duration_minutes, on_timer_end, on_break_end)
    except ValueError:
        print("Please enter valid integers for the time intervals.")

def on_timer_end():
    button_start.config(state=tk.NORMAL)

def on_break_end():
    button_start.config(state=tk.NORMAL)

label_interval = tk.Label(root, text="Choose the interval between breaks (in minutes)")
label_interval.pack(pady=10)

interval_minutes_entry = ttk.Combobox(root, values=[30, 45, 50, 60, 75, 90])
interval_minutes_entry.set(30)
interval_minutes_entry.pack(pady=10)

label_break = tk.Label(root, text="Choose the duration of your break (in minutes)")
label_break.pack(pady=10)

break_duration_minutes_entry = ttk.Combobox(root, values=[5, 10, 15])
break_duration_minutes_entry.set(5)
break_duration_minutes_entry.pack(pady=10)

button_start = ttk.Button(root, text="Start", command=on_start_button_click)
button_start.pack(pady=10)

root.mainloop()
