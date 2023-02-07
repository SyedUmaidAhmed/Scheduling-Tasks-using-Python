# pip install schedule -q

import schedule
import time

def task1():
print("Running task 1...")

def task2():
print("Running task 2...")

def task3():
print("Running task 3...")

# Schedule task 1 to run every hour
schedule.every(1).hours.do(task1)

# Schedule task 2 to run every day at 9am
schedule.every().day.at("09:00").do(task2)

# Schedule task 3 to run every Monday at 9pm
schedule.every().monday.at("21:00").do(task3)

while True:
    schedule.run_pending( )
    time.sleep(1)
