from django.contrib.auth.models import AbstractUser
from django.db import models

from db.base_model import BaseModel


class User(AbstractUser, BaseModel):
    '''用户模型类'''
    nickname = models.CharField(max_length=20, verbose_name='昵称')
    positon = models.CharField(max_length=20, verbose_name='职位')
    portrait = models.ImageField(upload_to='portrait', verbose_name='头像')

    class Meta:
        db_table = 'psh_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
