from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session
        
        # Get the current sessions key if it exists
        cart = self.session.get('session_key')
        
        # if the user is new, no session key! Create one!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        # Make sure is cart is available at all pages
        self.cart = cart
    
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        
        if product_id in self.cart:
            pass 
        else:
            # self.cart[product_id] = {'price' : str( product.price )}
            self.cart[product_id] = int(product_qty)
            
            self.session.modified = True 
            
    def __len__(self):
        return len(self.cart) 
    
    def get_prods(self):
        #Get ids for cart
        product_ids = self.cart.keys()
        #use the id to look product in database 
        products = Product.objects.filter(id__in=product_ids)
        
        # Returns those looked products 
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities