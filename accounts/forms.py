from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#create user form as a class
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password']