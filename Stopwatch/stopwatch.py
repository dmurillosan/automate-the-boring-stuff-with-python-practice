# Stopwatch project to practice concepts learned in 'Automate The Boring Things With Python'
# Written by David Murillo Santiago on Feb 6, 2026

#Start of Program
import datetime
import os
import sys

# init variable time_started, used to control stopwatch start and stop events
stopwatch_started = False

# track start stopwatch events
def start_time():
    dt_start = datetime.datetime.now()
    time_history_log(f"Stopwatch started on: {dt_start}")
    return dt_start

# track stop stopwatch events
def stop_time():
    dt_stop = datetime.datetime.now()
    time_history_log(f"Stopwatch stopped on: {dt_stop}")
    return dt_stop

# remove the microseconds from timedelta - inspired by sangorys from stackoverflow
# thank you sangorys: https://stackoverflow.com/questions/18470627/remove-the-microseconds-from-a-timedelta-object
def chop_microseconds(time):
    clean_time = str(time).split(".")[0]
    return clean_time

# calculate the time passed between start & stop and return in HH:MM:SS format
def elapsed_time(dt_start, dt_stop):
    time_elapsed = dt_stop - dt_start
    time_elapsed = chop_microseconds(time_elapsed)
    time_history_log(f"Total run time was: {time_elapsed}\n")
    return time_elapsed

# print underscores to separate console output
def spaces():
    for i in range(1):
        print("\n__________________________________________________")

# track user action - start stopwatch
def usr_action_start():
    global stopwatch_started
    print('\nPress "ENTER" To Start Stopwatch')
    input("> ")
    stopwatch_started = True

# track user action - stop stopwatch
def usr_action_stop():
    global stopwatch_started
    print('\nPress "ENTER" To Stop Stopwatch')
    input("> ")
    stopwatch_started = False

# logging function tracking program actions in a text file in the same directory
# will implement logging.basicConfig(level=logging.DEBUG) in future projects
def time_history_log(dt_event):
    log_path = "time_history_log.txt"
    with open(log_path, "a") as event:
        new_line = '\n' if os.path.getsize(log_path) > 0 else ''
        event.write(f"{new_line}{dt_event}")

# main function - calls the stopwatch event functions
def main_function():
    dt_start = None
    dt_stop = None
    while not stopwatch_started:
        spaces()
        usr_action_start()
        dt_start = start_time()
        spaces()
    else:
        usr_action_stop()
        dt_stop = stop_time()
    if dt_start and dt_stop:
        total_time = elapsed_time(dt_start, dt_stop)
        spaces()
        print("\n\nThe stopwatch ran for " + '[' + str(total_time) + ']')

# run main function continuously until program is manually closed by the user
while True:
    try:
        main_function()
    except KeyboardInterrupt:
        time_history_log('')
        sys.exit()
