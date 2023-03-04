from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    post_image = forms.ImageField()
    text = forms.Textarea()

    class Meta:
        model = Postfields = ["post_image", "text"]