from flask import Flask, send_from_directory

app = Flask(__name__)

# Serve the index.html file
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve the styles.css file
@app.route('/styles.css')
def styles():
    return send_from_directory('.', 'styles.css')

# Serve the menu.json file
@app.route('/menu.json')
def menu():
    return send_from_directory('.', 'menu.json')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
