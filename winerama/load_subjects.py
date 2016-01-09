import sys, os 
import pandas as pd


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "winerama.settings")

import django
django.setup()

from reviews.models import Subject 


def save_subject_from_row(subject_row):
    subject = Subject()
    subject.id = subject_row[0]
    subject.name = subject_row[1]
    subject.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])
        subjects_df = pd.read_csv(sys.argv[1])
        print subjects_df

        subjects_df.apply(
            save_subject_from_row,
            axis=1
        )

        print "There are {} subjects".format(Subject.objects.count())
        
    else:
        print "Please, provide Subject file path"
