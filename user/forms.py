from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User

class UserForm(UserCreationForm):
    GENDER_MALE = "m"
    GENDER_FEMALE = "f"

    GENDER_CHOICES = [
        (GENDER_MALE,"남자"),
        (GENDER_FEMALE,"여자")
    ]

    first_name = forms.CharField(label="이름")
    email = forms.EmailField(label="이메일")
    gender = forms.ChoiceField(label="성별",widget=forms.RadioSelect,choices=GENDER_CHOICES)
    # gender = forms.ModelChoiceField(label="성별",widget=forms.RadioSelect,choices=User.objects.all(),)
    birthday = forms.DateField(label="생일")
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "password1",
            "password2",
            "email",
            "gender",
            "birthday"
        )
