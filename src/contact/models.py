"""
    Django database models for Threads, Messages and Ratings

    classes
        Threads:
            A thread of messages between two users
        Messages:
            A message between two users in a thread
        Ratings:
            A rating given to a user by another user

"""

from django.db import models
from pu.settings import AUTH_USER_MODEL
from django.utils import timezone


class Thread(models.Model):
    """
    A thread of messages between two users

    Attributes
        threadid:
            The ID of the thread
        user1:
            The first user in th thread
        user2:
            The second user in the thread

    Functions
        __str__: str
            toString returning the username of user1 and user2
        get_threadid: int
            Returning the id of the thread

    """
    threadid = models.AutoField(db_column='threadID', primary_key=True)  # Field name made lowercase.
    user1 = models.ForeignKey(AUTH_USER_MODEL, models.DO_NOTHING, db_column='user1', related_name="user_1")
    user2 = models.ForeignKey(AUTH_USER_MODEL, models.DO_NOTHING, db_column='user2', related_name="user_2")

    class Meta:
        managed = True
        db_table = 'thread'
        app_label = "contact"

    def __str__(self):
        """ Returns the username of user1 and user2 """
        return self.user1.username + " " + self.user2.username

    def get_threadid(self):
        """ Returns the id of the thread """
        return self.threadid


class Messages(models.Model):
    """
    A message between two users in a thread

    Attributes
        messageid:
            The ID of the message
        message:
            The message
        sent:
            Timestamp of when the message was sent
        thread:
            The thread the message belongs to
        sentto:
            The user the message is sent to
        sentfrom:
            The user the message is sent from

    Functions
        __str__: str
            toString returning the message
        publish: None
            Sets sent to current time
    """
    messageid = models.AutoField(db_column='messageID', primary_key=True)  # Field name made lowercase.
    message = models.TextField()
    sent = models.DateTimeField(blank=True, null=True)
    thread = models.ForeignKey('Thread', models.DO_NOTHING, db_column='thread')
    sentto = models.ForeignKey(AUTH_USER_MODEL, models.DO_NOTHING, db_column='sentTo',
                               related_name="message_sent_to")  # Field name made lowercase.
    sentfrom = models.ForeignKey(AUTH_USER_MODEL, models.DO_NOTHING, db_column='sentFrom',
                                 related_name="message_sent_from")  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'messages'
        app_label = "contact"

    def __str__(self):
        """ Returns the message """
        return self.message

    def publish(self):
        """ Sets sent to timezone.now(). Returns None"""
        self.sent = timezone.now()
        self.save()


class Ratings(models.Model):
    """
    A rating given to a user by another user

    Attributes
        ratingid:
            The ID of the rating
        rated:
            The user being rated
        ratedby:
            The user who rated
        score:
            The score the rated was given
    """
    ratingid = models.AutoField(db_column='ratingid', primary_key=True)
    rated = models.ForeignKey(AUTH_USER_MODEL, models.DO_NOTHING, db_column='rated', related_name="user_rated")
    ratedby = models.ForeignKey(AUTH_USER_MODEL, models.DO_NOTHING, db_column='ratedBy',
                                related_name="user_rated_by")  # Field name made lowercase.
    score = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'ratings'
        app_label = "contact"
