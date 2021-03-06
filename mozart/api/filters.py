#!/usr/bin/python
# -*- coding: utf-8 -*-

from mozart.works.models import Work
from mozart.events.models import Event
from mozart.profiles.models import Address, Contact, Birthday, ExtendedUser

from .mixins import GenericUserFilter


class AddressFilter(GenericUserFilter):

    class Meta(GenericUserFilter.Meta):
        model = Address


class BirthdayFilter(GenericUserFilter):

    class Meta(GenericUserFilter.Meta):
        model = Birthday


class ContactFilter(GenericUserFilter):

    class Meta(GenericUserFilter.Meta):
        model = Contact


class ExtendedUserFilter(GenericUserFilter):

    class Meta(GenericUserFilter.Meta):
        model = ExtendedUser
        fields = ['user', 'sex', 'nationality', 'user_type']


class EventFilter(GenericUserFilter):

    class Meta(GenericUserFilter.Meta):
        model = Event
        fields = ['user', 'date']
        order_by = ['-date']


class WorkFilter(GenericUserFilter):

    class Meta(GenericUserFilter.Meta):
        model = Work
        fields = ['user', 'category', 'work_type', 'slug']
        order_by = ['-date']
