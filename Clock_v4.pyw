from time import strftime
from tkinter import *
import platform
from tkinter import messagebox
import pygame
from PIL import ImageTk, Image
from configparser import ConfigParser
from datetime import date
from tkcalendar import Calendar
from tkinter import ttk

root = Tk()
root.title("rthur's Alarm-Clock - V4")
root.geometry('552x350')
root.iconbitmap("C:\Clock\Clock_v4\\a13.ico")
root.config(bg="white")
root.resizable(0, 0)

master_frame = LabelFrame(root, text="", bg="white")
master_frame.pack(padx=6, pady=6)

pygame.mixer.init()

parser = ConfigParser()
parser.read("C:\Clock\Clock_v4\\alarm.ini")

alarm_one = parser.get('alarms', 'alarm_one')
alarm_two = parser.get('alarms', 'alarm_two')
alarm_three = parser.get('alarms', 'alarm_three')
alarm_jump = parser.get('alarms', 'alarm_jump')
condition1 = parser.get('alarms', 'condition1')
condition2 = parser.get('alarms', 'condition2')
condition3 = parser.get('alarms', 'condition3')

global condition
condition = False


def set_manual_time():
    hour_min_2.config(state=NORMAL)
    hour_min_3.config(state=NORMAL)

    hour_min_2.delete(0, END)
    hour_min_3.delete(0, END)

    hour_min_2.insert(0, f"{hour1.get()}:{min1.get()}")
    hour_min_3.insert(0, f"{hour2.get()}:{min2.get()}")

    save()

    hour_min_2.config(state=DISABLED)
    hour_min_3.config(state=DISABLED)

    clock_win.destroy()
    root.geometry('552x350')


def set_auto_time():
    hour_min_1.config(state=NORMAL)

    hour_min_1.delete(0, END)
    hour_min_1.insert(0, f"{hour1_auto.get()}:{min1_auto.get()}")

    save()

    hour_min_1.config(state=DISABLED)

    clock_auto_win.destroy()
    root.geometry('552x350')


def clock_def():
    global clock_win
    root.geometry('862x355')
    clock_win = LabelFrame(master_frame, bg="white", text="")
    clock_win.grid(row=0, column=2, pady=20, padx=20)

    frame_clock_1 = LabelFrame(clock_win, text="Set Manual Time Alarm 1", bg="white")
    frame_clock_1.grid(row=0, column=0, padx=5, pady=5)

    frame_clock_2 = LabelFrame(clock_win, text="Set Manual Time Alarm 2", bg="white")
    frame_clock_2.grid(row=1, column=0, padx=5, pady=5)

    frame_time_1_1 = LabelFrame(frame_clock_1, text="-- Set Hour -------- Set Minute --", bg="white")
    frame_time_2_2 = LabelFrame(frame_clock_2, text="-- Set Hour -------- Set Minute --", bg="white")
    frame_time_1_1.pack(padx=5, pady=5)
    frame_time_2_2.pack(padx=5, pady=5)

    global hour1, hour2, min1, min2

    # Hour
    hour_options = []

    for h in range(0, 24):
        hour_options.append(str(h))

    time_1 = str(hour_min_2.get())
    time_1 = time_1.split(":")

    time_2 = str(hour_min_3.get())
    time_2 = time_2.split(":")

    hour1 = ttk.Combobox(frame_time_1_1, value=hour_options, width=10)
    hour1.current(int(time_1[0]))
    hour1.grid(row=0, column=0, padx=5, pady=5)

    hour2 = ttk.Combobox(frame_time_2_2, value=hour_options, width=10)
    hour2.current(int(time_2[0]))
    hour2.grid(row=0, column=0, padx=5, pady=5)

    # Minutes
    min_options = []

    for m in range(0, 60):
        min_options.append(str(m))

    min1 = ttk.Combobox(frame_time_1_1, value=min_options, width=10)
    min1.current(int(time_1[1]))
    min1.grid(row=0, column=1, padx=5, pady=5)

    min2 = ttk.Combobox(frame_time_2_2, value=min_options, width=10)
    min2.current(int(time_2[1]))
    min2.grid(row=0, column=1, padx=5, pady=5)

    button = Button(clock_win, text="      << Save Manual Time Alarm      ", command=set_manual_time)
    button.grid(row=2, column=0, columnspan=2, pady=10)


