from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm #PasswordResetForm PARA ENVIO DE EMAIL, ESTUDAR ISSO DEPOIS HIHI
from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm): #formulario de cadastro padrao do django
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    #def __init__(self, *args, **kwargs):
    #    super(MyUserCreationForm, self).__init__(**args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'id':"id_register_username",
            'class': 'form-control',

        })
        self.fields['password1'].widget.attrs.update({
            'id':"id_register_password1",
            'class': 'form-control',
            
        })
        self.fields['password2'].widget.attrs.update({
            'id':"id_register_password2",
            'class': 'form-control',

        })

class MyPassworChangeForm(PasswordChangeForm): #formulario de cadastro padrao do django

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    #def __init__(self, *args, **kwargs):
    #   super(MyPassworChangeForm, self).__init__(**args, **kwargs)

        self.fields['old_password'].widget.attrs.update({
            'id':"id_change_old_password",
            'class': 'form-control',

        })
        self.fields['new_password1'].widget.attrs.update({
            'id':"id_change_password1",
            'class': 'form-control',
            
        })
        self.fields['new_password2'].widget.attrs.update({
            'id':"id_change_password2",
            'class': 'form-control',
            
        })