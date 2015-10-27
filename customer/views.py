from django.views.generic import FormView
from customer.forms import RegisterForm, LoginForm
from django.core.urlresolvers import reverse
from django import http
# Create your views here.


class RegisterView(FormView):
    form_class = RegisterForm

    def get_success_url(self):
        return reverse("homepage")

    def get_template_names(self):
        request = self.request
        if isinstance(request,  http.HttpRequest):
            if request.is_ajax():
                return ['form.html']
            return ["full_form.html"]

    def get_context_data(self, **kwargs):
        kwargs.update({
            'post': reverse('customer:register')
        })
        return super(RegisterView, self).get_context_data(**kwargs)


class Login(FormView):
    form_class = LoginForm

    def get_success_url(self):
        return reverse("homepage")



    def get_template_names(self):
        request = self.request
        if isinstance(request,  http.HttpRequest):
            if request.is_ajax():
                return ['form.html']
            return ["full_form.html"]

    def get_context_data(self, **kwargs):
        kwargs.update({
            'post': reverse('customer:login')
        })
        return super(Login, self).get_context_data(**kwargs)


    pass
