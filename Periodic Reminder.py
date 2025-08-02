from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

def job():
    print(f"Reminder at {datetime.datetime.now()} - Take a break!")

sched = BlockingScheduler()
sched.add_job(job, "interval", minutes=30)
sched.start()
