import json
import logging

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from twilio.base.exceptions import TwilioException
from twilio.rest import Client

logger = logging.getLogger(__name__)


def index(request):
    context = {'title': 'Sample Template'}
    return render(request, 'sample_app/index.html', context)


def example(request):
    return JsonResponse({'example': True})


@csrf_exempt
def send_sms(request):
    body = json.loads(request.body)
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=body['body'], from_=settings.TWILIO_PHONE_NUMBER, to=body['to']
        )
    except TwilioException:
        logger.exception('Error sending message')
        return JsonResponse(
            {
                'status': 'error',
                'message': 'Failed to send SMS. Check server logs for more details.',
            },
            status=500,
        )
    else:
        return JsonResponse(
            {
                'status': 'success',
                'message': f"SMS sent to {body['to']}. Message SID: {message.sid}",
            }
        )
