from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.

def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    return render(request, "cart_summary.html", {"cart_products": cart_products, "quantities": quantities})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get Stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        # Look up product in database
        product = get_object_or_404(Product, id=product_id)
        #Save to session 
        cart.add(product=product, quantity=product_qty)
        
        # get the quantity
        cart_quantity = cart.__len__()
        
        response = JsonResponse({'qly ': cart_quantity  })
        return response

def cart_delete(request):
    pass

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get Stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        cart.update(product=product_id, quantity=product_qty)
        
        response = JsonResponse({ 'qty' : product_qty})
        return response
        # return redirect("cart_summary")