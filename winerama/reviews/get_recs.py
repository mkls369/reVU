# import os
#
# os.chdir('D:/Users/Mykolas/subjectrama-recommender-tutorial/subjectrama')
# os.getcwd()
#
# os.environ['DJANGO_SETTINGS_MODULE'] = 'subjectrama.settings'
#
# #import django
#
# import django
#
# django.setup()

from models import Subject, UserRating, Rating
from django.contrib.auth.models import User
from sklearn.cluster import KMeans
from scipy.sparse import dok_matrix, csr_matrix
import numpy as np
import pandas as pd
from scipy.spatial.distance import cosine


#getting all UserRating instances

qs = UserRating.objects.all()
vlqs = qs.values_list()
r = np.core.records.fromrecords(vlqs,
                                names=[f.name for f in UserRating._meta.fields])

#Creating a place holder to store user - item values

#Getting Users
users_id = pd.DataFrame(list(User.objects.all().values('id')))

#Getting subjects
subjects_id = pd.DataFrame(list(Subject.objects.all().values()))


#Getting UserRatings

users_ratings = pd.DataFrame(list(UserRating.objects.all().values()))

users_rating = users_ratings.pivot(index='user_id', columns='rating_id',
                                   values='score')

#Getting RAINGS ONly

ratings = pd.DataFrame(list(Rating.objects.all().values()))

ratings.columns =  ['average',  'content_type_id',  'count',
                      'rating_id',  'object_id',  'total']

all_data = users_ratings.merge( ratings, on = 'rating_id')

all_data_r = all_data.pivot(index='user_id', columns='object_id',
                                   values='score')


# fill NANs with 0's

all_data_r = all_data_r.fillna(0)

data = all_data_r

#Placeholder for subject x subject similarity
data_ibs = pd.DataFrame(index=all_data_r.columns ,
                        columns=all_data_r.columns)


# Lets fill in those empty spaces with cosine similarities
# Loop through the columns

no_subjects = len(data_ibs.columns)

for i in range(0, no_subjects) :
    # Loop through the columns for each column
    for j in range(0, no_subjects) :
      # Fill in placeholder with cosine similarities
      data_ibs.iloc[i,j] = 1 - cosine(all_data_r.iloc[:,[i]],
                                all_data_r.iloc[:,[j]])

# Create a placeholder items for closes neighbours to an item

#Speifyinghowmany neighbours to return

no__neighbours = 5

data_neighbours = pd.DataFrame(index=data_ibs.columns,
                               columns=[range(no__neighbours)])

# Loop through our similarity dataframe and fill in neighbouring item names

for i in range(0,len(data_ibs.columns)):
    data_neighbours.iloc[i,:no__neighbours] = \
    data_ibs.iloc[0:,i].sort_values(ascending=False)[:5].index

data_neighbours.head(6).iloc[:6,2:4]

# --- Start User Based Recommendations --- #

# Helper function to get similarity scores
def getScore(history, similarities):
   return sum(history*similarities)/sum(similarities)

# Create a place holder matrix for similarities, and fill in the user name column
data_sims = pd.DataFrame(index=all_data_r.index,
                columns=all_data_r.columns)

#data_sims.ix[:,:1] = all_data_r.ix[:,:1]

#Loop through all rows, skip the user column, and fill with similarity scores
for i in range(0,len(data_sims.index)):
    for j in range(0,len(data_sims.columns)):
        user = data_sims.index[i]
        product = data_sims.columns[j]

        if data.iloc[i,j] > 0:
            data_sims.iloc[i,j] = 0

        else:
            product_top_names = data_neighbours.ix[product][1:4]
            product_top_sims = data_ibs.ix[product].order(ascending=False)[1:4]
            user_purchases = data.ix[user,product_top_names]

            data_sims.iloc[i,j] = getScore(user_purchases,product_top_sims)

# Get the top-3 songs
data_recommend = pd.DataFrame(index=data_sims.index,
                              columns=['user_id','1','2','3'])

data_recommend['user_id'] = data_recommend.index
#data_recommend.ix[0:,0] = data_sims.ix[:,0]

# Instead of top song scores, we want to see IDs
for i in range(0,len(data_sims.index)):
    data_recommend.iloc[i,1:] = \
    data_sims.iloc[i,:].order(ascending=False).iloc[1:4,].index.transpose()


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
        data_recommend_fn.iloc[i + j + ((len(subjects_names.index) - 1) * i ), 3]



# Print a sample
print data_recommend

data_recommend


