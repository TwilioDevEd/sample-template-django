import json
import traceback

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from sample_site.settings.env import env
from twilio.rest import Client


def index(request):
    context = {'title': 'Sample Template'}
    return render(request, 'sample_app/index.html', context)


def example(request):
    return JsonResponse({'example': True})


@csrf_exempt
def send_sms(request):
    body = json.loads(request.body)
    try:
        client = Client(env('TWILIO_ACCOUNT_SID'), env('TWILIO_AUTH_TOKEN'))
        message = client.messages.create(
            body=body['body'], from_=env('TWILIO_PHONE_NUMBER'), to=body['to']
        )
        return JsonResponse(
            {
                'status': 'success',
                'message': f"SMS sent to {body['to']}. Message SID: {message.sid}",
            }
        )
    except Exception:
        traceback.print_exc()
        return JsonResponse(
            {
                'status': 'error',
                'message': 'Failed to send SMS. Check server logs for more details.',
            },
            status=500,
        )
