from datetime import timedelta

from celery import Celery

app = Celery("spider", broker="redis://127.0.0.1:6379/1", backend="redis://127.0.0.1:6379/2",
             include=["celery_task.task_execute_spider", ])

# 时区
app.conf.timezone = "Asia/Shanghai"
# 是否使用UTC
app.conf.enable_utc = False

app.conf.beat_schedule = {
    "add-every-10-seconds": {
        "task": "celery_task.task_execute_spider.test_celery",
        "schedule": timedelta(seconds=300),
    }
}