def set_date_auto():
    month_day_1.config(state=NORMAL)

    global cal1_auto_date
    cal1_auto_date = str(cal_auto1.get_date()).split("/", 2)

    if cal1_auto_date[0] == "1":
        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Jan, {cal1_auto_date[1]}")

    elif cal1_auto_date[0] == "2":
        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Feb, {cal1_auto_date[1]}")

    elif cal1_auto_date[0] == "3":
        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Mar, {cal1_auto_date[1]}")

    elif cal1_auto_date[0] == "4":
        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Apr, {cal1_auto_date[1]}")

    elif cal1_auto_date[0] == "5":
        month_day_1.delete(0, END)
        month_day_1.insert(0, f"May, {cal1_auto_date[1]}")

    elif cal1_auto_date[0] == "6":
        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Jun, {cal1_auto_date[1]}")

    elif cal1_auto_date[0] == "7":
        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Jul, {cal1_auto_date[1]}")

    elif cal1_auto_date[0] == "8":
        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Aug, {cal1_auto_date[1]}")

    elif cal1_auto_date[0] == "9":
        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Sep, {cal1_auto_date[1]}")

    elif cal1_auto_date[0] == "10":
        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Oct, {cal1_auto_date[1]}")

    elif cal1_auto_date[0] == "11":
        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Nov, {cal1_auto_date[1]}")

    elif cal1_auto_date[0] == "12":
        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Dec, {cal1_auto_date[1]}")

    save()

    month_day_1.config(state=DISABLED)
    cal_auto_window.destroy()
    root.geometry('552x350')


def cal_auto_def():
    global cal_auto_window
    root.geometry('915x349')
    cal_auto_window = LabelFrame(master_frame, bg="white", text="")
    cal_auto_window.grid(row=0, column=2, pady=20, padx=20)

    global cal_auto1
    frame_calendar_1 = LabelFrame(cal_auto_window, text="Set Auto Day Alarm", bg="white")
    frame_calendar_1.grid(row=0, column=0, padx=5, pady=5)

    cal_auto1 = Calendar(frame_calendar_1, selectmode="day", year=int(strftime("%Y")), month=int(strftime("%m")),
                         day=int(strftime("%d")))
    cal_auto1.pack(padx=5, pady=5)

    frame_calendar_1.grid(row=0, column=0, padx=5, pady=5)

    # Buttons
    button1 = Button(cal_auto_window, text="                << Set Auto "
                                           "Day Alarm Values                ",
                     command=set_date_auto)
    button1.grid(row=1, column=0, columnspan=5, pady=5)


def set_date_two():
    month_day_2.config(state=NORMAL)
    month_day_3.config(state=NORMAL)

    global cal2_date
    cal2_date = str(cal2.get_date()).split("/", 2)

    global cal1_date
    cal1_date = str(cal1.get_date()).split("/", 2)

    if cal2_date[0] == "1":
        month_day_3.delete(0, END)
        month_day_3.insert(0, f"Jan, {cal2_date[1]}")

    elif cal2_date[0] == "2":
        month_day_3.delete(0, END)
        month_day_3.insert(0, f"Feb, {cal2_date[1]}")

    elif cal2_date[0] == "3":
        month_day_3.delete(0, END)
        month_day_3.insert(0, f"Mar, {cal2_date[1]}")

    elif cal2_date[0] == "4":
        month_day_3.delete(0, END)
        month_day_3.insert(0, f"Apr, {cal2_date[1]}")

    elif cal2_date[0] == "5":
        month_day_3.delete(0, END)
        month_day_3.insert(0, f"May, {cal2_date[1]}")

    elif cal2_date[0] == "6":
        month_day_3.delete(0, END)
        month_day_3.insert(0, f"Jun, {cal2_date[1]}")

    elif cal2_date[0] == "7":
        month_day_3.delete(0, END)
        month_day_3.insert(0, f"Jul, {cal2_date[1]}")

    elif cal2_date[0] == "8":
        month_day_3.delete(0, END)
        month_day_3.insert(0, f"Aug, {cal2_date[1]}")

    elif cal2_date[0] == "9":
        month_day_3.delete(0, END)
        month_day_3.insert(0, f"Sep, {cal2_date[1]}")

    elif cal2_date[0] == "10":
        month_day_3.delete(0, END)
        month_day_3.insert(0, f"Oct, {cal2_date[1]}")

    elif cal2_date[0] == "11":
        month_day_3.delete(0, END)
        month_day_3.insert(0, f"Nov, {cal2_date[1]}")

    elif cal2_date[0] == "12":
        month_day_3.delete(0, END)
        month_day_3.insert(0, f"Dec, {cal2_date[1]}")

    if cal1_date[0] == "1":
        month_day_2.delete(0, END)
        month_day_2.insert(0, f"Jan, {cal1_date[1]}")

    elif cal1_date[0] == "2":
        month_day_2.delete(0, END)
        month_day_2.insert(0, f"Feb, {cal1_date[1]}")

    elif cal1_date[0] == "3":
        month_day_2.delete(0, END)
        month_day_2.insert(0, f"Mar, {cal1_date[1]}")

    elif cal1_date[0] == "4":
        month_day_2.delete(0, END)
        month_day_2.insert(0, f"Apr, {cal1_date[1]}")

    elif cal1_date[0] == "5":
        month_day_2.delete(0, END)
        month_day_2.insert(0, f"May, {cal1_date[1]}")

    elif cal1_date[0] == "6":
        month_day_2.delete(0, END)
        month_day_2.insert(0, f"Jun, {cal1_date[1]}")

    elif cal1_date[0] == "7":
        month_day_2.delete(0, END)
        month_day_2.insert(0, f"Jul, {cal1_date[1]}")

    elif cal1_date[0] == "8":
        month_day_2.delete(0, END)
        month_day_2.insert(0, f"Aug, {cal1_date[1]}")

    elif cal1_date[0] == "9":
        month_day_2.delete(0, END)
        month_day_2.insert(0, f"Sep, {cal1_date[1]}")

    elif cal1_date[0] == "10":
        month_day_2.delete(0, END)
        month_day_2.insert(0, f"Oct, {cal1_date[1]}")

    elif cal1_date[0] == "11":
        month_day_2.delete(0, END)
        month_day_2.insert(0, f"Nov, {cal1_date[1]}")

    elif cal1_date[0] == "12":
        month_day_2.delete(0, END)
        month_day_2.insert(0, f"Dec, {cal1_date[1]}")

    save()

    month_day_2.config(state=DISABLED)
    month_day_3.config(state=DISABLED)

    cal_win.destroy()
    root.geometry('552x350')


