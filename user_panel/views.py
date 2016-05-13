from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.contrib.auth import (
    logout as auth_logout, login as auth_login,
    get_user_model, _get_backends)
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import UserForm
from .decorators import debug_required

User = get_user_model()


@debug_required
@csrf_exempt
@require_POST
def login_credentials(request):
    form = UserForm(request.POST)

    if not form.is_valid():
        return HttpResponseBadRequest()

    auth_login(request, form.get_user())
    return HttpResponseRedirect(request.POST.get('next', '/'))


@debug_required
@csrf_exempt
@require_POST
def login_pk(request, pk):
    user = get_object_or_404(User, pk=pk)
    backend, backend_path = _get_backends(return_tuples=True)[0]
    user.backend = backend_path

    auth_login(request, user)

    return HttpResponseRedirect(request.POST.get('next', '/'))


@debug_required
@csrf_exempt
@require_POST
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(request.POST.get('next', '/'))
