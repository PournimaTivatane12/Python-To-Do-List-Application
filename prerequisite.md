1. System Requirements

Operating System: Windows, macOS, or Linux

Python Version: Python 3.8 or later

Recommended: Virtual Environment (venv)

2. Required Dependencies

Ensure you have the following dependencies installed before running the application. If not, you can install them using pip.

Python Packages:

Flask

Flask-SQLAlchemy

Flask-WTF

SQLite3 (built-in with Python)

Install Dependencies:

Run the following command to install all required dependencies:

pip install -r requirements.txt

3. Database Setup

The application uses SQLite as the database.

Ensure that instance/ directory exists for SQLite storage.

Run database migrations if needed:

flask db upgrade

4. Environment Variables

Create a .env file in the project root directory and set up the following environment variables:

FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///instance/todo.db

5. Running the Application

Once all prerequisites are met, start the application by running:

python app.py

Or using Flask CLI:

flask run

6. Additional Tools (Optional)

Git (For version control)

Postman (For testing API endpoints if applicable)



