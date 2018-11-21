from django.dispatch import receiver
from django.core.signals import request_finished

## decorators 方式绑定
from app.chat.task import mytask
from app.testcase.models import TestCaseDocument


@receiver(request_finished, dispatch_uid="request_finished")
def my_signal_handler(sender, **kwargs):
    print("Request finished!================================")


# 普通绑定方式
# def my_signal_handler(sender, **kwargs):
#     print("Request finished!================================")
#
#
# request_finished.connect(my_signal_handler)


# 针对model 的signal


from django.dispatch import receiver
from django.db.models.signals import post_save

from app.user.models import User


@receiver(post_save, sender=User, dispatch_uid="user_post_save")
def my_model_handler(sender, **kwargs):
    print('Saved: {}'.format(kwargs['instance'].__dict__))


@receiver(post_save, sender=TestCaseDocument, dispatch_uid="testcase_post_save")
def my_model_handler(sender, **kwargs):
    print('Saved: {}'.format(kwargs['instance'].__dict__))
