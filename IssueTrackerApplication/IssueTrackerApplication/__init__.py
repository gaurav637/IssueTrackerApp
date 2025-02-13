# Comment out or remove the Zango celery import
from zango.config.celery import app as celery_app


__all__ = ["celery_app"]

default_app_config = 'IssueTrackerApplication.apps.IssueTrackerConfig'
