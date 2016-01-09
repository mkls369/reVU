import sys, os 
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "winerama.settings")

import django
django.setup()

from reviews.models import Rating, UserRating


def save_userrating_from_row(userrating_row):
    userrating = UserRating()
    userrating.id = userrating_row[0]
    #userrating.created = datetime.datetime.now()
    #userrating.modified = datetime.datetime.now()
    #userrating.ip = rating_row[3]
    userrating.score = userrating_row[2]
    userrating.user_id = userrating_row[1]
    userrating.rating_id = userrating_row[3]
    userrating.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])
        reviews_df = pd.read_csv(sys.argv[1])
        print reviews_df

        reviews_df.apply(
            save_userrating_from_row,
            axis=1
        )

        print "There are {} UserRatings in DB".format(UserRating.objects.count())
        
    else:
        print "Please, provide UserRatings file path"
