from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
        'username_taken': "This username is already taken.",
        'email_taken': "This email is already registered.",
        'password_too_short': "This password is too short. It must contain at least 8 characters.",
    }

    username = forms.CharField(
        label="Your username",
        error_messages={'unique': error_messages['username_taken']},
        widget=forms.TextInput(attrs={'id': 'id_username', 'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
    )

    email = forms.EmailField(
        label="Your email",
        error_messages={'unique': error_messages['email_taken']},
        widget=forms.EmailInput(attrs={'id': 'id_email', 'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
    )

    password1 = forms.CharField(
        label="Password",
        error_messages={'password_mismatch': error_messages['password_mismatch']},
        widget=forms.PasswordInput(attrs={'id': 'id_password1', 'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
    )

    password2 = forms.CharField(
        label="Confirm password",
        error_messages={'password_mismatch': error_messages['password_mismatch']},
        widget=forms.PasswordInput(attrs={'id': 'id_password2', 'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
    )
