from django.db import models

# Create your models here.
from db.base_model import BaseModel, PHONE_SYSTEM_CHOICES, CASE_RESULT_CHOICES, Trader_TYPE_CHOICES


class TestCaseDocument(BaseModel):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)

    class Meta:
        db_table = 'ps_testcase_document'
        verbose_name = '测试用例文档'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class TestCaseFunction(BaseModel):
    ''' 功能模块'''
    doucument = models.ForeignKey('TestCaseDocument', on_delete=models.CASCADE)  # 归属 比如这个用例测试的全是
    content = models.CharField(max_length=200)

    class Meta:
        db_table = 'ps_testcase_function'
        verbose_name = '测试用例功能模块'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class TestCaseModule(BaseModel):
    doucument = models.ForeignKey('TestCaseDocument', on_delete=models.CASCADE)  # 归属 比如这个用例测试的全是
    name = models.CharField(max_length=200)  # 用例名称
    method = models.CharField(max_length=200)  # 功能模块
    func = models.ForeignKey('TestCaseFunction', on_delete=models.CASCADE)  # 项目名称描述
    expection = models.CharField(max_length=300)  # 预期结果
    remarks = models.CharField(max_length=300)  # 备注

    class Meta:
        db_table = 'ps_testcase_module'
        verbose_name = '测试用例'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class TestCase(BaseModel):
    module = models.ForeignKey('TestCaseModule', on_delete=models.CASCADE)
    phone_system = models.SmallIntegerField(choices=PHONE_SYSTEM_CHOICES, verbose_name='手机系统')
    test_man = models.ForeignKey('user.User', on_delete=models.CASCADE)
    result = models.SmallIntegerField(default=0, choices=CASE_RESULT_CHOICES, verbose_name='测试结果')
    trader = models.ForeignKey('Trader', on_delete=models.CASCADE, verbose_name='券商')

    class Meta:
        db_table = 'ps_testcase'
        verbose_name = '测试用例实例'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.module.name


class TestCaseBug(BaseModel):
    description = models.TextField(max_length=200)  # 问题描述
    level = models.IntegerField()  # 等级
    test_man = models.TextField(max_length=50)  # 负责人
    test_case = models.ForeignKey('TestCase', on_delete=models.CASCADE)

    class Meta:
        db_table = 'ps_testcase_bug'
        verbose_name = '测试用例实例Bug'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.description


class TestCaseImage(BaseModel):
    image = models.ImageField(upload_to='portrait', verbose_name='用例图片')
    test_case_bug = models.ForeignKey('TestCaseBug', on_delete=models.CASCADE)
    test_case = models.ForeignKey('TestCase', on_delete=models.CASCADE)

    class Meta:
        db_table = 'ps_testcase_img'
        verbose_name = '测试用例实例Bug'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.test_case_bug.description


class Trader(BaseModel):
    logo = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    type = models.IntegerField(default=0, choices=Trader_TYPE_CHOICES, verbose_name='券商类别')

    class Meta:
        db_table = 'ps_trader'
        verbose_name = '测试用例实例Bug'
        verbose_name_plural = verbose_name
