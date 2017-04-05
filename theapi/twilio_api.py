from twilio.rest import TwilioRestClient

from random import choice

from theapi.models import CuentaTwilio, Telefono

import logging
logger = logging.getLogger()


def twilio_send_sms(to, body):
    try:
        logger.debug('mandando sms '+to)
        cuenta = CuentaTwilio.objects.all()
        if len(cuenta) > 0:
            cuenta = cuenta[0]
        else:
            return False

        client = TwilioRestClient(cuenta.account, cuenta.token)

        message = client.messages.create(to=to,
                                         from_=choice(Telefono.objects.filter(cuenta=cuenta)).telefono,
                                         body=body)
        logger.debug(message)
        return message.sid
    except Exception as e:
        logger.error(e)
        return False
