from django.db import models
# Create your models here.
class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    anons = models.CharField('Anonse', max_length=250)
    full_text = models.TextField('Full text')
    dete = models.DateTimeField("Date of publication", auto_now_add=True)
    img = models.ImageField(name="image",blank=True, default="pythonimage.webp", upload_to="images")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/'+str(self.id)
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'Newses'
