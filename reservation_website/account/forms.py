from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from .models import User, UserProfile
from reservation_website.settings import DATE_INPUT_FORMATS


class SignUpForm(UserCreationForm):
    last_name = forms.CharField(label='Фамилия:', required=True)
    first_name = forms.CharField(label='Имя:', required=True)
    patronymic_name = forms.CharField(label='Отчество:', required=True)
    email = forms.EmailField(label='Адрес электронной почты:', required=True)
    passport_id = forms.CharField(label='Идентификационный номер паспорта:', required=True)

    YEAR_CHOICES = ('1955','1956','1957','1958','1959',
        '1960','1961','1962','1963','1964','1965','1966','1967','1968','1969',
        '1970','1971','1972','1973','1974','1975','1976','1977','1978','1979',
        '1980','1981','1982','1983','1984','1985','1986','1987','1988','1989',
        '1990','1991','1992','1993','1994','1995','1996','1997','1998','1999',
        '2000','2001','2002','2003','2004'
    )
    
    date_of_birth = forms.DateField(
        label='Дата рождения:', 
        localize=True,
        widget=forms.SelectDateWidget(years=YEAR_CHOICES)
    )
    registration_city = forms.CharField(label='Город регистрации:', required=True)
    
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    @csrf_exempt
    def save(self):
        user: User = super().save(commit=False)
        user.last_name = self.cleaned_data.get('last_name')
        user.first_name = self.cleaned_data.get('first_name')
        user.patronymic_name = self.cleaned_data.get('patronymic_name')
        user.email = self.cleaned_data.get('email')
        user.passport_id = self.cleaned_data.get('passport_id')
        user.date_of_birth = self.cleaned_data.get('date_of_birth')
        user.registration_city = self.cleaned_data.get('registration_city')
        user.save()
        return user


class UpdateUserForm(forms.ModelForm):
    last_name = forms.CharField(label='Фамилия:', 
        max_length=50, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    first_name = forms.CharField(label='Имя:', 
        max_length=50, 
        required=True,  
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    patronymic_name = forms.CharField(label='Отчество:',    
        max_length=50, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.CharField(label='Адрес электронной почты:', 
        max_length=50, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    passport_id = forms.CharField(label='Идентификационный номер паспорта:', 
        max_length=14, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    YEAR_CHOICES = ('1955','1956','1957','1958','1959',
        '1960','1961','1962','1963','1964','1965','1966','1967','1968','1969',
        '1970','1971','1972','1973','1974','1975','1976','1977','1978','1979',
        '1980','1981','1982','1983','1984','1985','1986','1987','1988','1989',
        '1990','1991','1992','1993','1994','1995','1996','1997','1998','1999',
        '2000','2001','2002','2003','2004'
    )

    date_of_birth = forms.DateField(
        label='Дата рождения:', 
        localize=True,
        widget=forms.SelectDateWidget(years=YEAR_CHOICES)
    )

    registration_city = forms.CharField(label='Город регистрации:', 
        max_length=50, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['last_name','first_name', 'patronymic_name', 'email', 'passport_id', 'date_of_birth', 'registration_city']


class UpdateUserProfileForm(forms.ModelForm):
    photo = forms.ImageField(label='Фотография:', widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    additional_info = forms.CharField(label='Дополнительная информация:', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))

    class Meta:
        model = UserProfile
        fields = ['photo', 'additional_info']