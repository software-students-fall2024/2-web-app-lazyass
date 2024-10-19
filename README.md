# Web Application Exercise

A little exercise to build a web application following an agile development process. See the [instructions](instructions.md) for more detail.

## Product vision statement
This web application allows users to manage and manipulate data with functionalities to add, edit, delete, view, and search entries in a MongoDB database, providing a simple and mobile-friendly user experience.


## User stories

1\. As a user, I want to add data to the application so that I can store information for later use.

2\. As a user, I want to view all stored data so that I can see what has been saved.

3\. As a user, I want to edit existing data so that I can update information when needed. 

4\. As a user, I want to delete data that I no longer need. 

5\. As a user, I want to search for specific data so that I can quickly find what I am looking for.

6\. As an admin, I want to secure access to certain functionalities so that only authenticated users can perform data modifications.

## Steps necessary to run the software

### Prerequisites
- Python 3.x
- MongoDB
- `pip` for managing Python packages


1. **Clone the repository:**
   ```bash
   https://github.com/software-students-fall2024/2-web-app-lazyass.git
   cd 2-web-app-lazyass




2. **Create a virtual environment (recommended):**
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


3. **Install the required packages:**
pip install -r requirements.txt


4. **Create a .env file in the root directory with the following contents:**
MONGO_URI=mongodb://yourusername:yourpassword@localhost:27017/yourdbname
SECRET_KEY=your_secret_key

Replace yourusername, yourpassword, and yourdbname with your actual MongoDB credentials.

5. **Run the application:**
python app.py


6. **Open a web browser and navigate to:**
http://127.0.0.1:5000/


## Task boards
（no team)