def calendar_def():
    global cal_win
    root.geometry('1200x355')
    cal_win = LabelFrame(master_frame, bg="white", text="")
    cal_win.grid(row=0, column=2, pady=20, padx=20)

    global cal1, cal2

    frame_calendar_1 = LabelFrame(cal_win, text="Set Manual Alarm 1", bg="white")
    frame_calendar_1.grid(row=0, column=0, padx=5, pady=5)

    frame_calendar_2 = LabelFrame(cal_win, text="Set Manual Alarm 2", bg="white")
    frame_calendar_2.grid(row=0, column=1, padx=5, pady=5)

    cal1 = Calendar(frame_calendar_1, selectmode="day", year=int(strftime("%Y")), month=int(strftime("%m")),
                    day=int(strftime("%d")))
    cal1.pack(padx=5, pady=5)

    cal2 = Calendar(frame_calendar_2, selectmode="day", year=int(strftime("%Y")), month=int(strftime("%m")),
                    day=int(strftime("%d")))
    cal2.pack(padx=5, pady=5)

    frame_calendar_1.grid(row=0, column=0, padx=5, pady=5)
    frame_calendar_2.grid(row=0, column=1, padx=5, pady=5)

    # Buttons
    button1 = Button(cal_win, text="                                                               << Set Manual Alarm "
                                   "Values                                                               ",
                     command=set_date_two)
    button1.grid(row=1, column=0, columnspan=5, pady=5)


def clock_auto_def():
    global clock_auto_win
    root.geometry('862x355')
    clock_auto_win = LabelFrame(master_frame, bg="white", text="")
    clock_auto_win.grid(row=0, column=2, pady=20, padx=20)

    frame_clock_1 = LabelFrame(clock_auto_win, text="Set Auto Time Alarm 1", bg="white")
    frame_clock_1.grid(row=0, column=0, padx=5, pady=5)

    frame_time_1_1 = LabelFrame(frame_clock_1, text="-- Set Hour -------- Set Minute --", bg="white")
    frame_time_1_1.pack(padx=5, pady=5)

    global hour1_auto, min1_auto

    # Hour
    hour_options = []

    for h in range(0, 24):
        hour_options.append(str(h))

    time_1 = str(hour_min_1.get())
    time_1 = time_1.split(":")

    hour1_auto = ttk.Combobox(frame_time_1_1, value=hour_options, width=10)
    hour1_auto.current(int(time_1[0]))
    hour1_auto.grid(row=0, column=0, padx=5, pady=5)

    # Minutes
    min_options = []

    for m in range(0, 60):
        min_options.append(str(m))

    min1_auto = ttk.Combobox(frame_time_1_1, value=min_options, width=10)
    min1_auto.current(int(time_1[1]))
    min1_auto.grid(row=0, column=1, padx=5, pady=5)

    button = Button(clock_auto_win, text="      << Save Manual Time Alarm      ", command=set_auto_time)
    button.grid(row=2, column=0, columnspan=2, pady=10)


def save_def():
    save()

    global condition
    condition = False

    root.geometry('552x350')


