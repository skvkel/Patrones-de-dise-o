from abc import (
    ABC,
    abstractmethod
)


class PizzaBuilder(ABC):

    @abstractmethod
    def reset(self): raise NotImplementedError

    @abstractmethod
    def set_size(self, size): raise NotImplementedError

    @abstractmethod
    def set_crust(self, crust): raise NotImplementedError

    @abstractmethod
    def set_cheese(self, cheese): raise NotImplementedError

    @abstractmethod
    def set_sauce(self, sauce): raise NotImplementedError

    @abstractmethod
    def add_topping(self, topping): raise NotImplementedError

    @abstractmethod
    def build(self): raise NotImplementedError


class ClassicPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.pizza = {
            "type": "Classic",
            "size": None,
            "crust": None,
            "cheese": None,
            "sauce": None,
            "toppings": [],
        }
        return self

    def set_size(self, size):
        self.pizza['size'] = size
        return self

    def set_crust(self, crust):
        self.pizza['crust'] = crust
        return self

    def set_cheese(self, cheese):
        self.pizza['cheese'] = cheese
        return self

    def set_sauce(self, sauce):
        self.pizza['sauce'] = sauce
        return self

    def add_topping(self, topping):
        self.pizza['toppings'].append(topping)
        return self

    def build(self):
        return self.pizza


class GourmetPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.pizza = {
            "type": "Gourmet",
            "size": None,
            "crust": None,
            "cheese": None,
            "sauce": None,
            "toppings": [],
            "premium_ingredients": []
        }
        return self

    def set_size(self, size):
        self.pizza['size'] = size
        return self

    def set_crust(self, crust):
        self.pizza['crust'] = crust
        return self

    def set_cheese(self, cheese):
        self.pizza['cheese'] = cheese
        return self

    def set_sauce(self, sauce):
        self.pizza['sauce'] = sauce
        return self

    def add_topping(self, topping):
        self.pizza['toppings'].append(topping)
        return self

    def add_premium_ingredient(self, ingredient):
        self.pizza['premium_ingredients'].append(ingredient)
        return self

    def build(self):
        return self.pizza


class VeganPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.pizza = {
            "type": "Vegan",
            "size": None,
            "crust": "integral",
            "cheese": "queso vegano",
            "sauce": "tomate",
            "toppings": [],
        }
        return self

    def set_size(self, size):
        self.pizza['size'] = size
        return self

    def set_crust(self, crust): pass

    def set_cheese(self, cheese): pass

    def set_sauce(self, sauce):
        self.pizza['sauce'] = sauce
        return self

    def add_topping(self, topping):
        self.pizza['toppings'].append(topping)
        return self

    def build(self):
        return self.pizza


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def make_margherita(self):
        return self.builder.reset().set_size("medium").set_crust("thin").set_cheese("mozzarella").set_sauce(
            "tomato").build()

    def make_bbq_chicken(self):
        return self.builder.reset().set_size("big").set_crust("bug").set_cheese("mozzarella").set_sauce(
            "bbq").add_topping("chicken").add_topping("onion").build()

    def make_veggie(self):
        return self.builder.reset().set_size("big").add_topping("onion").build()

    def make_truffle_gourmet(self):
        return self.builder.reset().set_size("medium").set_crust("thin").set_cheese("gorgonzola").set_sauce(
            "cream").add_premium_ingredient("oil").build()

