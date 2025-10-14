from django.db import models
from django.urls import reverse

# Create your models here.

class Stamp(models.Model):
    SEASON_CHOICES = [ 
        ('spring', 'Spring'), # each item is a (value, label) pair
        ('summer', 'Summer'), 
        ('fall', 'Fall'),
        ('winter', 'Winter'),
    ]

    COUNTRY_CHOICES = [
        ('United States', '🇺🇸 United States'),
        ('Canada', '🇨🇦 Canada'),
        ('Mexico', '🇲🇽 Mexico'),
        ('Brazil', '🇧🇷 Brazil'),
        ('United Kingdom', '🇬🇧 United Kingdom'),
        ('Germany', '🇩🇪 Germany'),
        ('France', '🇫🇷 France'),
        ('Italy', '🇮🇹 Italy'),
        ('Spain', '🇪🇸 Spain'),
        ('Netherlands', '🇳🇱 Netherlands'),
        ('Switzerland', '🇨🇭 Switzerland'),
        ('Sweden', '🇸🇪 Sweden'),
        ('Australia', '🇦🇺 Australia'),
        ('Japan', '🇯🇵 Japan'),
        ('South Korea', '🇰🇷 South Korea'),
        ('China', '🇨🇳 China'),
        ('India', '🇮🇳 India'),
        ('South Africa', '🇿🇦 South Africa'),
        ('United Arab Emirates', '🇦🇪 United Arab Emirates'),
        ('Argentina', '🇦🇷 Argentina'),
    ]


    name = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    days = models.IntegerField()
    season = models.CharField(max_length=100, choices=SEASON_CHOICES)
    year = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("stamp-detail", kwargs={"pk": self.pk}) # refer to "pk" (primary key) because I created detail page as a class-based view and that is what is passed
    
        
    

