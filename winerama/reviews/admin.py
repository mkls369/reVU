from django.contrib import admin

from .models import Wine, Review, Cluster, Recommendation

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('wine', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']
    

class ClusterAdmin(admin.ModelAdmin):
    model = Cluster
    list_display = ['name', 'get_members']

class RecommendationAdmin(admin.ModelAdmin):
    model = Recommendation
    list_display = ['name', 'get_members', 'get_wines']

admin.site.register(Wine)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Cluster, ClusterAdmin)
admin.site.register(Recommendation, RecommendationAdmin)