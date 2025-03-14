from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils.decorators import method_decorator
from django.views import View
import json
import uuid
from datapush.tasks import send_data_to_destination

from users.models import User
from logs.models import Log
from destinations.models import Destination 


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class DataHandlerView(View):
    def post(self, request, *args, **kwargs):
        # Extract headers
        secret_token = request.headers.get("CL-X-TOKEN")
        event_id = request.headers.get("CL-X-EVENT-ID", str(uuid.uuid4()))  # Generate if not provided

        # Validate headers
        if not secret_token:
            return JsonResponse({"error": "Missing CL-X-TOKEN header"}, status=400)

        # Identify the account
        try:
            account = Account.objects.get(app_secret_token=secret_token)
        except Account.DoesNotExist:
            return JsonResponse({"error": "Invalid CL-X-TOKEN"}, status=403)

        # Parse JSON data
        try:
            received_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

        # Fetch destinations
        destinations = Destination.objects.filter(account=account)
        if not destinations.exists():
            return JsonResponse({"error": "No destinations configured for this account"}, status=404)

        # Save log entry (initial status: 'pending')
        log = Log.objects.create(
            event_id=event_id,
            account=account,
            received_timestamp=timezone.now(),
            received_data=received_data,
            status="pending"
        )

        # Trigger async task to send data
        for destination in destinations:
            send_data_to_destination.delay(log.id, destination.id)  # Pass log & destination IDs

        return JsonResponse({"message": "Data received and processing started", "event_id": event_id}, status=202)

