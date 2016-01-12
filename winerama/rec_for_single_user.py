# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 19:28:22 2016

@author: Mykolas
"""

import os

os.chdir('D:/Users/Mykolas/winerama-recommender-tutorial/winerama')
os.getcwd()

os.environ['DJANGO_SETTINGS_MODULE'] = 'winerama.settings'

#import django

import django

django.setup()

from reviews.models import UserRating, Rating, Recommendation, Subject
from django.contrib.auth.models import User
from sklearn.cluster import KMeans
from scipy.sparse import dok_matrix, csr_matrix
import numpy as np
import pandas as pd
from scipy.spatial.distance import cosine
import datetime

from django.template import RequestContext

sim_matrix = pd.read_csv("data/sim_matrix.csv")

# Create a placeholder items for closes neighbours to an item

#Speifying how many neighbours to return

no__neighbours = 7

data_neighbours = pd.DataFrame(index=sim_matrix.columns,
                               columns=[range(no__neighbours)])
                               
# Loop through our similarity dataframe and fill in neighbouring item names

for i in range(0,len(sim_matrix.columns)):
    data_neighbours.iloc[i,:no__neighbours] = \
    sim_matrix.iloc[0:,i].sort_values(ascending=False)[:no__neighbours].index

data_neighbours.head(6).iloc[:6,]

# --- Start User Based Recommendations --- #

# Helper function to get similarity scores
def getScore(history, similarities):
   return sum(history*similarities.values)/sum(similarities)


#addratings
users_ratings = pd.DataFrame(list(UserRating.objects.all().values()))

ratings = pd.DataFrame(list(Rating.objects.all().values()))

ratings.columns =  ['average',  'content_type_id',  'count',
                      'rating_id',  'object_id',  'total']

all_data = users_ratings.merge( ratings, on = 'rating_id')

all_data_r = all_data.pivot(index='user_id', columns='object_id',
                                   values='score')

# fill NANs with 0's

all_data_r = all_data_r.fillna(0)

data = all_data_r

# Create a place holder matrix for similarities, and fill in the user name column
data_sims = pd.DataFrame(index=[1],
                columns=all_data_r.columns)

#end ratings
                
#Loop through all rows, skip the user column, and fill with similarity scores

for j in range(0,len(data_sims.columns)):
    user = data_sims.index[0]
    product = data_sims.columns[j]

    if data.iloc[0,j] > 0:
        data_sims.iloc[0,j] = 0

    else:
        product_top_names = data_neighbours.ix[product+1][1:6]
        product_top_sims = sim_matrix.ix[product].sort_values(ascending=False)[2:7]
        user_purchases = data.ix[user,product_top_names]

        #data_sims.iloc[0,j] = getScore(user_purchases,product_top_sims)
                
        data_sims.iloc[0,j] = getScore(user_purchases,product_top_sims)

# Get the top-3 subjects
data_recommend = pd.DataFrame(index=data_sims.index,
                              columns=['user_id','1','2','3'])

data_recommend['user_id'] = data_recommend.index
#data_recommend.ix[0:,0] = data_sims.ix[:,0]

# Instead of top song scores, we want to see IDs
for i in range(0,len(data_sims.index)):
    data_recommend.iloc[i,1:] = \
    data_sims.iloc[i,:].sort_values(ascending=False).iloc[1:4,].index.transpose()

# Translate IDs to Names

data_recommend_fn = pd.melt(data_recommend, id_vars=['user_id'])

subjects_names = pd.DataFrame(index=data_sims.index,
                              columns=['1','2','3'])

#subjects_names['user_id'] = subjects_names.index

data_recommend_fn.columns = ['user_id', 'variable', 'id']

data_recommend_fn = data_recommend_fn.merge( subjects_id, on = 'id',how='left')

for i in range(0,len(subjects_names.index)):
    for j in range(0, len(subjects_names.columns)):
        subjects_names.iloc[i,j] = \
        data_recommend_fn.iloc[i + j + ((len(subjects_names.index) - 1) * j ), 3]

# Print a sample
print data_recommend

data_recommend
#end