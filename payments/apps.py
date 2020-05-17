from django.apps import AppConfig

class PaymentsConfig(AppConfig):
    name = 'payments'
    verbose_name = 'Payments'

    def ready(self):
        """ After load payments import signal """
        import payments.signals
