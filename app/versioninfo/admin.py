from django.contrib import admin

# Register your models here.
# 注册模型类
from app.versioninfo.models import VersionInfoBug, VersionInfo

admin.site.register(VersionInfo)
admin.site.register(VersionInfoBug)
