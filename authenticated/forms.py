from django import forms

class LoginForm(forms.Form):

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={

            'id': 'id_login_username',
            'class':'form_control'
        }))
    password = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={

            'id': 'id_login_password',
            'class':'form_control'
        }))