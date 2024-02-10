class Shopping:
    def __init__(self,name):
        self.name=name
        self.cart=[]

    def add_to_cart(self,item,price,quantity):
        product={'item':item,'price':price,'quantity':quantity}
        self.cart.append(product)

    def remove_item(self,item):
        target=item
        for i in range(len(self.cart)):
            if self.cart[i]['item']==target:
              #  ans+=i['price']*i['quantity']
                del self.cart[i]
                break
            
    
    def check_out(self,amount):
        total=0
        for item in self.cart:
            total+=item['price']*item['quantity']
       ## total-=self.remove_item()
        
        if amount < total:
            print(f'Please provide {total -amount} more')
        else:
            extra = amount - total
            print(f'Here is your items and extra money: {extra}')


swapan = Shopping('Alan Swapon')
swapan.add_to_cart('alu', 50, 6)
swapan.add_to_cart('dim', 12, 24)
swapan.add_to_cart('rice', 50, 5)
#print(swapan.cart)
#[{'item': 'alu', 'price': 50, 'quantity': 6}, {'item': 'dim', 'price': 12, 'quantity': 24}, {'item': 'rice', 'price': 50, 'quantity': 5}]
swapan.remove_item('dim')
print(swapan.cart)
#[{'item': 'alu', 'price': 50, 'quantity': 6}, {'item': 'rice', 'price': 50, 'quantity': 5}]


#swapan.check_out(600)
""" total price 838
Please provide 238 more """
swapan.check_out(1600)

"""total price 838
Here is your items and extra money: 762 """
#after remove_item: Here is your items and extra money: 1050