def calendar_auto_home_def():
    global cal_auto_win, entry, condition
    condition = True

    root.geometry('942x355')
    cal_auto_win = LabelFrame(master_frame, bg="white", text="")
    cal_auto_win.grid(row=0, column=2, pady=20, padx=20)

    parser = ConfigParser()
    parser.read("C:\Clock\Clock_v4\\alarm.ini")

    alarm_jump = parser.get('alarms', 'alarm_jump')

    frame = LabelFrame(cal_auto_win, text="Set How Many Days to Jump", bg="white")
    frame.grid(row=0, column=0, padx=10, pady=10)

    entry = Entry(frame, font=("Helvetica", 15), bg="white", bd=4)
    entry.pack(padx=20, pady=20)

    entry.insert(0, alarm_jump)

    # Buttons
    button1 = Button(frame, text="<< Set Set How Many Days to Jump", command=save_def)
    button1.pack(pady=5, padx=10, fill=X)


def save_futuro():
    parser = ConfigParser()
    parser.read("C:\Clock\Clock_v4\\alarm.ini")

    alarm_jump = parser.get("alarms", "alarm_jump")

    global futuro
    hj = date.today()
    futuro = date.fromordinal(hj.toordinal() + int(alarm_jump))

    futuro = str(futuro)
    futuro = futuro.split("-", 2)

    global futuro_mes
    hj = date.today()
    futuro_mes = f"{date.fromordinal(hj.toordinal() + int(alarm_jump))}"
    futuro_mes = futuro_mes.split("-", 2)

    month_day_1.config(state=NORMAL)

    if futuro_mes[2] == "01":
        parser.set('alarms', 'alarm_one', f"Jan, {int(futuro[2])}_{hour_min_1.get()}")
        alarm_one = parser.get('alarms', 'alarm_one')

        with open("C:\Clock\Clock_v4\\alarm.ini", "w") as configfile:
            parser.write(configfile)

        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Jan, {int(futuro[2])}")

    elif futuro_mes[1] == "02":
        parser.set('alarms', 'alarm_one', f"Feb, {int(futuro[2])}_{hour_min_1.get()}")
        alarm_one = parser.get('alarms', 'alarm_one')

        with open("C:\Clock\Clock_v4\\alarm.ini", "w") as configfile:
            parser.write(configfile)

        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Feb, {int(futuro[2])}")

    elif futuro_mes[1] == "03":
        parser.set('alarms', 'alarm_one', f"Mar, {int(futuro[2])}_{hour_min_1.get()}")
        alarm_one = parser.get('alarms', 'alarm_one')

        with open("C:\Clock\Clock_v4\\alarm.ini", "w") as configfile:
            parser.write(configfile)

        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Mar, {int(futuro[2])}")

    elif futuro_mes[1] == "04":
        parser.set('alarms', 'alarm_one', f"Apr, {int(futuro[2])}_{hour_min_1.get()}")
        alarm_one = parser.get('alarms', 'alarm_one')

        with open("C:\Clock\Clock_v4\\alarm.ini", "w") as configfile:
            parser.write(configfile)

        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Apr, {int(futuro[2])}")

    elif futuro_mes[1] == "05":
        parser.set('alarms', 'alarm_one', f"May, {int(futuro[2])}_{hour_min_1.get()}")
        alarm_one = parser.get('alarms', 'alarm_one')

        with open("C:\Clock\Clock_v4\\alarm.ini", "w") as configfile:
            parser.write(configfile)

        month_day_1.delete(0, END)
        month_day_1.insert(0, f"May, {int(futuro[2])}")

    elif futuro_mes[1] == "06":
        parser.set('alarms', 'alarm_one', f"Jun, {int(futuro[2])}_{hour_min_1.get()}")
        alarm_one = parser.get('alarms', 'alarm_one')

        with open("C:\Clock\Clock_v4\\alarm.ini", "w") as configfile:
            parser.write(configfile)

        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Jun, {int(futuro[2])}")

    elif futuro_mes[1] == "07":
        parser.set('alarms', 'alarm_one', f"Jul, {int(futuro[2])}_{hour_min_1.get()}")
        alarm_one = parser.get('alarms', 'alarm_one')

        with open("C:\Clock\Clock_v4\\alarm.ini", "w") as configfile:
            parser.write(configfile)

        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Jul, {int(futuro[2])}")

    elif futuro_mes[1] == "08":
        parser.set('alarms', 'alarm_one', f"Aug, {int(futuro[2])}_{hour_min_1.get()}")
        alarm_one = parser.get('alarms', 'alarm_one')

        with open("C:\Clock\Clock_v4\\alarm.ini", "w") as configfile:
            parser.write(configfile)

        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Aug, {int(futuro[2])}")

    elif futuro_mes[1] == "09":
        parser.set('alarms', 'alarm_one', f"Sep, {int(futuro[2])}_{hour_min_1.get()}")
        alarm_one = parser.get('alarms', 'alarm_one')

        with open("C:\Clock\Clock_v4\\alarm.ini", "w") as configfile:
            parser.write(configfile)

        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Sep, {int(futuro[2])}")

    elif futuro_mes[1] == "10":
        parser.set('alarms', 'alarm_one', f"Oct, {int(futuro[2])}_{hour_min_1.get()}")
        alarm_one = parser.get('alarms', 'alarm_one')

        with open("C:\Clock\Clock_v4\\alarm.ini", "w") as configfile:
            parser.write(configfile)

        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Oct, {int(futuro[2])}")

    elif futuro_mes[1] == "11":
        parser.set('alarms', 'alarm_one', f"Nov, {int(futuro[2])}_{hour_min_1.get()}")
        alarm_one = parser.get('alarms', 'alarm_one')

        with open("C:\Clock\Clock_v4\\alarm.ini", "w") as configfile:
            parser.write(configfile)

        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Nov, {int(futuro[2])}")

    elif futuro_mes[1] == "12":
        parser.set('alarms', 'alarm_one', f"Dec, {int(futuro[2])}_{hour_min_1.get()}")
        alarm_one = parser.get('alarms', 'alarm_one')

        with open("C:\Clock\Clock_v4\\alarm.ini", "w") as configfile:
            parser.write(configfile)

        month_day_1.delete(0, END)
        month_day_1.insert(0, f"Dec, {int(futuro[2])}")

    month_day_1.config(state=DISABLED)


