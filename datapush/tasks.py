from celery import shared_task
import requests
from django.utils.timezone import now
from logs.models import Log
from destinations.models import Destination



@shared_task
def send_data_to_destination(log_id, destination_id):
    try:
        log = Log.objects.get(id=log_id)
        destination = Destination.objects.get(id=destination_id)

        # Send data to destination
        response = requests.request(
            method=destination.http_method,
            url=destination.url,
            headers=destination.headers,
            json=log.received_data
        )

        # Update log based on response
        log.status = "success" if response.status_code in [200, 201, 202] else "failed"
        log.processed_timestamp = now()
        log.save()

    except Exception as e:
        log.status = "failed"
        log.processed_timestamp = now()
        log.save()