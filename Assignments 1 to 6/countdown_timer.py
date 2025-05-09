import time

def countdown_timer(seconds:int):

    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

seconds = int(input("Enter the time in seconds: "))

countdown_timer(seconds)