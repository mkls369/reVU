import sys, os 
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "winerama.settings")

import django
django.setup()

from reviews.models import Rating, UserRating


def save_userrating_from_row(rating_row):
    rating = Rating()
    rating.id = rating_row[0]
    rating.object_id = rating_row[1]
    rating.content_type_id= rating_row[2]
    rating.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])
        reviews_df = pd.read_csv(sys.argv[1])
        print reviews_df

        reviews_df.apply(
            save_userrating_from_row,
            axis=1
        )

        print "There are {} UserRatings in DB".format(Rating.objects.count())
        
    else:
        print "Please, provide UserRatings file path"
