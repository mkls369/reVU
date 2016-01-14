# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import  Subject, Rating, Recommendation, UserRating
from django.template import RequestContext
import pandas as pd
import datetime
from .recommend import update_recommendation

from django.contrib.auth.decorators import login_required

def subject_list(request):
    subject_list = Subject.objects.order_by('name')
    context = {'subject_list':subject_list}
    return render(request, 'reviews/subject_list.html', context)

def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'reviews/subject_detail.html', {'subject': subject})

def user_rating_list(request, username=None):
    if not username:
        username = request.user.username

    rating_ids = pd.DataFrame(list(UserRating.objects.filter(user=request.user.id).values()))['rating_id']
    objects_ids = pd.DataFrame(list(Rating.objects.filter(id__in = rating_ids).values()))['object_id']
    subject_list = Subject.objects.filter(id__in = objects_ids)

    context = {'subject_list':subject_list, 'username':username}
    return render(request, 'reviews/user_review_list.html', context)


# @login_required
# def user_recommendation_list(request):
#
#     # get request user reviewed subjects
#     user_reviews = Review.objects.filter(user_name=request.user.username).prefetch_related('subject')
#     user_reviews_subject_ids = set(map(lambda x: x.subject.id, user_reviews))
#
#     # get request user cluster name (just the first one righ now)
#     try:
#         user_cluster_name = \
#             User.objects.get(username=request.user.username).cluster_set.first().name
#     except: # if no cluster assigned for a user, update clusters
#         update_clusters()
#         user_cluster_name = \
#             User.objects.get(username=request.user.username).cluster_set.first().name
#
#     # get usernames for other memebers of the cluster
#     user_cluster_other_members = \
#         Cluster.objects.get(name=user_cluster_name).users \
#             .exclude(username=request.user.username).all()
#     other_members_usernames = set(map(lambda x: x.username, user_cluster_other_members))
#
#     # get reviews by those users, excluding subjects reviewed by the request user
#     other_users_reviews = \
#         Review.objects.filter(user_name__in=other_members_usernames) \
#             .exclude(subject__id__in=user_reviews_subject_ids)
#     other_users_reviews_subject_ids = set(map(lambda x: x.subject.id, other_users_reviews))
#
#     # then get a subject list including the previous IDs, order by rating
#     subject_list = sorted(
#         list(subject.objects.filter(id__in=other_users_reviews_subject_ids)),
#         key=lambda x: x.average_rating,
#         reverse=True
#     )
#
#     return render(
#         request,
#         'reviews/user_recommendation_list.html',
#         {'username': request.user.username,'subject_list': subject_list}
#     )

def best_subjects():

    best_w = []
    best_w = Subject.objects.filter(ratings__isnull=False).order_by('-ratings__average')
    #best_w = subject.ratings.get('total')

    return best_w

def index(request, username=None):
    # context = RequestContext(request)
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!

    best_w = best_subjects()

    if not username:
        username = request.user.username

    #context_dict = {'boldmessage': "I am bold font from the context"}
    context_dict = {'subjects': best_w, 'username':username}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'reviews/index.html', context_dict)

def recs_for_user(request):

    subject_ids = Recommendation.objects.filter(user=request.user.id).values_list('Subjects__pk', flat=True)
    entry_list = Subject.objects.filter(id__in=subject_ids)
    update_recommendation()

    context_dict = {'username': request.user.username, 'subject_list': entry_list }

    return render(request, 'reviews/user_recommendation_list.html', context_dict)