from django.shortcuts import render
from django.http import HttpResponse
from celery_progress.backend import ProgressRecorder
from celery import shared_task
from time import sleep
# Create your views here.

def index(request):
    task = go_to_sleep.delay(1)
    x= task
    print(x)
    return render(request, 'testcelery.html', {'task_id' : task.task_id,'x':x})

@shared_task(bind=True)
def go_to_sleep(self, duration):
    progress_recorder = ProgressRecorder(self)
    sum = 0
    for i in range(100):
        sum = sum + plus()
        sleep(duration)
        progress_recorder.set_progress(i + 1, 100, f'On iteration {i}')
    return 'Done'
def plus(a,b):
    return a+b