from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import send_mail
from django.conf import settings

def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_link = f"{settings.BASE_URL}/reset-password-confirm/{uid}/{token}/"
            send_mail(
                'Скидання паролю',
                f'Ви можете скинути свій пароль за посиланням: {reset_link}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return render(request, 'password_reset_email_sent.html')
        except User.DoesNotExist:
            return render(request, 'password_reset_form.html', {'error': 'Користувач з таким email не існує.'})
    else:
        return render(request, 'password_reset_form.html')