from django.db import models
#from login import models


class Thread(models.Model):
    threadid = models.AutoField(db_column='threadID', primary_key=True)  # Field name made lowercase.
    user1 = models.ForeignKey('Users', models.DO_NOTHING, db_column='user1', related_name="user1")
    user2 = models.ForeignKey('Users', models.DO_NOTHING, db_column='user2', related_name="user2")

    class Meta:
        managed = False
        db_table = 'thread'
        app_label = "contact"

    def __str__(self):
        return self.user1, self.user2;


class Messages(models.Model):
    messageid = models.AutoField(db_column='messageID', primary_key=True)  # Field name made lowercase.
    message = models.TextField()
    sent = models.DateTimeField(blank=True, null=True)
    thread = models.ForeignKey('Thread', models.DO_NOTHING, db_column='thread')
    sentto = models.ForeignKey('Users', models.DO_NOTHING, db_column='sentTo',
                               related_name="message_sent_to")  # Field name made lowercase.
    sentfrom = models.ForeignKey('Users', models.DO_NOTHING, db_column='sentFrom',
                                 related_name="message_sent_from")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'messages'
        app_label = "contact"

    def __str__(self):
        return self.message
