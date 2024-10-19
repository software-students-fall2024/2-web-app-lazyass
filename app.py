from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


# Initialize MongoDB
mongo = PyMongo(app)


# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# User class for authentication
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id


@login_manager.user_loader
def load_user(user_id):
    # This function should query the MongoDB to find the user
    user_data = mongo.db.users.find_one({"_id": user_id})
    if user_data:
        return User(user_id=user_id)
    return None


# Routes for the app
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_data():
    if request.method == 'POST':
        # Get data from form
        data = request.form.get('data')
        # Insert data into MongoDB
        mongo.db.mycollection.insert_one({"data": data})
        flash('Data added successfully!')
        return redirect(url_for('view_data'))
    return render_template('add_data.html')


@app.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit_data(id):
    if request.method == 'POST':
        # Update data in MongoDB
        new_data = request.form.get('data')
        mongo.db.mycollection.update_one({"_id": id}, {"$set": {"data": new_data}})
        flash('Data updated successfully!')
        return redirect(url_for('view_data'))
    # Fetch data to edit
    data = mongo.db.mycollection.find_one({"_id": id})
    return render_template('edit_data.html', data=data)


@app.route('/delete/<id>', methods=['POST'])
@login_required
def delete_data(id):
    mongo.db.mycollection.delete_one({"_id": id})
    flash('Data deleted successfully!')
    return redirect(url_for('view_data'))


@app.route('/view')
def view_data():
    data_list = mongo.db.mycollection.find()
    return render_template('view_data.html', data_list=data_list)


@app.route('/search', methods=['GET', 'POST'])
def search_data():
    if request.method == 'POST':
        search_term = request.form.get('search')
        # Query MongoDB with the search term
        search_results = mongo.db.mycollection.find({"data": {"$regex": search_term}})
        return render_template('search_data.html', results=search_results)
    return render_template('search_data.html', results=[])


if __name__ == '__main__':
    app.run(debug=True)