from celery import shared_task

@shared_task
def notify_large_transaction(amount):
    if amount > 1000:
        print(f"⚠️ Transaction over 1000 BGN: {amount}")