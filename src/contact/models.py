from django.db import models
#from login import models
from pu.settings import AUTH_USER_MODEL
from django.utils import timezone


class Thread(models.Model):
    threadid = models.AutoField(db_column='threadID', primary_key=True)  # Field name made lowercase.
    user1 = models.ForeignKey(AUTH_USER_MODEL, models.DO_NOTHING, db_column='user1', related_name="user_1")
    user2 = models.ForeignKey(AUTH_USER_MODEL, models.DO_NOTHING, db_column='user2', related_name="user_2")

    class Meta:
        managed = False
        db_table = 'thread'
        app_label = "contact"

    def __str__(self):
        return self.user1.username + " " + self.user2.username

    def get_threadid(self):
        return self.threadid


class Messages(models.Model):
    messageid = models.AutoField(db_column='messageID', primary_key=True)  # Field name made lowercase.
    message = models.TextField()
    sent = models.DateTimeField(blank=True, null=True)
    thread = models.ForeignKey('Thread', models.DO_NOTHING, db_column='thread')
    sentto = models.ForeignKey(AUTH_USER_MODEL, models.DO_NOTHING, db_column='sentTo',
                               related_name="message_sent_to")  # Field name made lowercase.
    sentfrom = models.ForeignKey(AUTH_USER_MODEL, models.DO_NOTHING, db_column='sentFrom',
                                 related_name="message_sent_from")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'messages'
        app_label = "contact"

    def __str__(self):
        return self.message

    def publish(self):
        self.sent = timezone.now()
        self.save()
