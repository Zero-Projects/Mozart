# -*- encoding: utf-8 -*-

from .forms import UserInformationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect,render_to_response
from django.views.generic import FormView
from django.template import RequestContext

class InformationFormView(FormView):
	template_name = 'account-settings.html'
	form_class = UserInformationForm
	success_url = '/configuracion/informacion'

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
			'username' : self.request.user.username,
			'first_name':self.request.user.first_name,
			'last_name':self.request.user.last_name,
			'nationality':self.request.user.mozart_user.nationality,
			'description':self.request.user.mozart_user.description,
			'personal_homepage':self.request.user.contact.personal_homepage,
			'phone_number':self.request.user.contact.phone_number,
			'adress':self.request.user.adress.adress,
			'city':self.request.user.adress.city,
			'zip_code':self.request.user.adress.zip_code,
			'neighborhood':self.request.user.adress.neighborhood,
		}
		return initial


