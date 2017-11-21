# -*- coding: utf-8 -*-
import logging
import json

from app.models import SecureInfo
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect

logger = logging.getLogger('root')


def home(request):
    user = getattr(request, 'user', None)
    if user and user.username == '12345':
        return JsonResponse({'result': True, 'message': 'success', 'code': 0, 'data': '1234'})
    return redirect('/api/get_info/')


def get_info(request):
    logger.info(request)
    return JsonResponse({'result': True, 'message': 'success', 'code': 0, 'data': 0})


def update_info(request):
    try:
        request_body = json.loads(request.body)
    except ValueError:
        request_body = {}

    app_code = request.POST.get('app_code', request_body.get('app_code', ''))
    secure_key = request.POST.get('secure_key', request_body.get('secure_key', ''))
    sec, created = SecureInfo.objects.get_or_create(app_code=app_code, secure_key=secure_key)
    return JsonResponse({'result': True, 'message': 'success', 'code': 0, 'data': sec.app_code})
