from django.contrib import admin

from .models import Subject, Recommendation

class RecommendationAdmin(admin.ModelAdmin):
    model = Recommendation
    list_display = ['name', 'get_members', 'get_subjects']

admin.site.register(Subject)
admin.site.register(Recommendation, RecommendationAdmin)