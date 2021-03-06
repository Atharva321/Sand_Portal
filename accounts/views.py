from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import CustomerSignUpForm, DealerSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User,Order
from django.http import HttpResponse

def register(request):
    return render(request, '../templates/register.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class dealer_register(CreateView):
    model = User
    form_class = DealerSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class order(CreateView):
    model = Order
    form_class = Order
    template_name = '../templates/order.html'
    def form_valid(self, form):
        order = form.save()
        login(self.request, order)
        return redirect('/')

def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                #return HttpResponse(user.is_customer)

                print(username)
                if user.is_customer is True:
                    print(1)
                    user = User.objects.filter(username=username)
                    return render(request, '../templates/order.html', {'me': user[0]})
                else:
                    print(2)

                    return render(request, '../templates/order.html',{'me':user[0]})




                """
                #print(1)
                user = User.objects.filter(username=username)
                if user from User.is:
                    print(1)
                    client = int(1)
                    return render(request, '../templates/order.html', {'me': user[0]},client)
                    return HttpResponse('customer id')
                else:
                    print(2)
                    return render(request, '../templates/order.html',{'me':user[0]})
                    return HttpResponse('dealer id')
                    """


            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')
