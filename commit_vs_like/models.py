from django.db import models


# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='comment_AFS')
    afs = models.ForeignKey('all_for_sale.AFS', on_delete=models.CASCADE, related_name='comment_AFS')
    description = models.TextField(blank=False)
    owner = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='comment_user')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True)

    class Mete:
        ordering = ['created_at']


class LikeDislike(models.Model):
    class LikeDislikeType(models.IntegerChoices):
        Like = 1
        DISLIKE = -1

    afs = models.ForeignKey('all_for_sale.AFS', on_delete=models.CASCADE, related_name='like_dislike')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='like_dislike')
    type = models.SmallIntegerField(choices=LikeDislikeType.choices)

    class Mete:
        unique_together = ['afs', "user"]

    def __str__(self):
        return str(self.user)
