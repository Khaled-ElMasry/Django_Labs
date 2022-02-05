from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_fname = models.CharField(max_length=10, default='unknown', verbose_name="fname")
    user_lname = models.CharField(max_length=10, default='unknown', verbose_name="lname")
    user_usrname = models.CharField(max_length=30, default='unknown', verbose_name="user_name",unique=True,null=False)
    user_email = models.EmailField(unique=True, default="email@email.com")

    user_password = models.CharField(max_length=50)

    def __str__(self):
        return self.user_usrname
