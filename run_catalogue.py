from flask import Flask, render_template, send_from_directory, request
import json
import os

app = Flask(__name__)

# Define the path to your JSON file
json_file = 'your_folder_here.json'

@app.route('/', methods=['GET', 'POST'])
def home():
    # Load the JSON data
    with open(json_file, 'r', encoding='utf-8') as f:
        items = json.load(f)

    return render_template('index.html', items=items)

@app.route('/<path:filename>')
def custom_static(filename):
    # Define the path to your images
    image_path = os.path.join(os.getcwd(), json_file.split('.')[0])

    return send_from_directory(image_path, filename)

if __name__ == '__main__':
    app.run(debug=True)