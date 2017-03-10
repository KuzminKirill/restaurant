from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import UserForm, OrderForm

from .models import Order, Salad, Soup, MainFood, Decert, Drink, Discount


# Create your views here.
def index(request):
    if not request.user.is_authenticated():
        return render(request, 'polls/login.html')
    else:
        orders = Order.objects.filter(user=request.user)
        return render(request, 'polls/index.html', {'orders': orders})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'polls/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #order = Orders.objects.filter(user=request.user)
                return render(request, 'polls/index.html') #, {'order': order}
            else:
                return render(request, 'polls/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'polls/login.html', {'error_message': 'Invalid login'})
    return render(request, 'polls/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #order = Order.objects.filter(user=request.user)
                return render(request, 'polls/index.html') #, {'order': order}
    context = {
        "form": form,
    }
    return render(request, 'polls/register.html', context)

#def orders(request):
#    return render_to_response('orders.html', {'orders': Order.objects.all(), 'username:' auth.get_user()})


@login_required
def create_order(request):
    if not request.user.is_authenticated():
        return render(request, 'polls/login.html')
    else:
        form = OrderForm(request.POST or None)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.status = 0
            order.bill = (order.salad.price + order.soup.price + order.main_food.price + order.drink.price + order.decert.price) * order.discount.coefficient
            order.save()
        context = {
            "form": form,
        }
        return render(request, 'polls/create_order.html', context)


def delete_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.delete()
    orders = Order.objects.filter(user=request.user)
    return render(request, 'polls/index.html', {'orders': orders})


def detail(request, order_id):
    if not request.user.is_authenticated():
        return render(request, 'polls/login.html')
    else:
        user = request.user
        order = get_object_or_404(Order, pk=order_id)
        return render(request, 'polls/detail.html', {'order': order, 'user': user})


#def salad(request):
#    if not request.user.is_authenticated():
#        return render(request, 'polls/login.html')
#    else:
#
#        return render('salad.html', {"salads": salad})
#
#
#def soup(request):
#    if not request.user.is_authenticated():
#        return render(request, 'polls/login.html')
#    else:
#        soup_list = Soup.objects.all()
#        return render('soup.html', {"soup": soup})
#

def show_menu(request):
    salad = Salad.objects.all()
    mainfood = MainFood.objects.all()
    decert = Decert.objects.all()
    drink = Drink.objects.all()
    soup = Soup.objects.all()
    return render(request, 'polls/menu.html', {'salad': salad, 'soup': soup, 'mainfood': mainfood, 'decert': decert, 'drink': drink})


def about(request):
    return render(request, 'polls/about.html')
