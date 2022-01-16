from django import forms
from django.forms import ModelForm

# from .models import Comment, PasteFile
from .models import PasteFile


class PasteForm(ModelForm):
    title = forms.CharField(required=True)
    content = forms.CharField(
        required=False, widget=forms.Textarea(attrs={"rows": 15, "cols": 120})
    )

    class Meta:
        model = PasteFile
        fields = ("title", "content")


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ("comment_text",)
