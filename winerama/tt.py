import os, sys, django

sys.path.append("C:/Users/Mykolas/winerama-recommender-tutorial/winerama")
os.environ["DJANGO_SETTINGS_MODULE"] = "winerama.settings"
django.setup()
