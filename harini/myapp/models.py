from django.db import models
from django.contrib import admin
class ZomatoDB(models.Model):
    orderNo=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=10)
    dish=models.CharField(max_length=20)
    rating=models.FloatField()
    address=models.TextField()
    Mobile_no=models.IntegerField()
    price=models.FloatField()
class ZomatoDBAdmin(admin.ModelAdmin):
	list_display=['orderNo','Name','dish','rating','address','Mobile_no','price'];