def save():
    parser.set('alarms', 'alarm_one', f"{month_day_1.get()}_{hour_min_1.get()}")
    parser.set('alarms', 'alarm_two', f"{month_day_2.get()}_{hour_min_2.get()}")
    parser.set('alarms', 'alarm_three', f"{month_day_3.get()}_{hour_min_3.get()}")

    alarm_one = parser.get('alarms', 'alarm_one')
    alarm_two = parser.get('alarms', 'alarm_two')
    alarm_three = parser.get('alarms', 'alarm_three')

    if condition == True:
        parser.set('alarms', 'alarm_jump', f"{entry.get()}")
        alarm_jump = parser.get('alarms', 'alarm_jump')
        entry.delete(0, END)
        entry.insert(0, alarm_jump)
        cal_auto_win.destroy()

    with open("C:\Clock\Clock_v4\\alarm.ini", "w") as configfile:
        parser.write(configfile)


def def_clock():
    current_time = strftime('%H:%M:%S')
    current_date = strftime(" %a, %d %b, %Y ")

    clock.config(text=current_time)

    date_label.config(text=current_date)
    date_label.after(1, def_clock)


def save_switch():
    parser.set('alarms', 'condition1', f"{switch1}")
    parser.set('alarms', 'condition2', f"{switch2}")
    parser.set('alarms', 'condition3', f"{switch3}")

    condition1 = parser.get('alarms', 'condition1')
    condition2 = parser.get('alarms', 'condition2')
    condition3 = parser.get('alarms', 'condition3')

    with open("C:\Clock\Clock_v4\\alarm.ini", "w") as configfile:
        parser.write(configfile)

    window.destroy()


def switch_1():
    global switch1
    if switch1 == True:
        auto_button.config(image=off)
        switch1 = False

    elif switch1 == False:
        auto_button.config(image=on)
        switch1 = True

    if switch1 == True:
        check_button_1.config(image=enabled)
    elif switch1 == False:
        check_button_1.config(image=disabled)


def switch_2():
    global switch2
    if switch2:
        manual_1_button.config(image=off)
        switch2 = False

    elif not switch2:
        manual_1_button.config(image=on)
        switch2 = True

    if switch2 == True:
        check_button_2.config(image=enabled)
    elif switch2 == False:
        check_button_2.config(image=disabled)


def switch_3():
    global switch3
    if switch3:
        manual_2_button.config(image=off)
        switch3 = False

    elif not switch3:
        manual_2_button.config(image=on)
        switch3 = True

    if switch3 == True:
        check_button_3.config(image=enabled)
    elif switch3 == False:
        check_button_3.config(image=disabled)


