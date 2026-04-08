# define the class and initialize
# create instances
# define a function that calculates the nutrition
# print the output and judge if there need be a warning

class food_item(object):
    def __init__(self , name , calories , protein , carbohydrates , fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat
apple = food_item("apple" , 60 , 0.3 , 15 , 0.5)
bread = food_item("bread" , 80 , 3 , 15 , 1)
chicken_breast = food_item("chicken breast" , 165 , 31 , 0 , 3.6)
rice = food_item("rice" , 200 , 4 , 45 , 0.5)
chocolate = food_item("chocolate" , 230 , 2 , 25 , 13)
milk = food_item("milk" , 120 , 8 , 12 , 5)
def calculate_nutrition(items_list):
    """
    Input: the list of all the food items
    Return: the calculated nutrition
    """
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
if __name__ == "__main__": # ensure that the test program will only be executed when directly run this file
    items_list = [apple , bread , chicken_breast , rice , chocolate , milk]
    calories , protein , carbohydrates , fat = calculate_nutrition(items_list)
    print(f"The total calories that an individual has consumed over a 24 hr period are {calories}.")
    print(f"The total protein that an individual has consumed over a 24 hr period is {protein} g.")
    print(f"The total carbohydrates that an individual has consumed over a 24 hr period are {carbohydrates} g.")
    print(f"The total fat that an individual has consumed over a 24 hr period is {fat} g.")
    if calories > 2500 or fat > 90:
        print("Warning")