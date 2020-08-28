from celery_task.celery import app
from master_task import execute_crawler


@app.task
def test_celery():
    ret = execute_crawler()
    return "test_celery任务结果:%s" % ret
