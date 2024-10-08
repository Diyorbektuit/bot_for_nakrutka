from django.contrib import admin
from .models import User, Referral, PaymentApplication
# Register your models here.

@admin.register(User)
class UserModel(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'wallet', 'username', 'phone',
                    'first_name', 'last_name', 'role', 'is_referred', 'is_active')
    list_filter = ('role', )


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'offered_user', 'created_at')
    list_filter = ('user',)


@admin.register(PaymentApplication)
class PaymentApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'status')
    list_filter = ('user', 'status')
