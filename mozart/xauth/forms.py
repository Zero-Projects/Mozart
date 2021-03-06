#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import date

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, EmailValidator
from django.utils import six

from djangular.forms import NgDeclarativeFieldsMetaclass, NgFormValidationMixin

from mozart.core import validators
from mozart.core.messages import custom_error_messages, regex_sentences
from mozart.core.messages import DAYS, MONTHS, SEXUALITY, USER_TYPE
from mozart.profiles.models import ExtendedUser, Contact, Address, Birthday


class LoginForm(six.with_metaclass(NgDeclarativeFieldsMetaclass, NgFormValidationMixin, forms.Form)):
    form_name = 'loginform'

    username = forms.CharField(
        max_length=20,
        min_length=5,
        validators=[RegexValidator(regex=regex_sentences['numbres_and_letters'])],
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
            }
        ),
    )

    password = forms.CharField(
        max_length=40,
        min_length=6,
        validators=[validators.eval_blank],
        widget=forms.PasswordInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(custom_error_messages['invalid_login'],)
            elif not self.user_cache.is_active:
                raise forms.ValidationError(custom_error_messages['inactive_account'])
        return cleaned_data


class SignupForm(six.with_metaclass(NgDeclarativeFieldsMetaclass, NgFormValidationMixin, forms.Form)):
    form_controller = 'signupFormCtrl'
    form_name = 'signupform'
    this_year = date.today().year

    day_of_birth = forms.ChoiceField(
        choices=DAYS,
        initial='1',
        widget=forms.Select(
            attrs={
                'class': 'mozart-field active-field',
                'ng-change': 'validateDate()',
                'mz-field': '',
            }
        ),
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
            }
        ),
    )

    month_of_birth = forms.ChoiceField(
        choices=MONTHS,
        initial='Enero',
        widget=forms.Select(
            attrs={
                'class': 'mozart-field active-field',
                'ng-change': 'validateDate()',
                'mz-field': '',
            }
        ),
    )

    password_1 = forms.CharField(
        max_length=40,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
            }
        ),
    )

    password_2 = forms.CharField(
        max_length=40,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
                'mz-match': 'password_1',
            }
        ),
    )

    user_sexuality = forms.ChoiceField(
        choices=SEXUALITY,
        initial='Masculino',
        widget=forms.Select(
            attrs={
                'class': 'mozart-field active-field',
                'ng-change': 'validateDate()',
                'mz-field': '',
            }
        ),
    )

    type_of_user = forms.ChoiceField(
        initial='Artista',
        choices=USER_TYPE,
        widget=forms.Select(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
            }
        ),
    )

    username = forms.CharField(
        max_length=20,
        min_length=5,
        widget=forms.TextInput(
            attrs={
                'class': 'mozart-field empty-initial-field',
                'mz-field': '',
                'ng-pattern': '/^[a-zA-Z0-9_ñÑ]*$/',
            }
        ),
    )

    year_of_birth = forms.IntegerField(
        max_value=this_year - 18,
        min_value=this_year - 100,
        widget=forms.NumberInput(
            attrs={
                'class': 'mozart-field active-field',
                'placeholder': 'Año',
                'ng-change': 'validateDate()',
                'value': this_year - 25,
                'mz-field': '',
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(SignupForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].validators = [RegexValidator(regex=regex_sentences['numbres_and_letters'])]
            if field == 'email':
                self.fields[field].validators = [EmailValidator()]
            if field == 'password_1' or field == 'password_2':
                self.fields[field].validators = [validators.eval_blank]
            self.fields[field].required = True

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return validators.eval_iexact(email, User, 'email', 'email')

    def clean_password_2(self):
        password_1 = self.cleaned_data.get('password_1')
        password_2 = self.cleaned_data.get('password_2')
        return validators.eval_matching(password_1, password_2)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return validators.eval_iexact(username, User, 'username', 'username')

    def save(self):
        cleaned_data = super(SignupForm, self).clean()

        user = User.objects.create_user(
            cleaned_data.get('username'),
            cleaned_data.get('email'),
            cleaned_data.get('password_2'),
        )

        extended_user_instance = ExtendedUser(
            user=user,
            user_type=cleaned_data.get('type_of_user'),
            sex=cleaned_data.get('user_sexuality')
        )

        extended_user_instance.nationality = 'US'
        extended_user_instance.save()

        birthday_instance = Birthday(
            user=user,
            day=cleaned_data.get('day_of_birth'),
            month=cleaned_data.get('month_of_birth'),
            year=cleaned_data.get('year_of_birth')
        )

        birthday_instance.save()

        contact_instance = Contact(user=user)
        contact_instance.save()

        address_instance = Address(user=user)
        address_instance.save()

        self.user_cache = authenticate(
            username=cleaned_data.get('username'),
            password=cleaned_data.get("password_2")
        )