def switcher():
    parser = ConfigParser()
    parser.read("C:\Clock\Clock_v4\\alarm.ini")

    condition1 = parser.get('alarms', 'condition1')
    condition2 = parser.get('alarms', 'condition2')
    condition3 = parser.get('alarms', 'condition3')

    global on, off, switch1, switch2, switch3, auto_button, manual_1_button, manual_2_button, window
    on = ImageTk.PhotoImage(Image.open("C:\Clock\Clock_v4\on.png"))
    off = ImageTk.PhotoImage(Image.open("C:\Clock\Clock_v4\off.png"))
    switch1 = None
    switch2 = None
    switch3 = None

    window = Toplevel()
    window.title("Switches")
    window.iconbitmap("C:/Clock/Clock_v4/enabled_disabled.ico")

    lframe = LabelFrame(window, text=" Enable/Disable Alarm ")
    lframe.pack(padx=20, pady=20)

    auto = Label(lframe, text="Auto Alarm:")
    auto_button = Button(lframe, image=on, command=switch_1)

    auto.grid(row=0, column=0, padx=10, pady=10)
    auto_button.grid(row=0, column=1, padx=10, pady=10)

    #############
    manual_1 = Label(lframe, text="Manual Alarm 1:")
    manual_1_button = Button(lframe, image=on, command=switch_2)

    manual_1.grid(row=1, column=0, padx=10, pady=10)
    manual_1_button.grid(row=1, column=1, padx=10, pady=10)

    #############
    manual_2 = Label(lframe, text="Manual Alarm 2:")
    manual_2_button = Button(lframe, image=on, command=switch_3)

    manual_2.grid(row=2, column=0, padx=10, pady=10)
    manual_2_button.grid(row=2, column=1, padx=10, pady=10)

    if condition1 == "True":
        auto_button.config(image=on)
        switch1 = True
    else:
        auto_button.config(image=off)
        switch1 = False

    if condition2 == "True":
        manual_1_button.config(image=on)
        switch2 = True
    else:
        manual_1_button.config(image=off)
        switch2 = False

    if condition3 == "True":
        manual_2_button.config(image=on)
        switch3 = True
    else:
        manual_2_button.config(image=off)
        switch3 = False

    save_button = Button(lframe, text="         Save Settings         ", command=save_switch)
    save_button.grid(row=3, column=0, padx=10, pady=10, columnspan=2)


def Alarm_Def():
    global futuro
    hj = date.today()
    futuro = date.fromordinal(hj.toordinal())
    futuro = str(futuro)
    futuro = futuro.split("-", 2)

    parser = ConfigParser()
    parser.read("C:\Clock\Clock_v4\\alarm.ini")

    alarm_one = parser.get('alarms', 'alarm_one')
    alarm_two = parser.get('alarms', 'alarm_two')
    alarm_three = parser.get('alarms', 'alarm_three')
    condition1 = parser.get('alarms', 'condition1')
    condition2 = parser.get('alarms', 'condition2')
    condition3 = parser.get('alarms', 'condition3')

    month_day_1.config(state=NORMAL)
    hour_min_1.config(state=NORMAL)

    alarm_time_1 = strftime(f"{month_day_1.get()}_{hour_min_1.get()}")
    alarm_time_1.replace("''", "")
    alarm_time_2 = alarm_two
    alarm_time_3 = alarm_three

    today_time = strftime("%b, %d_%H:%M")
    medicine_time = strftime(f"%b, {int(futuro[2])}_%H:%M")

    if alarm_time_1 == medicine_time and condition1 == "True":
        if platform.system() == 'Windows':
            pygame.mixer.music.load(f"C:\Clock\Clock_v4\Rooster.mp3")
            pygame.mixer.music.play(loops=10)
            response = messagebox.askyesno("rthur's Alarm-Clock", "Do you want to stop the sound?")
            if response == 1:
                pygame.mixer.music.stop()
                root.after(60000, Alarm_Def)
                save_futuro()

    elif alarm_time_2 == today_time and condition2 == "True":
        if platform.system() == 'Windows':
            pygame.mixer.music.load(f"C:\Clock\Clock_v4\Rooster.mp3")
            pygame.mixer.music.play(loops=10)
            response = messagebox.askyesno("rthur's Alarm-Clock", "Do you want to stop the sound?")
            if response == 1:
                pygame.mixer.music.stop()
                root.after(60000, Alarm_Def)

    elif alarm_time_3 == today_time and condition3 == "True":
        if platform.system() == 'Windows':
            pygame.mixer.music.load(f"C:\Clock\Clock_v4\Rooster.mp3")
            pygame.mixer.music.play(loops=10)
            response = messagebox.askyesno("rthur's Alarm-Clock", "Do you want to stop the sound?")
            if response == 1:
                pygame.mixer.music.stop()
                root.after(60000, Alarm_Def)

    else:
        root.after(1000, Alarm_Def)

    month_day_1.config(state=DISABLED)
    hour_min_1.config(state=DISABLED)


clock_frame = Frame(master_frame, bg="white")
clock_frame.grid(row=0, column=0, padx=10, pady=20)

# Make the widgets
clock = Label(clock_frame, text="", font=("digital-7", 65, "bold"), fg="#0000FF", bg="white")
date_label = Label(clock_frame, text="", font=("digital-7", 25, "italic"), fg="SteelBlue3", bg="white")
spacer = Label(clock_frame, text="                                                                                     "
                                 "             ", font=("digital-7", 5, "bold"), fg="#0000FF", bg="white")

