class food_item(object):
    def __init__(self , name , calories , protein , carbohydrates , fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat
apple = food_item(60 , 0.3 , 15 , 0.5)
bread = food_item(80 , 3 , 15 , 1)
chicken_breast = food_item(165 , 31 , 0 , 3.6)
rice = food_item(200 , 4 , 45 , 0.5)
chocolate = food_item(230 , 2 , 25 , 13)
milk = food_item(120 , 8 , 12 , 5)
def calculate_nutrition(items_list):
    calories = 0
    protein = 0
    carbohydrates = 0
    fat = 0
    for food in items_list:
        calories += food.calories
        protein += food.protein
        carbohydrates += food.carbohydrates
        fat += food.fat
    return calories , protein , carbohydrates , fat
items_list = [apple , bread , chicken_breast , rice , chocolate , milk]
calories , protein , carbohydrates , fat = calculate_nutrition(items_list)
print(f"The total calories that an individual has consumed over a 24 hr period are {calories}.")
print(f"The total protein that an individual has consumed over a 24 hr period is {protein} g.")
print(f"The total carbohydrates that an individual has consumed over a 24 hr period are {carbohydrates} g.")
print(f"The total fat that an individual has consumed over a 24 hr period is {fat} g.")
if calories > 2500 or fat > 90:
    print("Warning")