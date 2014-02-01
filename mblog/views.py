from django.http import HttpResponse
from django.shortcuts import render_to_response
from mblogdb.models import UserDetail
import datetime

from django import forms
from django.forms.util import ErrorList
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            if request.POST.has_key('nickname'):
                nickname = request.POST['nickname']
            else:
                nickname = request.POST['username']
            new_user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
            new_user.save()

            new_user_detail = UserDetail(user=new_user,
                                         nickname=nickname)
            new_user_detail.save()
            return HttpResponseRedirect("/login")
    else:
        form = UserCreationForm()
    return render_to_response("register.html", {
        'form': form,
    },context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")

@login_required(login_url="/login")
def profile(request):
    class ProfileForm(forms.Form):
        nickname = forms.CharField(max_length=30)
        self_describe = forms.CharField(max_length=200,required=False)
        mail = forms.EmailField()
        image = forms.URLField(required=False)
        birthday = forms.DateField(required=False)

    user = UserDetail.objects.get(user=request.user.id)

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            cdata = form.cleaned_data

            # sex
            if request.POST['sex'] == 'man':
                sex = True
            elif request.POST['sex'] == 'woman':
                sex = False
            else:
                sex = None

            # sexual orientation
            if request.POST['sexual_orientation'] == 'unknow':
                sexual_orientation = 0
            elif request.POST['sexual_orientation'] == 'heterosexuality':
                sexual_orientation = 1
            elif request.POST['sexual_orientation'] == 'homosexuality':
                sexual_orientation = 2
            elif request.POST['sexual_orientation'] == 'bisexuality':
                sexual_orientation = 3
            elif request.POST['sexual_orientation'] == 'transgender':
                sexual_orientation = 4
            elif request.POST['sexual_orientation'] == 'asexuality':
                sexual_orientation = 5
            else:
                sexual_orientation = 0

            # city

            # update
            user.nickname = cdata.get('nickname', user.user.username)
            user.self_describe = cdata.get('self_describe', '')
            user.mail = cdata.get('mail', None)
            user.image = cdata.get('image', '/static/images/avatar.jpg')
            user.birthday = cdata.get('birthday', '2014-01-01')
            user.city = 0
            user.sex = sex
            user.sexual_orientation = sexual_orientation
            user.save()

    else:
        form = ProfileForm()
    return render_to_response("profile.html",
                              {'form':form},
                              context_instance=RequestContext(request))

@login_required(login_url="/login")
def password(request):
    class PasswordForm(forms.Form):
        old_password = forms.CharField()
        new_password = forms.CharField()
        password_confirmation = forms.CharField()

        def clean_password_confirmation(self):
            cnew_password = self.cleaned_data['new_password']
            cpassword_confirmation = self.cleaned_data['password_confirmation']
            if cnew_password != cpassword_confirmation:
                raise forms.ValidationError("The two password fields didn't match")
            return cpassword_confirmation

    user = User.objects.get(id=request.user.id)

    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            if user.check_password(form.cleaned_data.get('old_password', '')):
                user.set_password(form.cleaned_data['new_password'])
                user.save()
            else:
                form.errors["old_password"] = ErrorList([u'Invalid Password.'])
    else:
        form = PasswordForm()
    return render_to_response("password.html",
                              {'form':form},
                              context_instance=RequestContext(request))



def main(request):
    return render_to_response("main.html", context_instance=RequestContext(request))

def hello(request):
    return HttpResponse("Hello world!")

def current_time(request):
    now = datetime.datetime.now()
    return render_to_response('current_time.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), \
        It will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def display_meta(request):
    values = request.META.items()
    #values = request.GET.items()
    #values = request.POST.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%r</td><td>%r</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        users = User.objects.filter(username__icontains=q)
        return render_to_response('search_results.html',
                                  {'users': users, 'query': q})
    else:
        return HttpResponse('You submitted an empty form.')
