from operator import sub
from django.core.mail import send_mail
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from apps import enquiries

from real_estate.settings.development import DEFAULT_FROM_EMAIL

from .models import Enquirty


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def send_enquirty_email(request):
    data = request.data

    try:
        subject = data["subject"]
        name = data["name"]
        email = data["email"]
        message = data["message"]
        from_email = data["email"]
        recipient_list = [DEFAULT_FROM_EMAIL]

        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        enquirty = Enquirty(name=name, email=email, subject=subject, message=message)
        enquirty.save()

        return Response({"sucess": "Your Enquiry was successfully submitted"})

    except:
        return Response({"fail": "Enquiry was not sent. Please try again"})
