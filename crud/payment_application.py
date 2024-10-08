from apps.models import PaymentApplication
from asgiref.sync import sync_to_async



@sync_to_async()
def create_application(user, receipt):
    application = PaymentApplication.objects.create(
        user=user,
        receipt=receipt,
    )

