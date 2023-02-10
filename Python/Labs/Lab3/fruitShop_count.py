class FruitShop():

    def __init__(self, shopname, fruits):
        self.shopname = shopname
        self.fruits = fruits
    
    def get_fruits_count(self):
        return len(self.fruits)


my_shop = FruitShop("My Fruit Shop", ["Banana" , "Orange", "Kiwi", "Apple"]) 
print(my_shop.get_fruits_count())

