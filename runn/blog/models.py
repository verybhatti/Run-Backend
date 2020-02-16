from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Blog(models.Model):
    football='football'
    cricket='cricket'
    badminton='badminton'
    karate='karate'
    table_Tennis='table tennis'
    tennis='tennis'
    gymnastics='gymnastics'
    boxing='boxing'
    chess='chess'
    volleyball='volleyball'
    basketball='basketball'
    e_Gaming='e gaming'
    swimming='swimming'
    sports_type_choices = [
        (football,'Football'),
        (cricket,'Cricket'),
        (badminton,'Badminton'),
        (karate,'Karate'),
        (table_Tennis,'Table Tennis'),
        (gymnastics,'Gymnastics'),
        (boxing,'Boxing'),
        (chess,'Chess'),
        (volleyball,'Volleyball'),
        (basketball,'Basketball'),
        (e_Gaming,'E Gaming'),
        (swimming,'Swimming')
    ]

    sports_type = models.CharField(
        max_length=15,
        choices=sports_type_choices,
        default=football
    )
    title = models.CharField(max_length=255)
    content = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    featured_Image = models.ImageField(upload_to='images/',blank=True,null=True)
    
    def __str__(self):
        return self.Title