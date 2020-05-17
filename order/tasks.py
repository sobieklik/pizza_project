from celery import task
from django.core.mail import send_mail
from .models import Order
from smsapi.client import SmsApiPlClient
import logging
logger = logging.getLogger("mylogger")
from django.conf import settings

@task
def send_sms(order_id):
    """
    Task to send sms notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    token = settings.SECRET_SMS_TOKEN

    #return logger.info('Numer zamowienia: {}'.format(token))    #  Only for test. If you wont send sms you should comment that line
    
    client = SmsApiPlClient(access_token=token)

    try:
        send_results = client.sms.send(to=str(order.phone), message=u"Czesc, to my restautacja XYZ. Twoje zamowienie o numerze {} zostalo przyjete.\
        Czekaj cierpliwie, niebawem ktos przybedzie z Twoim jedzeniem. Do zaplaty {} zl".format(order.id, order.total_cost()))
    except SmsApiException as e:
        print(e.message, e.code)
        logger.info(e.message)

    for result in send_results:
        print(result.id, result.points, result.error)
    
    return send_results
    