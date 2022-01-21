from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm): # DjangoのModelFormでは強力なValidationを使える

    class Meta: 
        model = Post 
        fields = '__all__'