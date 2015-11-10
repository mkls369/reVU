from django.forms import ModelForm, Textarea
from .models import Review, Star


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 3}),
        }

class FormStar(ModelForm):
    class Meta:
        model = Star
        fields = ['rating']
