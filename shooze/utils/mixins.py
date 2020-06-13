from django.urls import reverse, reverse_lazy

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.http import Http404


class StaffRequiredMixin(object):
	@classmethod
	def as_view(self, *args, **kwargs):
		view = super(StaffRequiredMixin, self).as_view(*args, **kwargs)
		return login_required(view)

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_staff and request.user.is_active:
			return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
		else:
			raise Http404

class SuperUserRequiredMixin(object):
	@classmethod
	def as_view(self, *args, **kwargs):
		view = super(SuperUserRequiredMixin, self).as_view(*args, **kwargs)
		return login_required(view)

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_superuser and request.user.is_active:
			return super(SuperUserRequiredMixin, self).dispatch(request, *args, **kwargs)
		else:
			raise Http404

class MedicalUserRequiredMixin(object):
	@classmethod
	def as_view(self, *args, **kwargs):
		view = super(MedicalUserRequiredMixin, self).as_view(*args, **kwargs)
		return login_required(view)

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_medical and request.user.is_active or request.user.is_superuser:
			return super(MedicalUserRequiredMixin, self).dispatch(request, *args, **kwargs)
		else:
			raise Http404

class AppraisalRequireMixiin(object):
	@classmethod
	def as_view(self, *args, **kwargs):
		view = super(AppraisalRequireMixiin, self).as_view(*args, **kwargs)
		return login_required(view)

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		if request.user.can_appraise and request.user.is_active or request.user.is_superuser:
			return super(AppraisalRequireMixiin, self).dispatch(request, *args, **kwargs)
		else:
			raise Http404


class SecurityRequiredMixin(object):
	@classmethod
	def as_view(self, *args, **kwargs):
		view = super(SecurityRequiredMixin, self).as_view(*args, **kwargs)
		return login_required(view)

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_staff and request.user.is_security and not request.user.is_dismissed:
			return super(SecurityRequiredMixin, self).dispatch(request, *args, **kwargs)
		else:
			raise Http404

class InternRequiredMixin(object):
	@classmethod
	def as_view(self, *args, **kwargs):
		view = super(InternRequiredMixin, self).as_view(*args, **kwargs)
		return login_required(view)

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_intern and not request.user.is_dismissed:
			return super(InternRequiredMixin, self).dispatch(request, *args, **kwargs)
		else:
			raise Http404
