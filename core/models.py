from django.db import models
from django.contrib.auth.models import User
from django.contrib.comments.models import Comment

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    librarian = models.BooleanField(null=False)
    
    @property
    def karma(self):
        myComments = self.user.comment_comments.all()
        myKarma = 0
        for comment in myComments:
            myKarma += comment.karma
        return myKarma
        
class CommentExtras(models.Model):
    comment = models.OneToOneField(Comment, related_name='extras')
    karma = models.IntegerField(default=0)
    dplaLink = models.URLField()
    question = models.ForeignKey('Question', related_name='commentextras')
    
class Question(models.Model):
    user = models.ForeignKey(User, related_name='user')
    text = models.TextField()
    
    @property
    def open(self):
        for extra in self.commentextras:
            if extra.karma:
                return False
        return True
    
        