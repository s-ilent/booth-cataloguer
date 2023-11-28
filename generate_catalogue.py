from flask import Flask, render_template, render_template_string
import json
import os

app = Flask(__name__)

# Define the path to your JSON file
json_file = 'your_folder_here.json'

with app.app_context():
    # Load the JSON data
    with open(json_file, 'r', encoding='utf-8') as f:
        items = json.load(f)

    # Render the template to a string
    html = render_template_string(render_template('index.html', items=items))

    # Write the string to an HTML file
    with open('output.html', 'w', encoding='utf-8') as f:
        f.write(html)
