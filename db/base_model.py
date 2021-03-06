from django.db import models

PHONE_SYSTEM_CHOICES = (
    (0, "AndroidPhone"),
    (1, "iOSPhone"),
    (2, "AndroidPad"),
    (3, "iOSPad")
)
CASE_RESULT_CHOICES = (
    (0, "watting"),  # 等待测试
    (1, "success"),  # 测试成功
    (2, "fail")  # 测试失败
)

Trader_TYPE_CHOICES = (
    (0, "全部"),
    (1, "国内券商"),
    (2, "自营项目"),
    (3, "国内期货")
)


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    class Meta:
        # 说明是一个抽象模型类
        abstract = True
