from django.db import models

# Create your models here.
from db.base_model import BaseModel


class VersionInfo(BaseModel):
    title = models.CharField(max_length=200)  # 标题
    trader_code = models.CharField(max_length=20)  # 券商代码
    commit_date = models.DateField()  # 提交日期
    name = models.CharField(max_length=100)  # 项目名称描述
    isdebug = models.BooleanField()  # 测试环境
    server_ip = models.CharField(max_length=100)  # 认证地址
    svn_version = models.CharField(max_length=20)  # svnRevison
    update_address = models.CharField(max_length=100)  # 下载地址
    version_code = models.CharField(max_length=20)  # versioncode
    upadete_version = models.CharField(max_length=200)  # 提交版本
    bundle_id = models.CharField(max_length=200)  # bundleid

    class Meta:
        db_table = 'ps_version_info'
        verbose_name = '开发版本说明书'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class VersionInfoBug(BaseModel):
    content = models.TextField(max_length=200)  # 问题描述
    level = models.IntegerField()  # 等级
    solution = models.TextField(max_length=200)  # 解决方案
    result = models.TextField(max_length=50)  # 自测结果
    man = models.ForeignKey('user.User', on_delete=models.CASCADE)  # 负责人
    versioninfo = models.ForeignKey('VersionInfo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'ps_version_bug'
        verbose_name = '开发版本说明书bug'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