clock.grid(row=0, column=0)
date_label.grid(row=1, column=0)
spacer.grid(row=2, column=0)

################

frame = Frame(master_frame, bg="white")
frame.grid(row=0, column=1, pady=5, padx=10)

frame_medicine_master = LabelFrame(frame, bg="light blue", fg="black", text="  Medicine Automatic Alarm  ")
frame_medicine_master.grid(row=0, column=0)

frame_medicine = LabelFrame(frame_medicine_master, bg="#0000FF", fg="white", text="  Month -  Day  -  Hour - Minute  ")
frame_medicine.grid(row=0, column=0)

frame_other_master = LabelFrame(frame, bg="light blue", text="  Manual Alarm  ")
frame_other_master.grid(row=1, column=0)

frame_other = LabelFrame(frame_other_master, bg="steelblue1", text="  Month -  Day  -  Hour - Minute  ")
frame_other.grid(row=1, column=0)

cancel_img = ImageTk.PhotoImage(Image.open("C:/Clock/Clock_v4/enabled_disabled.png"))
enabled = ImageTk.PhotoImage(Image.open("C:/Clock/Clock_v4/enabled.png"))
disabled = ImageTk.PhotoImage(Image.open("C:/Clock/Clock_v4/disabled.png"))

frame1 = Frame(frame_medicine, bg="#0000FE")
frame1.grid(row=0, column=0, pady=10, padx=10)

frame2 = Frame(frame_other, bg="steelblue1")
frame2.grid(row=1, column=0, pady=10, padx=10)

frame3 = Frame(frame_other, bg="steelblue1")
frame3.grid(row=2, column=0, pady=10, padx=10)

frame4 = Frame(frame_other, bg="steelblue1")
frame4.grid(row=3, column=0, padx=10)

frame5 = Frame(frame_medicine, bg="#0000FE")
frame5.grid(row=1, column=0, padx=10)

month_day_1 = Entry(frame1, font=("Arial", 12), bd=2, width=6)
hour_min_1 = Entry(frame1, font=("Arial", 12), bd=2, width=6)
check_button_1 = Label(frame1, bg="#0000FE")

if condition1 == "True":
    check_button_1.config(image=enabled)
elif condition1 == "False":
    check_button_1.config(image=disabled)

check_button_1.grid(row=0, column=2, padx=5)
month_day_1.grid(row=0, column=0)
hour_min_1.grid(row=0, column=1)

month_day_2 = Entry(frame2, font=("Arial", 12), bd=2, width=6)
hour_min_2 = Entry(frame2, font=("Arial", 12), bd=2, width=6)
check_button_2 = Label(frame2, bg="steelblue1")

if condition2 == "True":
    check_button_2.config(image=enabled)
elif condition2 == "False":
    check_button_2.config(image=disabled)

check_button_2.grid(row=1, column=3, padx=5)
month_day_2.grid(row=1, column=0)
hour_min_2.grid(row=1, column=2)

month_day_3 = Entry(frame3, font=("Arial", 12), bd=2, width=6)
hour_min_3 = Entry(frame3, font=("Arial", 12), bd=2, width=6)
check_button_3 = Label(frame3, bg="steelblue1")

if condition3 == "True":
    check_button_3.config(image=enabled)
elif condition3 == "False":
    check_button_3.config(image=disabled)

check_button_3.grid(row=2, column=3, padx=5)
month_day_3.grid(row=2, column=0)
hour_min_3.grid(row=2, column=2)

calendar_img = ImageTk.PhotoImage(Image.open("C:\Clock\Clock_v4\calendar.png"))
clock_img = ImageTk.PhotoImage(Image.open("C:\Clock\Clock_v4\clock.png"))
cal_edit_img = ImageTk.PhotoImage(Image.open("C:\Clock\Clock_v4\cal_manual.png"))
delay = ImageTk.PhotoImage(Image.open("C:\\Clock\\Clock_v4\\arrow.png"))

button_date = Button(frame4, image=calendar_img, command=calendar_def, bg="steelblue1",
                     activebackground="dark blue", fg="dark blue", activeforeground="white")
button_date.grid(row=0, column=0, pady=5, padx=5)

button_time = Button(frame4, image=clock_img, command=clock_def, bg="steelblue1",
                     activebackground="dark blue", fg="dark blue", activeforeground="white")
button_time.grid(row=0, column=1, pady=5, padx=5)

enabled_btn = Button(frame4, image=cancel_img, command=switcher, bg="steelblue1",
                     activebackground="dark blue", fg="dark blue", activeforeground="white")
enabled_btn.grid(row=0, column=2, padx=5)

##############
button_auto_plus = Button(frame5, image=cal_edit_img, command=calendar_auto_home_def, bg="#0000FE",
                          activebackground="dark blue", fg="dark blue", activeforeground="white")
