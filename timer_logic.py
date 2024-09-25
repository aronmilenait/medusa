import time
import subprocess
from threading import Thread

stop_timer = False

def notify(title, message):
    try:
        subprocess.run(["notify-send", title, message], check=True)
        subprocess.run(["paplay", "/usr/share/sounds/freedesktop/stereo/message.oga"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error sending notification: {e}")

def start_timer(break_interval_minutes, break_duration_minutes, on_timer_end, on_break_end):
    global stop_timer
    stop_timer = False  

    def timer():
        while not stop_timer:
            time.sleep(break_interval_minutes * 60)
            if stop_timer: 
                break

            notify("Time to rest your eyesight!", f"Take a {break_duration_minutes}-minute break.")
            on_timer_end()  

            time.sleep(break_duration_minutes * 60) 
            if stop_timer: 
                break

            notify("Your break is over", "Let's get back to work!")
            on_break_end()  

    Thread(target=timer, daemon=True).start()  

def stop_timer_func():
    global stop_timer
    stop_timer = True  