import json

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import stripe
from .settings import STRIPE_WEBHOOK_SECRET
from .signals import stripe_webhook


@csrf_exempt
def StripeView(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET, tolerance=9999999
        )
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)

    stripe_webhook.send(sender=None, event=event, request=request)

    if settings.DEBUG:
        parsed = json.loads(request.body)
        print('----->stripe webhook event<-----')
        print(sig_header)
        print(json.dumps(parsed, indent=4))
    return HttpResponse(status=200)
