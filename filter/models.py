from django.db import models

class SearchHistory(models.Model):
    """ Data for user search history"""
    user = models.CharField(max_length=100,null=False,blank=False)
    keyWord = models.CharField(max_length=10,null=False, blank=False)
    searchedDate = models.DateTimeField();
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self.keyWord)