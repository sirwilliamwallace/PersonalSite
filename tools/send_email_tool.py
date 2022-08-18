from django.core.mail import send_mail, mail_admins
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def send_email(subject, to, context, template_name):
    """
    Method for sending email
    """
    html_message = render_to_string(template_name, context)
    plain_message = strip_tags(html_message)
    try:
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to],
            html_message=html_message,
            fail_silently=False
        )
    # Email the admin in case of any errors
    except Exception as e:
        mail_admins(
            subject='Error in sending email',
            message=f'Error in sending email: {e}'
        )
