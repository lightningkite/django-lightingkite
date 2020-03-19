from .settings import STRIPE_API_KEY, STRIPE_API_VERSION


_stripe = None
default_app_config = "django_lightningkite.stripe.apps.StripeConfig"


# stripe client singleton
def get_stripe_client():
    global _stripe

    if _stripe is None:
        import stripe as Stripe
        Stripe.api_key = STRIPE_API_KEY
        if STRIPE_API_VERSION is not None:
            Stripe.api_version = STRIPE_API_VERSION
        _stripe = Stripe
    return _stripe


stripe = get_stripe_client()
