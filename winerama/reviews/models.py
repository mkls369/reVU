from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import numpy as np
from star_ratings.models import Rating, UserRating
from django.contrib.contenttypes.fields import GenericRelation

class Wine(models.Model):
    name = models.CharField(max_length=200)
    ratings = GenericRelation(Rating, related_query_name="wines")


    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __unicode__(self):
        return self.name

    def get_average(self):
        rat = Rating.objects.get(wines = self.id).average
        return rat

    def sort_by_rating(self):
        ratt = Wine.objects.filter(ratings__isnull=False).order_by('ratings__average')
        return ratt


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    wine = models.ForeignKey(Wine)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)


class Cluster(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def get_members(self):
        return "\n".join([u.username for u in self.users.all()])

class Recommendation(models.Model):
    name = models.CharField(max_length=100, null=True)
    wines = models.ManyToManyField(Wine)
    user = models.ForeignKey(User, null = True, related_query_name="recs")

    def get_members(self):
        return self.user

    def get_wines(self):
        return "\n".join([u.name for u in self.wines.all()])

    def get_wine_list(self):
        wine_ids = Recommendation.objects.filter(user=25).values_list('wines__pk', flat=True)
        entry_list = Wine.objects.filter(id__in=wine_ids)

        return entry_list