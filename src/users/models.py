# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self,email,username,firstname,lastname,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(email=self.normalize_email(email),username = username,firstname = firstname, lastname = lastname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, firstname, lastname, password=None):
        user = self.create_user(email=self.normalize_email(email),password=password,username = username,firstname = firstname, lastname = lastname)
        user.admin = 1
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    last_login = None
    username = models.CharField(max_length=45,unique=True)
    password = models.TextField(max_length=200)
    email = models.EmailField(max_length=45)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    admin = models.IntegerField(blank=True, null=True)
    blocked = models.IntegerField(blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','firstname','lastname']
    objects = UserManager()

    class Meta:
        managed = False
        db_table = 'users'
        app_label ="users"

    def __str__(self):
        return self.username


class Ads(models.Model):
    adid = models.AutoField(db_column='adID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=45)
    desciption = models.TextField()
    published = models.DateTimeField()
    publisher = models.ForeignKey('Users', models.DO_NOTHING, db_column='publisher')
    sold = models.IntegerField(blank=True, null=True)
    solddate = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey('Categories', models.DO_NOTHING, db_column='category')

    class Meta:
        managed = False
        db_table = 'ads'

#class Thread(models.Model):
#    threadid = models.AutoField(db_column='threadID', primary_key=True)  # Field name made lowercase.
#    user1 = models.ForeignKey('Users', models.DO_NOTHING, db_column='user1',related_name="user1")
#    user2 = models.ForeignKey('Users', models.DO_NOTHING, db_column='user2',related_name="user2")
#
#    class Meta:
#        managed = False
#        db_table = 'thread'
#        app_label = "users"
#
#    def __str__(self):
#        return self.user1,self.user2;


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categories(models.Model):
    categoryid = models.AutoField(db_column='categoryID', primary_key=True)  # Field name made lowercase.
    category = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ImagesInAd(models.Model):
    imageid = models.AutoField(db_column='imageID', primary_key=True)  # Field name made lowercase.
    image = models.CharField(max_length=45, blank=True, null=True)
    adid = models.ForeignKey(Ads, models.DO_NOTHING, db_column='adID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'images_in_ad'
        unique_together = (('imageid', 'adid'),)


#class Messages(models.Model):
#    messageid = models.AutoField(db_column='messageID', primary_key=True)  # Field name made lowercase.
#    message = models.TextField()
#    sent = models.DateTimeField(blank=True, null=True)
#    thread = models.ForeignKey('Thread', models.DO_NOTHING, db_column='thread')
#    sentto = models.ForeignKey('Users', models.DO_NOTHING, db_column='sentTo',related_name="message_sent_to")  # Field name made lowercase.
#    sentfrom = models.ForeignKey('Users', models.DO_NOTHING, db_column='sentFrom',related_name="message_sent_from")  # Field name made lowercase.#
#
#    class Meta:
#        managed = False
#        db_table = 'messages'
#
#    def __str__(self):
#        return self.message


class Ratings(models.Model):
    rated = models.ForeignKey('Users', models.DO_NOTHING, db_column='rated',related_name="user_rated")
    ratedby = models.ForeignKey('Users', models.DO_NOTHING, db_column='ratedBy',related_name="user_rated_by")  # Field name made lowercase.
    score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ratings'
        unique_together = (('rated', 'ratedby'),)


class SellyoshitProduct(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sellyoshit_product'



