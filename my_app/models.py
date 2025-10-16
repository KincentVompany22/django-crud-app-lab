from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

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

RATING_CHOICES = [
    (5, '⭐️⭐️⭐️⭐️⭐️'),
    (4, '⭐️⭐️⭐️⭐️'),
    (3, '⭐️⭐️⭐️'),
    (2, '⭐️⭐️'),
    (1, '⭐️'),
]


class Stamp(models.Model):
    name = models.CharField(max_length=100, choices=COUNTRY_CHOICES, default=COUNTRY_CHOICES[0][0])
    days = models.IntegerField()
    season = models.CharField(max_length=100, choices=SEASON_CHOICES, default=SEASON_CHOICES[0][0])
    year = models.IntegerField()
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # linking a Stamp to a User

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("stamp-detail", kwargs={"pk": self.pk}) # refer to "pk" (primary key) because I created detail page as a class-based view and that is what is passed
    
class Stop(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('Visit Date')
    rating = models.IntegerField(choices=RATING_CHOICES, default=RATING_CHOICES[0][0])
    
    stamp = models.ForeignKey(Stamp, on_delete=models.CASCADE)
    # In a one-to-many relationship, the on_delete=models.CASCADE is required.
    # It ensures that if a Stamp record is deleted, all of the child Stops will be deleted automatically as well
        # - thus avoiding orphan records for Stops that are no longer tied to an existing Stamp.
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("stamp-detail", kwargs={"pk": self.stamp.pk}) # reference stamp because we are redirecting to the stamp details page

    class Meta:
        ordering = ['-date']


