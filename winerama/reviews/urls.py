# -*- encoding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.subject_list, name='subject_list'),
    # ex: /review/5/
    #url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /subject/
    url(r'^subject_list/$', views.subject_list, name='subject_list'),
    # ex: /subject/5/
    url(r'^subject/(?P<subject_id>[0-9]+)/$', views.subject_detail, name='subject_detail'),
    # ex: /review/user - get reviews for the logged user
    url(r'^review/user/(?P<username>\w+)/$', views.user_rating_list, name='user_rating_list'),
    # ex: /review/user - get reviews for the user passed in the url
    url(r'^review/user/$', views.user_rating_list, name='user_rating_list'),
    # ex: /recommendation - get subject recommendations for the logged user
    #url(r'^recommendation/$', views.user_recommendation_list, name='user_recommendation_list'),

    url(r'^index/$', views.index, name='index'),
    url(r'^recommendation/$', views.recs_for_user, name='user_recommendation_list'),
    # url(r'^best_subject/$', views.best_subjects, name = 'best_subjects'),

     # url(r'^subject/(?P<subject_id>[0-9]+)/add_star/$', views.add_star, name='add_star'),
]