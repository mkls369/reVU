from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import numpy as np
from star_ratings.models import Rating, UserRating
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Subject(models.Model):
    name = models.CharField(max_length=200)
    ratings = GenericRelation(Rating, related_query_name="subjects")

    def __str__(self):
        return self.name

    def get_average(self):
        rat = Rating.objects.get(subjects = self.id).average
        return rat

    def sort_by_rating(self):
        ratt = Subject.objects.filter(ratings__isnull=False).order_by('ratings__average')
        return ratt

class Recommendation(models.Model):
    name = models.CharField(max_length=100, null=True)
    Subjects = models.ManyToManyField(Subject)
    user = models.ForeignKey(User, null = True, related_query_name="recs")

    def get_members(self):
        return self.user

    def get_subjects(self):
        return "\n".join([u.name for u in self.Subjects.all()])

    def get_subject_list(self):
        subject_ids = Recommendation.objects.filter(user=25).values_list('subjects__pk', flat=True)
        entry_list = Subject.objects.filter(id__in=subject_ids)

        return entry_list