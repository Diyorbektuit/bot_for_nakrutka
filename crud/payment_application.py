from apps.models import PaymentApplication
from asgiref.sync import sync_to_async
from django.db.models import Sum
from apps.models import User

@sync_to_async()
def create_payment_application(user, receipt_path):
    application = PaymentApplication.objects.create(
        user=user,
        receipt=receipt_path,
    )
    return application

@sync_to_async()
def all_payment_amount_application(user):
    all_amount = user.payment_applications.filter(
        status="approved"
    ).aggregate(
        all_amount=Sum("amount")
    )['all_amount']
    if all_amount is None:
        all_amount = 0
    return all_amount

@sync_to_async()
def count_payment_approved_applications(user):
    count = user.payment_applications.filter(
        status="approved"
    ).count()

    return count

@sync_to_async()
def moderation_applications_for_admin():
    all_applications = PaymentApplication.objects.filter(
        status="moderation"
    )

    result = []
    count = 1
    for application in all_applications:
        data = {
            'number': count,
            'id': application.id,
            'user': application.user.phone,
            'receipt': application.receipt,
        }
        count += 1
        result.append(data)

    all_result = {
        'all_count': count,
        'data': result
    }
    return all_result

@sync_to_async()
def get_application(number):
    application = PaymentApplication.objects.get(
        id=number
    )

    if application.status == "moderation":
        return {
            "user": application.user.phone,
            "receipt": application.receipt,
        }
    else:
        return False


@sync_to_async()
def add_point_user_db(amount, user_phone):
    user = User.objects.get(phone=user_phone)
    user.wallet += amount
    user.save()
    return user


