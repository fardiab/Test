from celery import shared_task

from time import sleep


@shared_task(bind=True)
def sleepy(self, duration):
    sleep(duration)
    return "Done"
    