from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='User Name',
                               widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(max_length=30, label="Password",
                               widget=forms.PasswordInput(attrs={'class': "form-control"}))
