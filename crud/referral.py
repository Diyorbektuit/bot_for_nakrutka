from asgiref.sync import sync_to_async
from apps.models import Referral
from dp import REFERRAL_POINT

@sync_to_async()
def user_referrals(user_id):
    referrals = Referral.objects.filter(
        user__user_id=user_id
    ).order_by('-created_at')
    referrals_count = referrals.count()

    referrals = referrals[:10]
    referral_users = []
    for referral in referrals:
        referral_users.append(f"{referral.offered_user.first_name} {referral.offered_user.last_name}")

    return {
        'referrals_count': referrals_count,
        'referral_users': referral_users
    }

@sync_to_async()
def user_referrals_count(user):
    count = user.referrals.all().count()
    return count


@sync_to_async()
def create_referral(user, offered_user):
    return Referral.objects.create(
        user=user,
        offered_user=offered_user,
        amount=REFERRAL_POINT
    )

@sync_to_async()
def get_referral(offered_user):
    return Referral.objects.get(offered_user=offered_user)


@sync_to_async()
def get_all_referrals():
    all_referrals = Referral.objects.all()

    data = {
        "count": all_referrals.count(),
    }

    return data
