from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, Category, Customer, Cart, OrderPlaced
from .forms import NewUserForm, CustomerProfile
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def hpage(request):
    category=Category.objects.all()
    dic={"category":category}
    return render(request, "shop/hpage.html", dic)

def category(request, category):
    part=get_object_or_404(Category, slugc=category)
    item_list=list(Product.objects.filter(category=part))
    dic={"item_list":item_list}
    return render(request, "shop/category.html", dic)

@login_required(login_url='/login/')
def product(request, category, slug):
	product=get_object_or_404(Product, slug=slug)
	dic={"product":product}
	return render(request, "shop/product.html", dic)

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("profile")
	else:
		form = NewUserForm()
	return render (request=request, template_name="shop/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("homepage")
			else:
				messages.error(request, "Invalid username, or password")
		else:
			messages.error(request, "Invalid username, or password")
	form = AuthenticationForm()
	return render(request=request, template_name="shop/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("homepage")

def cart(request):
	user = request.user
	id = request.GET.get('prod_id')
	item = Product.objects.get(id=id)
	product = get_object_or_404(Product, id=id)
	x= Cart(user=user, item=item).save()
	cart = Cart.objects.filter(user=user)
	sum=0
	total=0
	for c in cart:
		temp=(c.item.item_cost)*(c.quantity)
		sum+=temp
		total = sum+70
	return render(request, "shop/product.html", {"product":product})

def profile(request):
	if request.method == "POST" :
		form = CustomerProfile(request.POST)
		if form.is_valid():
			user = request.user
			name = form.cleaned_data['name']
			address = form.cleaned_data['address']
			city = form.cleaned_data['city']
			state = form.cleaned_data['state']
			zipcode = form.cleaned_data['zipcode']
			cust = Customer(user=user, name=name, address=address, city=city, state=state, zipcode=zipcode).save()
			messages.success(request, "Profile Registration successful." )
			return redirect("homepage")
	else:
		form = CustomerProfile()
	return render(request,"shop/profile.html", {"form":form})

def adress(request):
	add = Customer.objects.get(user=request.user)
	dic = {"add":add}
	return render(request, "shop/address.html", dic)

def placeorder(request):
	user = request.user
	add = Customer.objects.get(user=user)
	cart_items = Cart.objects.filter(user=user)
	sum=0
	total=0
	for c in cart_items:
		sum+=(c.item.item_cost)*(c.quantity)
		total=sum+70
	return render(request, "shop/placeorder.html", {"add":add, "sum":sum, "total":total, "cart_items":cart_items})

def paymentdone(request):
	user = request.user
	cust_id = request.GET.get('custid')
	customer = Customer.objects.get(id=cust_id)
	cart_item = Cart.objects.filter(user=user)
	for c in cart_item:
		OrderPlaced(customer=customer, items=c.item).save()
		c.delete()
	return redirect("orders")

def orders(request):
	user = request.user
	customer = Customer.objects.get(user=user)
	orders = OrderPlaced.objects.filter(customer=customer)
	return render(request, "shop/orders.html", {"orders":orders})

def cartshow(request):
	user = request.user
	cart = Cart.objects.filter(user=user)
	if cart:
		return render(request, "shop/show_cart.html", {"cart":cart})
	return render(request, "shop/emptycart.html")

def removecart(request):
	pass