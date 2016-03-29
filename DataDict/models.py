#coding:utf-8
from django.db import models

# Create your models here.

class Dict(models.Model):
    seq = models.IntegerField(default=0,verbose_name=u'序号') 	
    dictname = models.CharField(max_length=50,verbose_name=u'字典名')
    dictcode = models.CharField(max_length=50,verbose_name=u'字典编码')

    class Meta:
        db_table = 't_s_dict'
        verbose_name_plural = verbose_name = u"字典项"
        ordering = ['seq']

    def __unicode__(self):
        return self.dictname  


class Item(models.Model):
    seq = models.IntegerField(default=0,verbose_name=u'序号') 	
    dictgroup = models.ForeignKey(Dict)	
    itemcode = models.CharField(max_length=50,verbose_name=u'字典编码')
    itemname = models.CharField(max_length=50,verbose_name=u'字典名')

    class Meta:
        db_table = 't_s_item'
        verbose_name_plural = verbose_name = u"字典值"
        ordering = ['seq']

    def __unicode__(self):
        return self.itemname  
