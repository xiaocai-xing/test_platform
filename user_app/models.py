from django.db import models

# Create your models here.
# ORM  创建数据库表

# class  = table user_app_project 数据库的表名，前缀区别应用
# 变量 = 表中的字段（类型，长度等）
class Project(models.Model):
    name = models.CharField("名称", max_length=100, blank=False, null=True)
    describe = models.TextField("描述", default="")
    status = models.BooleanField("状态", default=True)
    create_time = models.DateTimeField("创建时间", auto_now=True)

class Module(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=100, blank=False, default="")
    describe = models.TextField("描述", default="")
    create_time = models.DateTimeField("创建时间", auto_now=True)