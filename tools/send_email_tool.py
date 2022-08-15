from django.core.mail import send_mail, mail_admins
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def send_email(subject, to, context, template_name):
    """
    Method for sending email
    """
    try:
        html_message = render_to_string(template_name, context)
        plain_message, from_email = strip_tags(html_message), settings.EMAIL_HOST_USER
        send_mail(subject,
                  plain_message,
                  from_email,
                  [to],
                  html_message=html_message)
    except Exception as e:
        # print(e)
        mail_admins("ERROR occurred in sending email",
                    message=e,
                    fail_silently=True)
        pass
