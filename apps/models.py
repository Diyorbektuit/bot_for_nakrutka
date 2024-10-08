from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, Group, Permission

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CustomUserManager(UserManager):
    def _create_user(self, phone=None, password=None, **extra_fields):
        user = self.model(phone=phone,  **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone=phone, password=password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("user_id")


        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(
            username=username, password=password, **extra_fields
        )

class User(AbstractUser, BaseModel):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    last_name = models.CharField(max_length=150, null=True, blank=True)
    role = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default="user")
    phone = models.CharField(max_length=150, unique=True, null=True, blank=True)
    user_id = models.CharField(max_length=25, unique=True)
    wallet = models.IntegerField(default=0)
    offers_count = models.IntegerField(default=0)
    is_referred = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name="common_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="common_user_permissions", blank=True)

    objects = CustomUserManager()

    class Meta:
        db_table = "common_user"
        verbose_name = "User"
        verbose_name_plural = "Users"


class Referral(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="referrals")
    offered_user = models.OneToOneField(User, on_delete=models.PROTECT, related_name="referral")
    amount = models.IntegerField()


class PaymentApplication(BaseModel):
    STATUS_CHOICES = (
        ('moderation', 'Moderation'),
        ('approved', 'Approved'),
        ('canceled', "Canceled")
    )
    amount = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="payment_applications")
    status = models.CharField(max_length=123, choices=STATUS_CHOICES, default="moderation")
    receipt = models.ImageField(upload_to='media/receipt')
    reason = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.user.phone} -- {self.amount}"



