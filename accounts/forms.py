from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile


def widget_attrs(placeholder):
    return {'class': 'form-control mb-2 mr-md-2', 'placeholder': placeholder}


def form_kwargs(widget, label, max_length):
    return {'widget': widget, 'label': label, 'max_length': max_length}


class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        **form_kwargs(
            widget=forms.TextInput(attrs=widget_attrs('')),
            label='First Name',
            max_length=20
        )
    )
    last_name = forms.CharField(
        **form_kwargs(
            widget=forms.TextInput(attrs=widget_attrs('')),
            label='Last Name',
            max_length=20
        )
    )
    username = forms.CharField(
        **form_kwargs(
            widget=forms.TextInput(attrs=widget_attrs('')),
            label='Phone Number',
            max_length=15
        )
    )
    email = forms.EmailField(
        **form_kwargs(
            widget=forms.TextInput(attrs=widget_attrs('')),
            label='Email',
            max_length=64 + 255
        )
    )
    password = forms.CharField(
        **form_kwargs(
            widget=forms.PasswordInput(attrs=widget_attrs('')),
            label='Password',
            max_length=64
        )
    )
    password_confirmation = forms.CharField(
        **form_kwargs(
            widget=forms.PasswordInput(attrs=widget_attrs('')),
            label='Confirm Password',
            max_length=64
        )
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        # Only accept phone number
        try:
            [int(char) for char in username]
        except Exception:
            raise forms.ValidationError(
                'Your phone number may contain only numbers')

        if len(username) != 10:
            raise forms.ValidationError(
                'Please enter a phone number with 10 digits!')
        # Clean password
        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match!')

        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(
        **form_kwargs(
            widget=forms.TextInput(attrs=widget_attrs('')),
            label='Phone Number',
            max_length=15
        )
    )
    password = forms.CharField(
        **form_kwargs(
            widget=forms.PasswordInput(attrs=widget_attrs('')),
            label='Password',
            max_length=64
        )
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = User.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError('The user is not registered!')
        elif user and not user.check_password(password):
            raise forms.ValidationError('Password Incorrect!')

        return self.cleaned_data


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(
                'This email address is already in use. Please supply a different email address.')
        return self.cleaned_data


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']

    def clean(self):
        age = self.cleaned_data.get('age')

        if age < 1 or age > 125:
            raise forms.ValidationError(
                'Please enter the age a person who is actually alive! (1-124)')
        return self.cleaned_data
