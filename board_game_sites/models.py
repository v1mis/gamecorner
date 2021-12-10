from typing import Text
from django.db import models


#THE BOARDGAME MODEL
class Boardgame(models.Model):

    text = models.CharField(max_length = 100)
    date_added = models.DateTimeField(auto_now_add = True)

    #RETURN A STRING REPRESENTATION OF THE MODEL
    def __str__(self):
        return self.text

#INFORMATION MODEL FOR THE BOARD GAMES
class Info(models.Model):

    boardgame = models.ForeignKey(Boardgame, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Info'

    #RETURN A STRING REPRESENTATION OF THE MODEL
    def __str__(self):
        return f"{self.text[:50]}"


