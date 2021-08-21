from db.models import models 



class Videos(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')


    def __str__(self):
        return self.title