from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/submit', methods=['POST'])
def submit():
    # Handle form submission
    data = request.form.get('data')
    # Process the data as needed
    return redirect(url_for('main.home'))