#Create a product class with attributes price, name, description
class product:
    def __init__(self,name,description,unit_price,qty,net_price):
        self.name=name
        self.description=description
        self.unit_price=unit_price
        self.qty=qty
        self.net__price=net_price
    def product_info(self):
        return f"{self.name} with the following properties"
p1=product("laptop","Gaming laptop",2)