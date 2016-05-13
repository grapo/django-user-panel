import functools

from django.conf import settings
from django.http import HttpResponseForbidden


def debug_required(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        if not getattr(settings, 'USER_PANEL_DEBUG', settings.DEBUG):
            return HttpResponseForbidden()
        return fn(*args, **kwargs)
    return wrapper
