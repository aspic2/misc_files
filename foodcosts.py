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

    def print_cpu(self):
        print("%s costs $%.2f per %s" % (self.name, self.pkgcost/self.upp, self.units))


class Meal(object):
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.price = 0

    def makemeal(self):
        ingredients = self.ingredients
        print("-" * 50, "\nMaking %s..." % self.name)
        print("%s contains the following ingredients and quantities:" % self.name)
        print(ingredients)
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
lunchmeat = Food('lunchmeat', 5.99, 'slice', 32)
pepperoni = Food('pepperoni', 4, 'slice', 70)
chobani_flip = Food('Chobani Flip', 1.33, '1oz', 5.3)
chobani_tub = Food('Chobani Tub', 5.49, '1oz', 32)


highlife = Food('Miller Highlife', 6.99, '12oz', 12)
budlight = Food('Bud Light', 9.99, '12oz', 15)
z_dust = Food('Zombie Dust', 14.99, '12oz', 6)
troublesome = Food('Off Color Troublesome', 8.99, '12oz', 6)

flip_yogurt_bfast = Meal('2 Chobani Flips')
flip_yogurt_bfast.ingredients = {'Chobani Flip': 10.6}

tub_yogurt_bfast = Meal('Chobani Yogurt')
tub_yogurt_bfast.ingredients = {'Chobani Tub': 10.6}

wheat_sandwich = Meal('wheat sandwich')
wheat_sandwich.ingredients = {'wheat bread': 4, 'cheese': 2, 'lunchmeat': 4}

raisinbread_sandwich = Meal('raisin bread sandwich')
raisinbread_sandwich.ingredients = {'raisin bread': 4, 'cheese': 2, 'lunchmeat': 4}

hh = Meal('hamburger helper')
hh.ingredients = {'ground beef': 1/5, 'milk': 2/5, 'hamburger helper mix': 1/5}

grilled_cheese = Meal('grilled cheese')
grilled_cheese.ingredients = {'wheat bread': 4, 'cheese': 2, 'pepperoni': 6}



highlife.print_cpu()
z_dust.print_cpu()
troublesome.print_cpu()
budlight.print_cpu()

#wheat_sandwich.makemeal()
#raisinbread_sandwich.makemeal()
#tub_yogurt_bfast.makemeal()
#flip_yogurt_bfast.makemeal()
hh.makemeal()
grilled_cheese.makemeal()
