from django.forms import ModelForm
from django.contrib.auth.models import User

class CustomUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def save(self):
        self.clean()
        user = self.Meta.model(
            username = self.cleaned_data['username'],
            email = self.cleaned_data['email'],
        )
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
    
#credit for save function given to
#Om Kashyap, Stack Overflow
#https://stackoverflow.com/questions/72761071/username-and-password-are-always-incorrect-in-my-django-authenticationform
#initial problem: when new user signs up, password was not being stored,
#resulting in user being unable to log in after logging out initially.
#problem was isolated to the fact that a custom CustomUserForm (above) was being used instead of Django's default UserCreationForm,
#causing the password to be stored incorrectly.
#by using the above clean() method, password is now set explicitly, and stored into the database correctly,
#so that users can log in with the said password at a later time.