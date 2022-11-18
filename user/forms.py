from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User, Pet
from django.forms.widgets import NumberInput

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

class PetForm(forms.ModelForm):
    KIND_CHOICES = (
        (0, "강아지"),
        (1, "고양이"),
        (2, "어류"),
        (3, "조류"),
        (4,"파충류"),
        (5,"소동물"),
        (6,"기타")
    )
    def __init__(self,*args,request,**kwargs):
        # self.request = kwargs.pop("request")
        self.user = kwargs.pop("user") or None
        super(PetForm,self).__init__(*args,**kwargs)
        # self.fields["user"].initial = self.user
        print("form에서 확인")
        print(self.fields["user"].initial)
        print(type(self.user))

    # user = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    user = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.HiddenInput)
    profile = forms.ImageField(label='프로필')
    name = forms.CharField(label='이름')
    kind = forms.Select()
    breed = forms.CharField(label="품종")
    adoption_day = forms.DateField(label='입양일',widget=NumberInput(attrs={'type': 'date'}))
    birthday = forms.DateField(label='생일',widget=NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = Pet
        fields = ('user','profile','name','kind','breed','adoption_day','birthday')