button_auto_plus.grid(row=1, column=0, pady=5, padx=5)

button_auto_cal = Button(frame5, image=calendar_img, command=cal_auto_def, bg="#0000FE",
                         activebackground="dark blue", fg="dark blue", activeforeground="white")
button_auto_cal.grid(row=1, column=1, pady=5, padx=5)

button_auto_clock = Button(frame5, image=clock_img, command=clock_auto_def, bg="#0000FE",
                           activebackground="dark blue", fg="dark blue", activeforeground="white")
button_auto_clock.grid(row=1, column=2, pady=5, padx=5)

button_delay = Button(frame5, image=delay, command=save_futuro, bg="#0000FE",
                           activebackground="dark blue", fg="dark blue", activeforeground="white")
button_delay.grid(row=1, column=3, pady=5, padx=5)

global futuro_mes
hj = date.today()

futuro_mes = f"{date.fromordinal(hj.toordinal())}"
futuro_mes = str(futuro_mes)
futuro_mes = futuro_mes.split("-", 2)

month_day_1.delete(0, END)
hour_min_1.delete(0, END)

month_day_2.delete(0, END)
hour_min_2.delete(0, END)

month_day_3.delete(0, END)
hour_min_3.delete(0, END)

alarm_one_day_hour = alarm_one.split("_")

alarm_one_day = alarm_one_day_hour[0]
alarm_one_day = alarm_one_day.split(",")

alarm_one_hour = alarm_one_day_hour[1]
alarm_one_hour = alarm_one_hour.split(":")

alarm_one_min = alarm_one.split(":")
alarm_one_month = alarm_one.split(",")

if futuro_mes[1] == "01":
    month_day_1.delete(0, END)
    month_day_1.insert(0, "Jan")

elif futuro_mes[1] == "02":
    month_day_1.delete(0, END)
    month_day_1.insert(0, "Feb")

elif futuro_mes[1] == "03":
    month_day_1.delete(0, END)
    month_day_1.insert(0, "Mar")

elif futuro_mes[1] == "04":
    month_day_1.delete(0, END)
    month_day_1.insert(0, "Apr")

elif futuro_mes[1] == "05":
    month_day_1.delete(0, END)
    month_day_1.insert(0, "May")

elif futuro_mes[1] == "06":
    month_day_1.delete(0, END)
    month_day_1.insert(0, "Jun")

elif futuro_mes[1] == "07":
    month_day_1.delete(0, END)
    month_day_1.insert(0, "Jul")

elif futuro_mes[1] == "08":
    month_day_1.delete(0, END)
    month_day_1.insert(0, "Aug")

elif futuro_mes[1] == "09":
    month_day_1.delete(0, END)
    month_day_1.insert(0, "Sep")

elif futuro_mes[1] == "10":
    month_day_1.delete(0, END)
    month_day_1.insert(0, "Oct")

elif futuro_mes[1] == "11":
    month_day_1.delete(0, END)
    month_day_1.insert(0, "Nov")

elif futuro_mes[1] == "12":
    month_day_1.delete(0, END)
    month_day_1.insert(0, "Dec")

month_day_1.insert(END, f",{alarm_one_day[1]}")
hour_min_1.insert(0, f"{alarm_one_hour[0]}:{alarm_one_min[1]}")

month_day_1.config(state=DISABLED)
hour_min_1.config(state=DISABLED)

#############
alarm_two_day_hour = alarm_two.split("_")

alarm_two_day = alarm_two_day_hour[0]
alarm_two_day = alarm_two_day.split(",")

alarm_two_hour = alarm_two_day_hour[1]
alarm_two_hour = alarm_two_hour.split(":")

alarm_two_min = alarm_two.split(":")
alarm_two_month = alarm_two.split(",")

month_day_2.insert(0, f"{alarm_two_month[0]},{alarm_two_day[1]}")
hour_min_2.insert(0, f"{alarm_two_hour[0]}:{alarm_two_min[1]}")

#############
alarm_three_day_hour = alarm_three.split("_")

alarm_three_day = alarm_three_day_hour[0]
alarm_three_day = alarm_three_day.split(",")

alarm_three_hour = alarm_three_day_hour[1]
alarm_three_hour = alarm_three_hour.split(":")

alarm_three_min = alarm_three.split(":")
alarm_three_month = alarm_three.split(",")

month_day_3.insert(0, f"{alarm_three_month[0]},{alarm_three_day[1]}")
hour_min_3.insert(0, f"{alarm_three_hour[0]}:{alarm_three_min[1]}")

month_day_2.config(state=DISABLED)
hour_min_2.config(state=DISABLED)

month_day_3.config(state=DISABLED)
hour_min_3.config(state=DISABLED)

Alarm_Def()
def_clock()

root.mainloop()
