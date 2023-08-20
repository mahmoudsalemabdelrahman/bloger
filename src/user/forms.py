from django import forms
from django.contrib.auth.models import User

class UserCreationForms(forms.ModelForm):

    username = forms.CharField(label='اسم المستخدم', max_length=50)
    email = forms.EmailField(label='البريد الالكتروني')
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الاخير')
    password1 = forms.CharField(label= 'كلمه المرور', widget=forms.PasswordInput(),min_length=8)
    password2 = forms.CharField(label='تاكيد كلمه  المرور', widget=forms.PasswordInput(),min_length=8)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')