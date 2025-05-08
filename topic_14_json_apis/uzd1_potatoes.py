import requests
from collections import Counter
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog
 
 
# Funkcija, lai iegūtu receptes no API
def get_recipes(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Kļūda API: {response.status_code}")
        return None
 
# Funkcija, lai atrastu receptes, kuru tags satur ingredient
def find_recipes_with_ingredient(recipes, ingredient):
    return [
        recipe for recipe in recipes
        if any(ingredient.lower() in tag.lower() for tag in recipe.get('ingredients', []))
    ]
 
# Funkcija, lai iegūtu visas receptes ar kartupeļiem - saturot "potato"
def get_potato_recipes(recipes):
    return find_recipes_with_ingredient(recipes, "potato")
 
# Funkcija, lai iegūtu visas zupu receptes
#zupas ir tās, kurām kādā no tags ir vērtība Soup
def get_soup_recipes(recipes):
    return [recipe for recipe in recipes if 'Soup' in recipe.get('tags', [])]
 
# Funkcija, lai iegūtu sarakstā visus ingredientus no receptēm
def get_all_ingredients(recipes):
    all_ingredients = []
    for recipe in recipes:
        all_ingredients.extend(recipe['ingredients'])
    return all_ingredients
 
# Funkcija, lai iegūtu visbiežāk sastopamos ingredientus
def get_top_ingredients(ingredients, top_n=5):
    counter = Counter(ingredients)
    return counter.most_common(top_n)
 
# Funkcija, lai uzzīmētu histogrammu top 10 ingredientiem
def plot_top_ingredients(ingredients, top_n=10):
    counter = Counter(ingredients)
    most_common = counter.most_common(top_n)
    labels, values = zip(*most_common)
 
    plt.bar(labels, values)
    plt.xlabel('Ingredients')
    plt.ylabel('Count')
    plt.title(f'Top {top_n} Ingredients')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
 
# Funkcijas, kas meklē recepti pēc nosaukuma
def search_recipe_by_name(recipes, name):
    return [recipe for recipe in recipes if name.lower() in recipe['name'].lower()]
 
#Izsaukt receptes no API
# API URL
api_url = "https://dummyjson.com/recipes"
# Iegūstam receptes
recipes_data = get_recipes(api_url)
 
# izdrukājam kartupeļu, zupu receptes, top 5 ingredientus un histogrammu
if recipes_data:
    # Iegūstam kartupeļu receptes
    potato_recipes = get_potato_recipes(recipes_data['recipes'])
    print(f"Kartupeļu receptes ({len(potato_recipes)}):")
    for recipe in potato_recipes:
        print(f"- {recipe['name']}")
 
    # Izdrukājam zupu receptes
    soup_recipes = get_soup_recipes(recipes_data['recipes'])
    print(f"\nZupu receptes ({len(soup_recipes)}):")
    for recipe in soup_recipes:
        print(f"- {recipe['name']}")
 
    # Iegūstam visus ingredientus
    all_ingredients = get_all_ingredients(recipes_data['recipes'])
 
    # Iegūstam top 5 ingredientus
    top_ingredients = get_top_ingredients(all_ingredients, top_n=5)
    print("\nTop 5 ingredients:")
    for ingredient, count in top_ingredients:
        print(f"- {ingredient}: {count}")
 
    # Uzzīmējam histogrammu ar top 10 ingredientiem
    plot_top_ingredients(all_ingredients, top_n=10)
 
# Izveidojam vienkaŗšu dialogu, lai ievadītu meklēto ēdienu
def search_recipe():
    root = tk.Tk()
    root.withdraw()  # Paslēpjam galveno logu
    recipe_name = simpledialog.askstring("Meklēt recepti", "Ievadiet ēdiena nosaukumu:")
    if recipe_name:
        found_recipes = search_recipe_by_name(recipes_data['recipes'], recipe_name)
        if found_recipes:
            print(f"\nReceptes ar '{recipe_name}':")
            for recipe in found_recipes:
                print(f"- {recipe['name']} - {recipe['ingredients']} - {recipe['instructions']}")
        else:
            print(f"\nNav atrastas receptes ar '{recipe_name}'.")
    root.destroy()
 
# Izsaucam meklēšanas funkciju
search_recipe()