from __future__ import absolute_import, unicode_literals
import os
import logging
import threading

import wsgiserver

from django.conf import settings
from celery import Celery
from celery.schedules import crontab
from prometheus_client import multiprocess
from prometheus_client import generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST, Gauge, Counter

from . import project_env


logger = logging.getLogger("tasks")


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# APP_NAME = BASE_DIR.rsplit("/", 1)[-1]

# ENV_CHOICES = ("DEV", "FAT", "PRO")
# ENV = os.environ.get("ENV")
# settings = "settings_pro" if ENV == "PRO" else "settings"
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{APP_NAME}.{settings}')
# os.environ["DJANGO_SETTINGS_MODULE"] = settings


# project_env.set_django_settings_env()
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AppSsvBackend.settings')
settings_name = project_env.get_django_settings()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_name)

app = Celery(project_env.APP_NAME)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'sync_account': {
        'task': 'ccc.tasks.sync_account',
        'schedule': 60 * 10
    },
    'sync_all_nft': {
        'task': 'ccc.tasks.sync_all_nft',
        'schedule': 60 * 10
    },
    'sync_account_icp_balance': {
        'task': 'ccc.tasks.sync_account_icp_balance',
        'schedule': 60 * 60 * 3
    },
    'sync_nft_transaction_record': {
        'task': 'ccc.tasks.sync_nft_transaction_record',
        'schedule': 60 * 60 * 3
    },
    'sync_wicp_op_record': {
        'task': 'ccc.tasks.sync_wicp_op_record',
        'schedule': 60 * 60 * 3
    },
    'sync_wicp_others': {
        'task': 'ccc.tasks.sync_wicp_others',
        'schedule': 60 * 60 * 1
    },
    'sync_icp_transaction': {
        'task': 'ccc.tasks.sync_icp_transaction',
        'schedule': 60 * 60 * 2
    },
    'sync_other_nft': {
        'task': 'ccc.tasks.sync_other_nft',
        'schedule': 60 * 60 * 2
    }
}
app.conf.enable_utc = False
app.conf.timezone = "Asia/Shanghai"


# def metrics(environ, start_response):
#     registry = CollectorRegistry()
#     multiprocess.MultiProcessCollector(registry)
#     data = generate_latest(registry)
#     # return Response(data, mimetype=CONTENT_TYPE_LATEST)
#
#     status = '200 OK'
#     response_headers = [('Content-type', 'text/html; charset=utf-8')]
#     start_response(status, response_headers)
#     return [data]
#
#
# def start_server():
#     server = wsgiserver.WSGIServer(metrics, host="0.0.0.0", port=settings.CELERY_PROMETHEUS_PORT)
#     server.start()
#
#
# class PrometheusServer(threading.Thread):
#
#     def metrics(self, environ, start_response):
#         registry = CollectorRegistry()
#         multiprocess.MultiProcessCollector(registry)
#         data = generate_latest(registry)
#         # return Response(data, mimetype=CONTENT_TYPE_LATEST)
#
#         status = '200 OK'
#         response_headers = [('Content-type', CONTENT_TYPE_LATEST), ('Content-Length', str(len(data)))]
#         start_response(status, response_headers)
#         return [data]
#
#     def run(self) -> None:
#         server = wsgiserver.WSGIServer(self.metrics, host="0.0.0.0", port=settings.CELERY_PROMETHEUS_PORT)
#         server.start()
#
#
# IS_CELERY = os.getenv("IS_CELERY")
# print(f"IS_CELERY: {IS_CELERY}")
# logger.info(f"IS_CELERY: {IS_CELERY}")
#
# if os.getenv("IS_CELERY"):
#     prometheus_server = PrometheusServer()
#     prometheus_server.start()
#     print("prometheus_server start completed")


# @celery.task(celery.Strategy=shutdown_after_strategy)
# def shutdown_after():
#     print('will shutdown after this')