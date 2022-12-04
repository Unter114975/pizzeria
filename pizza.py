from _datetime import datetime

class AbstractPizza():
    title = ''
    dough = ''
    sauce = ''
    filing = ''
    price = 0
    SysTime = datetime.today()

    def __init__(self, title, dough, sauce, filing, price, SysTime):
        self.title = title
        self.dough = dough
        self.sauce = sauce
        self.filing = filing
        self.price = price
        self.SysTime = SysTime

    def time(self, startTime):
        pass

class PepperoniPizza(AbstractPizza):
    title = 'Пеперони'
    dough = 'Дрозжевое'
    sauce = 'Томатный'
    filing = 'Помидоры, оливки, колбаса, перец'
    price = 400
    cooking_time = 20

    def __str__(self):
        indredient = 'Пицца ' + PepperoniPizza.title + '\nСостав пиццы: ' + '\nТесто - ' + PepperoniPizza.dough \
        + '\nСоус - ' + PepperoniPizza.sauce + '\nНачинка - ' + PepperoniPizza.filing
        return indredient


class BarbecuePizza(AbstractPizza):
    title = 'Барбекю'
    dough = 'Дрозжевое'
    sauce = 'Барбекю '
    filing = 'Помидоры, оливки, куриная грудка'
    price = 450
    cooking_time = 20

    def __str__(self):
        indredient = 'Пицца ' + BarbecuePizza.title + '\nСостав пиццы: ' + '\nТесто - ' + BarbecuePizza.dough \
                     + '\nСоус - ' + BarbecuePizza.sauce + '\nНачинка - ' + BarbecuePizza.filing
        return indredient


class SeafoodPizza(AbstractPizza):
    title = 'Дары моря'
    dough = 'Слоёное'
    sauce = 'Майонез'
    filing = 'Помидоры, осьминог, креветки, мидии'
    price = 450
    cooking_time = 25

    def __str__(self):
        indredient = 'Пицца ' + SeafoodPizza.title + '\nСостав пиццы: ' + '\nТесто - ' + SeafoodPizza.dough \
                     + '\nСоус - ' + SeafoodPizza.sauce + '\nНачинка - ' + SeafoodPizza.filing
        return indredient