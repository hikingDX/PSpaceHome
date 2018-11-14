from django.contrib import admin

# Register your models here.
from app.testcase.models import TestCase, TestCaseBug, TestCaseModule, TestCaseFunction, TestCaseDocument, \
    TestCaseImage, Trader

admin.site.register(TestCase)
admin.site.register(TestCaseBug)
admin.site.register(TestCaseModule)
admin.site.register(TestCaseFunction)
admin.site.register(TestCaseDocument)
admin.site.register(TestCaseImage)
admin.site.register(Trader)
