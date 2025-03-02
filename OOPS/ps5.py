class Order:
    def __init__(self,items,price):
        self.price=price
        self.items=items

    def __gt__(self,order2): #use dunder function for supports operators
        return self.price>order2.price
    
order1=Order("chips",90)
order2=Order("tea",20)

print(order1>order2)#True
print(order1>order2)#10,20---false