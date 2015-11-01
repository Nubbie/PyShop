from django.views.generic import FormView, UpdateView
from customer.forms import RegisterForm, LoginForm, ProfileForm
from django.contrib import auth
from django.core.urlresolvers import reverse
from django import http
from customer.models import Customer

# Create your views here.


class RegisterView(FormView):
    form_class = RegisterForm

    def get_success_url(self):
        return reverse("customer:login")

    def get_template_names(self):
        request = self.request
        if isinstance(request, http.HttpRequest):
            if request.is_ajax():
                return ['form.html']
            return ["full_form.html"]

    def get_context_data(self, **kwargs):
        kwargs.update({
            'post': reverse('customer:register')
        })
        return super(RegisterView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        new = Customer()
        new.username = form.cleaned_data['username']
        new.set_password(form.cleaned_data['password1'])
        new.save()
        return super(RegisterView, self).form_valid(form)


class ProfileView(UpdateView):

    form_class = ProfileForm

    def get_object(self, queryset=None):
        return Customer.objects.filter(pk=self.request.user.id).first()

    def get_success_url(self):
        return reverse("shop:homepage")

    def get_template_names(self):
        request = self.request
        if isinstance(request, http.HttpRequest):
            if request.is_ajax():
                return ['form.html']
            return ["full_form.html"]

    def get_context_data(self, **kwargs):
        kwargs.update({
            'post': reverse('customer:profile')
        })
        return super(ProfileView, self).get_context_data(**kwargs)


class Login(FormView):
    form_class = LoginForm

    def get_success_url(self):
        return reverse("shop:homepage")

    def get_template_names(self):
        request = self.request
        if isinstance(request, http.HttpRequest):
            if request.is_ajax():
                return ['form.html']
            return ["full_form.html"]

    def get_context_data(self, **kwargs):
        kwargs.update({
            'post': reverse('customer:login')
        })
        return super(Login, self).get_context_data(**kwargs)

    def form_valid(self, form):
        credentials = {
            "username": form.cleaned_data['username'],
            "password": form.cleaned_data['password'],
        }
        user = auth.authenticate(**credentials)
        if user is None:
            form.add_error('username', "اطلاعات وارد شده صحیح نیست")
            return self.form_valid(form)
        auth.login(self.request, user)
        return super(Login, self).form_valid(form)

    pass


def logout(request):
    auth.logout(request)
    return http.HttpResponseRedirect(reverse("shop:homepage"))
