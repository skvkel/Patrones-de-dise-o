from abc import ABC, abstractmethod


class PizzaBuilder(ABC):
    """ This is the interface that include all methods that implementations must implement """

    @abstractmethod
    def set_size(self, size): raise NotImplementedError

    @abstractmethod
    def set_cheese(self, cheese): raise NotImplementedError

    @abstractmethod
    def set_toppings(self, toppings): raise NotImplementedError

    @abstractmethod
    def build(self): raise NotImplementedError


class CustomPizzaBuilder(PizzaBuilder):
    """ This is a concrete builder that implement the interface """

    def __init__(self):
        self.pizza = {}

    def set_size(self, size):
        """ Set the size of the pizza """

        self.pizza['size'] = size
        return self

    def set_cheese(self, cheese):
        """ Set the cheese of the pizza """

        self.pizza['cheese'] = cheese
        return self

    def set_toppings(self, toppings):
        """ Set the toppings of the pizza """

        self.pizza['toppings'] = toppings
        return self

    def build(self):
        return self.pizza


class PizzaDirector:
    """ This is a director to automatize the creations """

    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def make_vegetarian_pizza(self):
        """ This method creates a vegetarian pizza """

        return self.builder.set_size("medium").set_cheese("mozzarella").set_toppings(["tomato", "pepper"]).build()

    def make_pepperoni_pizza(self):
        """ This method creates a pepperoni pizza """

        return self.builder.set_size("large").set_cheese("cheddar").set_toppings(["pepperoni"]).build()

##############
# Without Director
##############

# Instance the builder
builder = CustomPizzaBuilder()
custom_pizza = (
    builder
    .set_size("large")  # First step
    .set_cheese("mozzarella")   # Second step
    .set_toppings(["mushroom", "pepperoni"])    # Third step
    .build()    # Build
)
print("Custom Pizza:", custom_pizza)


##############
# With Director
##############

# Instance director with last builder
director = PizzaDirector(CustomPizzaBuilder())
# Create a vegetarian pizza
vegetarian_pizza = director.make_vegetarian_pizza()
pepperoni_pizza = director.make_pepperoni_pizza()

print("Vegetarian Pizza:", vegetarian_pizza)
print("Pepperoni Pizza:", pepperoni_pizza)



