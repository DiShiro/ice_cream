from django import forms

from .models import Contest


class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ('title', 'description', 'price', 'comment')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }