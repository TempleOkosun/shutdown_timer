import tkinter as tk
import subprocess

# Set up the window and the frame to hold contents properly
window = tk.Tk()
window.title("Shutdown Timer")
frame = tk.Frame(master=window, width=500, height=400, bg='#37d3ff')
frame.pack()


# Create the needed functions
def shutdown():
    get_time = getvalue()
    subprocess.call(["shutdown", "-f", "-s", "-t", get_time])


def restart():
    get_time = getvalue()
    subprocess.call(["shutdown", "-f", "-r", "-t",  get_time])


def abort():
    subprocess.call(["shutdown", "-a"])


def close_window():
    window.destroy()


set_time = tk.StringVar()


def getvalue():
    input_time = set_time.get()
    # if not input_time:    #     input_time = '60'
    # else:
    #     input_time = input_time
    # return input_time
    input_time = input_time if input_time else '60'
    return input_time


# Process the provided time
enter_time = tk.Label(master=frame, text="Enter Time in Seconds:", bg='#37d3ff', font="TKFixedFont 10 bold").place(
    relx=0.14, rely=0.704)
entry = tk.Entry(master=frame, textvariable=set_time).place(relx=0.45, rely=0.700, height=25, width=120)


btn1 = tk.Button(master=frame, text="Shut Down", command=shutdown).place(relx=0.14, rely=0.300, height=30, relwidth=0.70)
btn2 = tk.Button(master=frame, text="Restart", command=restart).place(relx=0.14, rely=0.400, height=30, relwidth=0.70)
btn3 = tk.Button(master=frame, text="Abort", command=abort).place(relx=0.14, rely=0.500, height=30, relwidth=0.70)
btn4 = tk.Button(master=frame, text="Quit", command=close_window).place(relx=0.14, rely=0.600, height=30, relwidth=0.70)
info = tk.Label(master=frame, text="If you want to Control your PC do it!!!", bg='#37d3ff',
                font=("TKFixedFont 10 bold")).place(
    relx=0.24, rely=0.200, height=30, relwidth=0.500)


window.mainloop()


# Generate executable. pip install pyinstaller incase you dont have it already.
# The '.pyw' extension is used in this case to hide the terminal window from appearing when the program is running.
# pyinstaller.exe --onefile --icon=shutdown.ico shutdown_timer.pyw
