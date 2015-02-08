# -*- encoding: utf-8 -*-

from .forms import UserInformationForm,ChangePasswordForm
from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect,render_to_response
from django.views.generic import FormView
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy

class InformationFormView(FormView):
	template_name = 'settings-account.html'
	form_class = UserInformationForm
	success_url =  reverse_lazy('settings_account')

	def form_valid(self,form):
		form.save()
		ctx = {'updated':'Perfil Actualizado','form':form}
		return render_to_response(self.template_name, ctx, context_instance = RequestContext(self.request))

	def get_form_kwargs(self):
		kwargs = super( InformationFormView,self).get_form_kwargs()
		kwargs['request'] = self.request
		return kwargs

	def get_initial(self):
		initial = {
			'adress':self.request.user.adress.adress,
			'city':self.request.user.adress.city,
			'description':self.request.user.mozart_user.description,
			'first_name':self.request.user.first_name,
			'last_name':self.request.user.last_name,
			'nationality':self.request.user.mozart_user.nationality,
			'neighborhood':self.request.user.adress.neighborhood,
			'personal_homepage':self.request.user.contact.personal_homepage,
			'profile_picture':self.request.user.mozart_user.profile_picture,
			'phone_number':self.request.user.contact.phone_number,
			'username' : self.request.user.username,
			'zip_code':self.request.user.adress.zip_code,
		}
		return initial

class ChangePasswordView(FormView):
	template_name = 'settings-password.html'
	form_class = ChangePasswordForm
	success_url = reverse_lazy('settings_password')


