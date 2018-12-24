from django.db import models

# Create your models here.
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True,max_length=15,unique=True)
    addr = models.CharField(max_length=128)


class Book(models.Model):


    id = models.AutoField(primary_key=True,)
    title = models.CharField(null=False,max_length=20,unique=True)
    publisher = models.ForeignKey(to='Publisher')

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, null=False, unique=True)
    # 告诉ORM 我这张表和book表是多对多的关联关系,ORM自动帮我生成了第三张表
    book = models.ManyToManyField(to="Book")

