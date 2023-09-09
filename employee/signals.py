from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.signals import *
from django.dispatch import receiver

from .models import Employee


@receiver(social_account_updated, sender=SocialAccount)
def associate_sociallogin_to_employee(request, **kwargs):
    sociallogin = kwargs.get('sociallogin', None)
    if sociallogin:
        employee, created = Employee.objects.get_or_create(email=sociallogin.user.email)
        employee.user = sociallogin.user

        if created:
            employee.email = sociallogin.user.email
            employee.name_sei = sociallogin.user.last_name
            employee.name_mei = sociallogin.user.first_name

        employee.save()

social_account_added.connect(associate_sociallogin_to_employee)
social_account_updated.connect(associate_sociallogin_to_employee)