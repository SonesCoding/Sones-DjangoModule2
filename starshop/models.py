from django.db import models
from django import forms
from . import views

# Create your models here.
class Star(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    color = models.TextField(max_length=100)
    Quote = models.ManyToManyField(Quote)
    
    def __str__(self) -> str:
        return self.name
    
class Author(models.Model):
    name = models.CharField(300)
    
    def __str__(self) -> str:
        return self.name
    
    
class Quote(models.Model):
    name = models.CharField(max_length=50)
    Qtext = models.TextField()
    Author = models.ManyToManyField(Author)
    
    def __str__(self):
        quote_list = Quote.objects.all()
        return self.name + ", " + self.Author.name
    
    
# Will display stars, pick 1 star and hit a done button. use star data to fill in a statement and assign a random
#quote that will come with your star

#timestamp model for the checkout star + quote page.

        """
        Sirius, 50.00, Blue
        Regulus, 50.00, Orange
        Aldebaram, 65.00, Gold
        Maia, 100.00, Purple
        Electra, 150.00, ???
        Alcyone, 100.00, Red
        Celaeno, 75.00, Pink
        
        Beyonce,
        Emma Xu,
        Vincent Van Gogh
        Maya Angelou
        Socrates
        Oscar Wilde
        
        A, "Shine Bright Like a diamond.", Beyonce
        B, "You can be the brightest star in someones darkest nights.", Emma Xu
        C, "For my part I know nothing with any certainty, but the sight of the stars makes me dream." , Vincent Van Gogh
        D, "Nohting can dim the light which shines from within.", Maya Angelou
        E, "Be as you wish to seem.", Socrates
        F, "Wisdom begins in wonder.", Socrates
        G, "You can never be overdressed or overeducated.", Oscar Wilde
        
        """