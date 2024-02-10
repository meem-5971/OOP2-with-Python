class Shop:
    #cart = [] # cart is a class attribute
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart=[]

    def add_to_cart(self, item):
        self.cart.append(item)

my_shop=Shop('food')
print(my_shop.add_to_cart('egg')) #None


mehzbeeeen = Shop('mehu')
mehzbeeeen.add_to_cart('shoes')
mehzbeeeen.add_to_cart('phone')
print(mehzbeeeen.cart) #['egg','shoes', 'phone']

nisho = Shop('noisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart) #['egg','shoes', 'phone', 'cap', 'watch'] aksthe print hcche