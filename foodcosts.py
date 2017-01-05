#calculate the cost of foods / consumable goods for comparison

#should meals be different classes or different instances of the class meals?


class Food(object):

    foods = {}

    def __init__(self, name, pkgcost, units, units_per_pkg):
        self.name = name
        self.pkgcost = pkgcost
        self.units = units
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
        print("-" * 50, "\nMaking %s..." % self.name)
        print("%s contains the following ingredients and quantities:" % self.name)
        print(self.ingredients)
        for i in ingredients:
            self.price += Food.foods[i] * self.ingredients[i]
        print("-" * 25, "\nThis dish costs $%.2f per meal" % self.price)




ground_beef = Food('ground beef', 5.6, 'lbs', 1)
milk = Food('milk', 2.5, 'cups', 16)
hhmix = Food('hamburger helper mix', 1.5, 'box', 1)
#dishes I am uncertain about
wheat_bread = Food('wheat bread', 1.2, 'slice', 20)
raisinbread = Food('raisin bread', 2, 'slice', 16)
cheese = Food('cheese', 2.5, 'slice', 11)
lunchmeat = Food('lunchmeat', 5.99, 'slice', 24)
pepperoni = Food('pepperoni', 4, 'slice', 30)


wheat_sandwich = Meal('wheat sandwich')
wheat_sandwich.ingredients = {'wheat bread': 4, 'cheese': 2, 'lunchmeat': 4}

raisinbread_sandwich = Meal('raisin bread sandwich')
raisinbread_sandwich.ingredients = {'raisin bread': 4, 'cheese': 2, 'lunchmeat': 4}

hh = Meal('hamburger helper')
hh.ingredients = {'ground beef': .25, 'milk': .25, 'hamburger helper mix': .25}

grilled_cheese = Meal('grilled cheese')
grilled_cheese.ingredients = {'wheat bread': 4, 'cheese': 2, 'pepperoni': 6}


#wheat_sandwich.makemeal()
#raisinbread_sandwich.makemeal()
hh.makemeal()
grilled_cheese.makemeal()
