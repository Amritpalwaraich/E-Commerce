from .cart import Cart

# Create context processors so that our page can run on all pages 
def cart(request):
    # Return the default data from our cart 
    return {'cart': Cart(request)}
    