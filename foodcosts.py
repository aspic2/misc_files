#calculate the cost of foods / consumable goods for comparison
'''
meat_sandwich = bread, meat, cheese
pbj_sandwich = bread, peanutbutter, jelly

xhamburger_helper = ground_beef, milk, hh_mix

grilled_cheese = bread, cheese, pepperoni
'''

class Food(object):

    foods = {}

    def __init__(self, name, pkgcost, units_per_pkg):
        self.name = name
        self.pkgcost = pkgcost
        self.upp = units_per_pkg
        self.cost_per_unit = self.pkgcost / self.upp
        Food.foods[self.name] = self.cost_per_unit

    def print_cost_per_meal(self):
        print("%s costs $%d per meal" % (self.name, self.unitcost/self.mpu))

class Meal(object):
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.price = 0

    def makemeal(self):
        ingredients = self.ingredients
        price = self.price
        for i in ingredients:
            ingredients.append(i)
        for i in ingredients:
            price += Food.foods[i]
        return price






ground_beef = Food('ground beef', 5.6, 1)
milk = Food('milk', 2.5, 16)

#dishes I am uncertain about
wheat_bread = Food('wheat bread', 1.2, 20)
raisinbread = Food('raisin bread', 2, 16)
cheese = Food('cheese', 2.5, 11)
lunchmeat = Food('lunchmeat', 5.99, 24)
pepperoni = Food('pepperoni', 4, 30)


print(Food.foods)

wheat_sandwich = Meal('wheat sandwich')
wheat_sandwich.ingredients = 'wheat bread', 'cheese', 'lunchmeat'

raisinbread_sandwich = Meal('raisin bread sandwich')
raisinbread_sandwich.ingredients = 'raisin bread', 'cheese', 'lunchmeat'

print(wheat_sandwich.ingredients)
wheat_sandwich.makemeal
print(wheat_sandwich.price)
