from __future__ import absolute_import, unicode_literals
from celery import task
from dashboard.functions import *

@task()
def task_updateDashboard():
    updateSocialsDashboard()

@task()
def task_createStatsLog():
    updateSocialsDashboard()
    createStatsLog();
