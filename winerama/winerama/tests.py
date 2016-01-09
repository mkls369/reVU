import os

os.chdir('D:/Users/Mykolas/winerama-recommender-tutorial/winerama')
os.getcwd()

os.environ['DJANGO_SETTINGS_MODULE'] = 'winerama.settings'

#import django

import django
django.setup()
