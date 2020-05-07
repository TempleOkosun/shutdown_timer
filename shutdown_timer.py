import tkinter as tk
import subprocess


def shutdown():
    subprocess.call(["shutdown", "-f", "-s", "-t", inputted_time])


def restart():
    subprocess.call(["shutdown", "-f", "-r", "-t",  inputted_time])


def abort():
    subprocess.call(["shutdown", "-a"])


def close_window():
    window.destroy()


window = tk.Tk()
window.title("Shutdown Timer")

frame = tk.Frame(master=window, width=500, height=400, bg='#37d3ff')
frame.pack()

btn1 = tk.Button(master=frame, text="Shut Down", command=shutdown).place(relx=0.14, rely=0.300, height=30, relwidth=0.70)
btn2 = tk.Button(master=frame, text="Restart", command=restart).place(relx=0.14, rely=0.400, height=30, relwidth=0.70)
btn3 = tk.Button(master=frame, text="Abort", command=abort).place(relx=0.14, rely=0.500, height=30, relwidth=0.70)
btn4 = tk.Button(master=frame, text="Quit", command=close_window).place(relx=0.14, rely=0.600, height=30, relwidth=0.70)
info = tk.Label(master=frame, text="If you want to Control your PC do it!!!", bg='#37d3ff',
                font=("TKFixedFont 10 bold")).place(
    relx=0.24, rely=0.200, height=30, relwidth=0.500)

# Process the provided time
store_time = tk.StringVar()
inputted_time = store_time.get()
if not inputted_time:
    inputted_time = "60"
else:
    inputted_time

entry = tk.Entry(master=frame, textvariable=store_time).place(relx=0.45, rely=0.700, height=25, width=120)
get_time = tk.Label(master=frame, text="Enter Time in Seconds:", bg='#37d3ff',font=("TKFixedFont 10 bold")).place(relx=0.14, rely=0.704)


window.mainloop()

# Generate executable
# pyinstaller.exe --onefile --icon=shutdown-img.ico shutdown_timer.pyw
