pip install gradio

import random
import gradio as gr

# 1. Randomly generate a recipe name
def generate_recipe_name(ingredients):
    styles = ["Delight", "Surprise", "Fusion", "Treat", "Fiesta", "Heaven", "Magic", "Bliss", "Special", "Craze"]
    main_ingredient = random.choice(ingredients).capitalize()
    style = random.choice(styles)
    return f"{main_ingredient} {style}"

# 2. Generate fake instructions
def generate_instructions(ingredients):
    instructions = []
    instructions.append(f"Gather all your ingredients: {', '.join(ingredients)}.")
    instructions.append(f"Prepare the {random.choice(ingredients)} by chopping or slicing it finely.")
    instructions.append(f"Heat some oil/butter in a pan and add {random.choice(ingredients)}.")
    instructions.append(f"Add the rest of the ingredients, stir well, and cook until done.")
    instructions.append(f"Season with salt, pepper, and your favorite spices.")
    instructions.append(f"Garnish and serve hot!")
    return instructions

# 3. Fake nutrition
def generate_nutrition():
    return {
        "protein": random.randint(5, 20),
        "fat": random.randint(5, 25),
        "carbs": random.randint(10, 50)
    }

# 4. Create a single recipe
def create_recipe(ingredients):
    recipe_name = generate_recipe_name(ingredients)
    instructions = generate_instructions(ingredients)
    nutrition = generate_nutrition()

    recipe_text = f"""
    <h3 style="color: #FF6347;">🍽️ <b>{recipe_name}</b></h3>
    <p><b>Ingredients:</b> <span style="color: #8A2BE2;">{', '.join(ingredients)}</span></p>
    <h4 style="color: #32CD32;">Instructions:</h4>
    <ol style="color: #555555;">
    """
    for idx, step in enumerate(instructions, 1):
        recipe_text += f"<li>{step}</li>"
    recipe_text += f"""
    </ol>
    <h5 style="color: #FFD700;">Nutrition (estimated):</h5>
    <p>Protein: <span style="color: #FF4500;">{nutrition['protein']}g</span>, 
    Fat: <span style="color: #FF4500;">{nutrition['fat']}g</span>, 
    Carbs: <span style="color: #FF4500;">{nutrition['carbs']}g</span></p>
    <hr style="border-color: #FFD700;">
    """
    
    return recipe_text

# 5. Main Gradio interface function
def generate_recipe_book(ingredients, num_recipes):
    user_ingredients = [ingredient.strip().lower() for ingredient in ingredients.split(',')]

    if not user_ingredients:
        return "❌ No ingredients entered. Please try again."

    num_recipes = int(num_recipes)

    book_content = "<h2 style='color: #32CD32;'>📖 My AI Recipe Book</h2><br>"
    for _ in range(num_recipes):
        book_content += create_recipe(user_ingredients)
    
    return book_content

# Create the Gradio interface
iface = gr.Interface(
    fn=generate_recipe_book,
    inputs=[
        gr.Textbox(label="Enter Ingredients (comma-separated)", placeholder="e.g. tomato, onion, cheese, pasta"),
        gr.Number(value=5, label="Number of Recipes to Generate")
    ],
    outputs=gr.HTML(label="Generated Recipe Book"),
    live=True,
    title="AI Recipe Generator",
    description="Generate a custom recipe book based on your ingredients!"
)

# Launch the Gradio app
iface.launch()
