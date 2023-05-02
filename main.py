def one():
    class restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.name = restaurant_name
            self.type = cuisine_type
        def describe_restaurant(self):
            print(f"Название ресторана: {self.name}")
            print(f"Тип кухни: {self.type}")
        def open_restaurant(self):
            print("Ресторан открыт")

    newRestaurant = restaurant("KFC", "Быстрое питание")
    print(newRestaurant.name)
    print(newRestaurant.type, "\n")
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def two():
    class restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.name = restaurant_name
            self.type = cuisine_type
        def describe_restaurant(self):
            print(f"Название ресторана: {self.name}")
            print(f"Тип кухни: {self.type}")

    newRestaurant = restaurant("KFC", "Быстрое питание \n")
    newRestaurant2 = restaurant("ТОКИО-CITY", "Восточная кухня \n")
    newRestaurant3 = restaurant("Pepela", "Европейская кухня")

    newRestaurant.describe_restaurant()
    newRestaurant2.describe_restaurant()
    newRestaurant3.describe_restaurant()

def three():
    class restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating=3): # 0 - подойдет больше, особенно при 3 ресторанах
            self.name = restaurant_name
            self.type = cuisine_type
            self.rating = rating
        def describe_restaurant(self):
            print(f"Название ресторана: {self.name}")
            print(f"Тип кухни: {self.type}")
            print(f"Рейтинг: {self.rating} \n")
        def new(self):
            self.rating = float(input('Введите новое значение рейтинга: '))
            print(f"Название ресторана: {self.name}")
            print(f"Тип кухни: {self.type}")
            print(f"Рейтинг обновлен: {self.rating} \n")

    newRestaurant = restaurant("KFC", "Быстрое питание" )
    # newRestaurant2 = restaurant("ТОКИО-CITY", "Восточная кухня")
    # newRestaurant3 = restaurant("Pepela", "Европейская кухня")

    newRestaurant.describe_restaurant()
    # newRestaurant2.describe_restaurant()
    # newRestaurant3.describe_restaurant()

    newRestaurant.new()
    # newRestaurant2.new()
    # newRestaurant3.new()

# one()
# two()
# three()