from celery import shared_task
import logging

logger = logging.getLogger('django')


@shared_task
def create_task(automation_id, **kwargs):
    # automation = get_automation(automation_id)
    # automation.main(**kwargs)
    logger.info(f'Running automation {automation_id} with arguments: {kwargs}')
    return f'Running automation {automation_id} with arguments: {kwargs}'
