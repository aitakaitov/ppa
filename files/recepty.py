import os
import locale

locale.setlocale(locale.LC_NUMERIC, "cs-CZ.UTF-8")


class Ingredient:
    def __init__(self, amount: float, units: str, description: str):
        self.amount = amount
        self.units = units
        self.description = description

    def __str__(self):
        return f'{self.amount} {self.units} {self.description}'


class Recipe:
    def __init__(self, name: str, amount: int, ingredients: list[int]):
        self.name = name
        self.amount = amount
        self.ingredients = ingredients
    
    def __str__(self):
        buffer = f'{self.name} ({self.amount} porcí)\n'
        for ingredient in self.ingredients:
            buffer += str(ingredient) + '\n'
        
        return buffer

    @staticmethod
    def find_name(lines: list[str]):
        for line in lines:
            if line.startswith('#') and not line.startswith('##'):
                return line[1:].strip()
    
    @staticmethod   
    def find_amount(lines: list[str]):
        in_info = False
        for i in range(len(lines)):
            line = lines[i]          
            
            if in_info:
                if 'porce' in line:
                    _, amount = line.split(':')
                    return int(amount)

            if line.startswith('##') and not line.startswith('###'):
                if line[2:].strip().lower() == 'info':
                    in_info = True
                    continue            
    
    @staticmethod
    def find_ingredients(lines: list[str]):
        ingredients = []
        in_ingredients = False
        for line in lines:
            if line.startswith('##') and not line.startswith('###'):
                if line[2:].strip().lower() == 'suroviny':
                    in_ingredients = True
                    continue
                in_ingredients = False
            
            if in_ingredients:
                parts = line.split()
                amount = locale.atof(parts[1])
                unit = parts[2]
                name = " ".join(parts[3:])
                ingredients.append(Ingredient(amount, unit, name))


        return ingredients

    @staticmethod
    def from_file(file_path: str):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line for line in f.readlines() if line.strip() != '']

        return Recipe(
            Recipe.find_name(lines),
            Recipe.find_amount(lines),
            Recipe.find_ingredients(lines)
        )


def main(recipe_dir):
    files = os.listdir(recipe_dir)
    recipes = []
    for file in files:
        if '.md' not in file:
            continue
        recipes.append(
            Recipe.from_file(
                os.path.join(recipe_dir, file)
            )
        )
    
    for r in recipes:
        print(r)
        print()


if __name__ == '__main__':
    print(os.getcwd())
    recipe_directory = "files/data"
    main(recipe_directory)
