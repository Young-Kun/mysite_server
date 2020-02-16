from random import choice
from django.core.mail import send_mail
from mysite_server.settings import EMAIL_HOST_USER


def generate_code(n):
    """
    生成n位数验证码
    :return:
    """
    seeds = '1234567890'
    random_str = []
    for i in range(n):
        random_str.append(choice(seeds))
    return ''.join(random_str)


def send_verify_code_by_email(verify_code, to_emails):
    subject = '验证码'
    message = '欢迎注册youngkun.site！您的验证码是：<h1>%s</h1>' % verify_code
    from_email = EMAIL_HOST_USER
    status = send_mail(
        subject,
        message,
        from_email,
        to_emails,
        fail_silently=False,
    )
    return status


# if __name__ == '__main__':
#     import os
#     import sys
#     import django
#
#     # django环境配置
#     pwd = os.path.dirname(os.path.realpath(__file__))
#     sys.path.append(pwd)
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite_server.settings')
#     django.setup()
#
#     verify_code = generate_code(4)
#     to_emails = ['youngkunzhu@163.com']
#     status = send_verify_code_by_email(verify_code, to_emails)
#     print(status)
