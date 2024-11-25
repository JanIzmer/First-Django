from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    anons = models.CharField('Anonse', max_length=250)
    full_text = models.TextField('Full text')
    dete = models.DateTimeField("Date of publication", auto_now_add=True)
    img = models.ImageField(name="image",blank=True, default="images/pythonlogo.png", upload_to="images")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/'+str(self.id)
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'Newses'
