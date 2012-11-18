import django

def require_secret_handshake(fn):
    """
    Decorator to make a view only accept particular request with secret param.  Usage::

        @require_secret_handshake
        def my_view(request):
            # I can assume now that only requests that have valid secret param made it
            # ...

    """
    def decorator(func):
        @wraps(func, assigned=available_attrs(func))
        def inner(request, *args, **kwargs):
            secret = request.GET.get('secret', '')
            signer = django.core.signing.TimestampSigner()
            try:
                signer.unsign(secret, max_age=10)
            except django.core.signing.SignatureExpired:
                return HttpResponseNotAllowed("Tsk tsk.")
            return func(request, *args, **kwargs)
        return inner
    return decorator

