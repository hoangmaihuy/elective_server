from tuike_api.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from huey.contrib import djhuey

@djhuey.task()
def send_verification_code(to_email, verification_code):
    message = "【推课网】验证码：{}，有效5分钟，请凭验证码登陆。".format(verification_code)
    try:
        send_mail(
            subject="【推课网】登陆验证码",
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=False
        )
        return True
    except Exception as e:
        print(e)
        return False
