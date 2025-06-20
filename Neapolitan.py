class Neapolitan:
    def __init__(self, name, age, level_of_fun):
        self.name= name
        self.age = age
        self.level_of_fun = level_of_fun
    
    def fun(self):
        print("Youre soo funny ヾ(≧▽≦*)o")

    def presentation(self):
        print(f"Hello, her name is {self.name} she is {self.age} years old and her level of fun is {self.level_of_fun}")
    
    def saludar(self):
        print("HIIIIIII ILLAAAA")

illa = Neapolitan("My little Illa 😍", 18, 999999999999999999999999999999999999999999)

illa.presentation()
