from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return "<h1>Welcome to My Flask App</h1><p>This is the home page.</p>"

# About page route
@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This Flask app is a simple example.</p>"

# Form page route
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Get data from form
        name = request.form.get('name')
        return f"<h1>Hello, {name}!</h1><p>Thank you for submitting the form.</p>"
    return '''
        <form method="POST" action="/form">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name" required>
            <button type="submit">Submit</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
