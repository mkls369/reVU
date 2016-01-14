# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 19:28:22 2016

@author: Mykolas
"""

import os

os.chdir('C:/Users/mykolas.suminas/Documents/GitHub/reVU/winerama')
os.getcwd()

os.environ['DJANGO_SETTINGS_MODULE'] = 'winerama.settings'

#import django

import django

django.setup()

from reviews.models import UserRating, Rating, Recommendation, Subjects, Subject
from django.contrib.auth.models import User
import numpy as np
import pandas as pd
from scipy.spatial.distance import cosine
import datetime
from compiler.ast import flatten

from django.template import RequestContext

sim_matrix = pd.read_csv("data/sim_matrix.csv")

# Create a placeholder items for closes neighbours to an item

#Specifying how many neighbours to return

no__neighbours = 7

data_neighbours = pd.DataFrame(index=sim_matrix.columns,
                               columns=[range(no__neighbours)])
                               
# Loop through our similarity dataframe and fill in neighbouring item names

for i in range(0,len(sim_matrix.columns)):
    data_neighbours.iloc[i,:no__neighbours] = \
    sim_matrix.iloc[0:,i].sort_values(ascending=False)[:no__neighbours].index

data_neighbours = data_neighbours.drop(0, 1)

# --- Start User Based Recommendations --- #

# Helper function to get similarity scores
def getScore(history, similarities):
   return sum(history*similarities.values)/sum(similarities)


#addratings #test user = 101
user_used = 101

users_ratings = pd.DataFrame(list(UserRating.objects.filter(user=user_used).values()))

ratings = pd.DataFrame(list(Rating.objects.all().values()))

ratings.columns =  ['average',  'content_type_id',  'count',
                      'rating_id',  'object_id',  'total']

all_data = users_ratings.merge(ratings, on = 'rating_id', how = 'outer')

all_data['user_id'] = user_used

all_data_r = all_data.pivot(index='user_id', columns='object_id',
                                   values='score')

# fill NANs with 0's

all_data_r = all_data_r.fillna(0)

data = all_data_r

# Create a place holder matrix for similarities, and fill in the user name column
data_sims = pd.DataFrame(index=[1],
                columns=all_data_r.columns)

#end ratings
#user = data_sims.index[0]                
#Loop through all rows, skip the user column, and fill with similarity scores

for j in range(0,len(data_sims.columns)):     
    product = data_sims.columns[j]
    
    if data.iloc[0,j] > 0:
        data_sims.iloc[0,j] = 0

    else:
        product_top_names = data_neighbours.loc[str(product)]
        
        product_top_sims = sim_matrix.ix[product].drop(['object_id',str(product)]) \
        .sort_values(ascending=False)[0:no__neighbours-1]
        
        user_purchases = data.ix[user_used,product_top_names]

        #data_sims.iloc[0,j] = getScore(user_purchases,product_top_sims)
                
        data_sims.iloc[0,j] = getScore(user_purchases,product_top_sims)

## subjects to recommend
subs_to_rec = 3

column_names = flatten(['user_id', map(str, range(1,subs_to_rec+1) ) ])

# Get the top-3 subjects
data_recommend = pd.DataFrame(index=data_sims.index,
                              columns = column_names)

data_recommend['user_id'] = user_used
#data_recommend.ix[0:,0] = data_sims.ix[:,0]

# Instead of top song scores, we want to see IDs
data_recommend.iloc[0,1:subs_to_rec+1] = \
data_sims.iloc[0].sort_values(ascending=False).iloc[0:subs_to_rec].index.transpose()

# Update Recommendation
Recommendation.objects.filter(user = user_used).delete()

new_rec = Recommendation(user_id = user_used)

new_rec.save()

for i in range(1, subs_to_rec+1):

    new_rec.Subjects.add(Subject.objects.get(id =data_recommend.iloc[0,i] ) )

#new_rec.Subjects.add(Subject.objects.filter(id__in=data_recommend.iloc[0,1:subs_to_rec+1]))

# Translate IDs to Names

#data_recommend_fn = pd.melt(data_recommend, id_vars=['user_id'])
#
#subjects_names = pd.DataFrame(index=data_sims.index,
#                              columns=['1','2','3'])
#
#for i in range(0,len(subjects_names)):
#    subjects_names.iloc
## Print a sample
#print data_recommend
#
#data_recommend
#end