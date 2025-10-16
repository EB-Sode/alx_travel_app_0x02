# listings/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from .models import Payment

@shared_task
def send_payment_confirmation_email(payment_id):
    try:
        payment = Payment.objects.get(id=payment_id)
        subject = "Booking Payment Confirmation"
        message = f"Hello {payment.user.first_name},\n\nYour payment of {payment.amount} {payment.currency} for booking has been successfully processed.\n\nThank you!"
        recipient = [payment.user.email]
        send_mail(subject, message, "noreply@yourapp.com", recipient)
    except Payment.DoesNotExist:
        pass
