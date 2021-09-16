from django import forms

from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

#for item in choices:
  #   choice_list.append(item)


#choices = [('coding', 'coding'), ('sports', 'sports'), ('entertaiment','entertaiment')]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')

        widgets = {
           'title': forms.TextInput(attrs={'class': 'form-control'}),
           'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
           'author': forms.TextInput(attrs={'class': 'form-control',  'value' : '', 'id': 'elder', 'type' : 'hidden'}),
           #'author': forms.Select(attrs={'class': 'form-control'}),
           'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
           'body': forms.Textarea(attrs={'class': 'form-control'}),
           'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = Category.objects.all().values_list('name', 'name')
        choice_list = []
        
        for item in choices:
            choice_list.append(item)
        self.fields['category'].choices = choice_list


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('title', 'title_tag', 'body', 'snippet')

        widgets = {
           'title': forms.TextInput(attrs={'class': 'form-control'}),
           'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
           #'author': forms.Select(attrs={'class': 'form-control'}),
           'body': forms.Textarea(attrs={'class': 'form-control'}),
           'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('name', 'body')

        widgets = {
           'name': forms.TextInput(attrs={'class': 'form-control'}),
           'body': forms.Textarea(attrs={'class': 'form-control'}),

        }
