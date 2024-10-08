from asgiref.sync import sync_to_async
from django.utils import timezone
from apps.models import User


@sync_to_async
def create_user_in_db(phone, password, **extra_fields):
    return User.objects.create_user(phone=phone, password=password, **extra_fields)


@sync_to_async()
def have_user_db(user_id):
    user = User.objects.filter(
        user_id=user_id,
        is_active=True
    )
    if user.exists():
        return True
    else:
        return False

@sync_to_async()
def get_user_db(user_id):
    try:
        return User.objects.get(user_id=user_id)
    except User.DoesNotExist:
        return None

@sync_to_async()
def update_user_db(user:User, phone=None, is_active=None, is_referred=None):
    if phone:
        user.phone = phone
    if is_active:
        user.is_active = is_active
    if is_referred:
        user.is_referred = is_referred
    user.save()
    return user

@sync_to_async()
def add_point(user:User, point):
    user.wallet += point
    user.save()
    return user

@sync_to_async()
def get_users_count():
    today = timezone.now()
    a_week_ago = today - timezone.timedelta(days=7)
    a_month_ago = today - timezone.timedelta(days=30)

    users = User.objects.all()
    all_users_count = users.count()
    last_week_count = users.filter(
        created_at__gte=a_week_ago
    ).count()
    last_month_count = users.filter(
        created_at__gte=a_month_ago
    ).count()

    data = {
        'all_users_count': all_users_count,
        'last_week_count': last_week_count,
        'last_month_count': last_month_count
    }

    return data