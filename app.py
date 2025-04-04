from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
recipes = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipes', methods=['GET', 'POST'])
def recipes_page():
    global recipes
    if request.method == 'POST':
        title = request.form.get('title')
        ingredients = request.form.get('ingredients')
        category = request.form.get('category')
        instructions = request.form.get('instructions')
        recipes.append({
            'title': title,
            'ingredients': ingredients,
            'category': category,
            'instructions': instructions
        })
        return redirect(url_for('recipes_page'))
    search = request.args.get('search')
    filtered = recipes
    if search:
        search_lower = search.lower()
        filtered = [r for r in recipes if search_lower in r['ingredients'].lower() or search_lower in r['category'].lower()]
    return render_template('main.html', recipes=filtered)

if __name__ == '__main__':
    app.run(debug=True)