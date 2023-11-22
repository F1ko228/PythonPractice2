from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User
from main.models import ApplicationCategory, Application

class ApplicationCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите название заявки'}), required=True)
    imageofapp = forms.ImageField(widget=forms.FileInput(), required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите описание'}), required=True)
    category = forms.ModelChoiceField(queryset=ApplicationCategory.objects.all(), required=True,)
    #username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}), required=False)
    #created_timestamp = forms.DateTimeField(widget=forms.SelectDateWidget(attrs={'readonly': True}), required=False)

    class Meta:
        model = Application
        fields = ('name', 'imageofapp', 'description', 'category')

    #def __init__(self, *args, **kwargs):
     #   super(ApplicationCreateForm, self).__init__(*args, **kwargs)


