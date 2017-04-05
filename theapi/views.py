# coding=utf-8
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from theapi.models import HistorialSMS
from theapi.twilio_api import twilio_send_sms


def build_msg(error, message):
    content = {
        'error': error,
        'message': message,
    }
    return Response(content)


def build_error(message):
    return build_msg(1, message)


def build_good(message):
    return build_msg(0, message)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def send_sms(request):
    if 'number' in request.data and 'code' in request.data and 'text' in request.data:
        userphone = request.data['code'] + request.data['number']
        if not userphone.startswith('+'):
            userphone = '+' + userphone
        text = request.POST['text']
        if twilio_send_sms(to=userphone, body=text):
            HistorialSMS(destinatario=userphone, mensaje=text,
                         user=request.user).save()
            return build_good("Mensaje enviado con éxito")
        else:
            return build_good("Ocurrió un error al enviar el mensaje")
    else:
        return build_error('Debe proveer todos los datos para poder ejecutar esta acción')
