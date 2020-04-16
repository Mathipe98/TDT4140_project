from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):
    """
    A manager for the model Users

    functions
        create_user : user
            Creates a new user
        create_superuser : user
            Creates a new superuser, an user who is an admin on the site
    """
    def create_user(self, email, username, firstname, lastname, password=None):
        """
        Creates a new user

        :param email: The user's email
        :param username: The user's username
        :param firstname: The user's first name
        :param lastname: The user's last name
        :param password: The user's password
        :return:
            user : Returns the newly created user
        """
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(email=self.normalize_email(email), username=username, firstname=firstname, lastname=lastname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, firstname, lastname, password=None):
        """
        Creates a new superuser, an user who is an admin on the site

        :param email: The user's email
        :param username: The user's username
        :param firstname: The user's first name
        :param lastname: The user's last name
        :param password: The user's password
        :return:
            user : Returns the newly created superuser
        """
        user = self.create_user(email=self.normalize_email(email), password=password, username=username,
                                firstname=firstname, lastname=lastname)
        user.admin = 1
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser):
    """
    A registered user on the site

    Attributes
        userid : AutoField
            Unique user-ID for each registered user
        last_login : None
            Removes the attribute last_login from the AbstractBaseUser model
        username : CharField
            Unique username of the user
        password : TextField
            The user's password
        email : EmailField
            The user's email
        firstname : CharField
            The user's first name
        lastname : CharField
            The user's last name
        admin : IntegerField
            A bit checking if the user is an admin or not. 0 = false, 1 = true
        blocked : IntegerField
            A bit checking if the user is blocked from the site or not. 0 = false, 1 = true
    """
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
        
    @staticmethod
    def has_module_perms(app_label):
        return True

    @staticmethod
    def has_perm(perm, obj=None):
        return True
        
    class Meta:
        managed = True
        db_table = 'users'
        app_label = "users"

    def __str__(self):
        return self.username
