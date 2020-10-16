from django.template import loader
from django.core.mail import EmailMultiAlternatives
from pynliner import Pynliner


def email_from_template(html_template, txt_template, context, from_email):
    html_email = loader.render_to_string(html_template, context)
    html_email = Pynliner().from_string(html_email).run()
    text_email = loader.render_to_string(txt_template, context)
    details = {
        'subject': context['subject'],
        'body': text_email,
        'from_email': from_email,
        'to': context['to'],
    }
    msg = EmailMultiAlternatives(**details)
    msg.attach_alternative(html_email, 'text/html')
    return msg
