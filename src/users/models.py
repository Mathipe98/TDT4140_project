from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, username, firstname, lastname, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(email=self.normalize_email(email), username=username, firstname=firstname, lastname=lastname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, firstname, lastname, password=None):
        user = self.create_user(email=self.normalize_email(email), password=password, username=username,
                                firstname=firstname, lastname=lastname)
        user.admin = 1
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    last_login = None
    username = models.CharField(max_length=45, unique=True)
    password = models.TextField(max_length=200)
    email = models.EmailField(max_length=45)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    admin = models.IntegerField(blank=True, null=True)
    blocked = models.IntegerField(blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'firstname', 'lastname']
    objects = UserManager()

    @property
    def is_staff(self):
        """Only users with field admin = True will have permission to enter django admin page"""
        return self.admin

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    class Meta:
        managed = True
        db_table = 'users'
        app_label = "users"

    def __str__(self):
        return self.username