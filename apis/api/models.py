from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser, models.Model):
      avatar = models.ImageField(upload_to='uploads/%Y/%m')


class Account(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(null=False, max_length=100)
    username = models.CharField(null=False, max_length=20)
    role = models.CharField(null=False, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username

class Rack_group(models.Model):
    location = models.CharField(null=False,max_length=100)
    description = models.TextField(null=True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id_Rackgroup = models.ForeignKey(User,related_name="Rack_group",on_delete= models.DO_NOTHING,null=True)




class Rack(models.Model):
    rack_name = models.CharField(null=False,max_length=100)
    role = models.CharField(null=False,max_length=100)
    rack_group_id = models.ForeignKey(Rack_group, related_name="Rack", on_delete= models.CASCADE)
    user_id_Rack = models.ForeignKey(User,related_name="Rack",on_delete=models.DO_NOTHING,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.rack_name
class Document(models.Model):
    #image = models.ImageField(upload_to='images/%Y/%m',default=None) #duong link anh = MEDIA_ROOT + upload_to
    rack_id_Document = models.ForeignKey(Rack, related_name="Document",on_delete=models.DO_NOTHING)
    name = models.CharField(null=False,max_length=100)
    #user_id_Document = models.ForeignKey(Account, on_delete=models.DO_NOTHING,default=None)
    author = models.CharField(null=False,max_length=100)
    published_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField()
    active = models.BooleanField(default=True)
    group_rack_id = models.ForeignKey(Rack_group,on_delete=models.DO_NOTHING,null=True)
    def __str__(self):
        return self.name

class Borrowing(models.Model):
    document_id = models.ForeignKey(Document, related_name="Borrowing",on_delete=models.DO_NOTHING)
    user_id_Borrowing = models.ForeignKey(User,related_name="Borrowing",on_delete=models.CASCADE,null=True)
    date_borrowed = models.DateTimeField()
    date_returned = models.DateTimeField()

class Environment_status(models.Model):
    temperature = models.FloatField(null=False)
    humidity = models.FloatField(null=False)
    smoke = models.CharField(null=False,max_length=100)
    collision = models.CharField(null=False,max_length=100)
    rack_id_Environment = models.ForeignKey(Rack, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

class Operation_status(models.Model):
    movement_speed = models.FloatField(null=False)
    weight = models.FloatField(null=False)
    displacement = models.FloatField(null=False)
    number_users = models.IntegerField(null=False)
    is_hard_locked = models.BooleanField(default=False)
    is_endpoint = models.BooleanField(default=False)
    user_id_Operation = models.ForeignKey(Account,related_name="Operation",on_delete=models.CASCADE)
    rack_id_Operation = models.ForeignKey(Rack,related_name="Operation",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

class Breakdown_status(models.Model):
    is_obstructed = models.BooleanField(default=False)
    is_skewed = models.BooleanField(default=False)
    rack_id_Breakdown = models.ForeignKey(Account,related_name="Beakdown",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    is_overload_motor = models.BooleanField(default=False)

class Operation(models.Model):
    guide_light = models.IntegerField(null=False,default=0)
    open_specific_rack = models.IntegerField(null=False,default=0)
    ventilate = models.BooleanField(default=False)
    rack_id_Operation = models.ForeignKey(Rack,on_delete=models.CASCADE, null =True)
    created_at = models.DateTimeField(auto_now=True)
    handlemoving = models.IntegerField(null=False,default=0)
    group_id = models.IntegerField(null=False,default=0)

class History(models.Model):
    action = models.CharField(null=False, max_length=200)
    created_at = models.DateTimeField()

class Maintenance(models.Model):
    action = models.CharField(null=False, max_length=200)
    created_at = models.DateTimeField()
