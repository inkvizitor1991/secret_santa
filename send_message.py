from django.core.mail import send_mail
from django.conf import settings





def send_message_to_mail(recipient_email):
    send_mail(
        'Жеребьевка в игре "Тайный Санта"',
        'hello!!!!',
        settings.EMAIL_HOST_USER,
        [recipient_email],
        fail_silently=False,
    )





