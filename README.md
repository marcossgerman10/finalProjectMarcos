# INF601 - Advanced Programming in Python
# Marcos German
# Final Project

# Soccer Recruitment Web Application

A web application designed to assist in managing player recruitment efficiently and effectively.

## Description

The Soccer Recruitment Web Application helps the agency to easily know if a player who is planning to study and play soccer in the US is eligible and also helps the player to upload required documents easily for the agency to manage and being able to start the process of sneding the information to the different universities and being able to receive and scholarship.

## Getting started

### Dependencies

-Python 3.10 or higher

-Django 5.1.4

-SQLite (default database)

Install dependencies using pip:
pip install -r requirements.txt

### Installing
1. Clone the repository:
git clone https://github.com/marcossgerman10/finalProjectMarcos.git

2. Navigate to the project directory:
cd finalProjectMarcos

3. Set up a virtual environment:
python -m venv .venv
source .venv/bin/activate  # For Linux/Mac
.venv\Scripts\activate    # For Windows

4. Install the required libraries:
pip install -r requirements.txt

5. Set up the database:
python manage.py migrate

6. Run the development server:
python manage.py runserver

### Executing program

1. Start the application by running:
python manage.py runserver

2. Open your browser and navigate to:
http://127.0.0.1:8000

## Usage

In the main page you can navigate through home page, soccer scholarships and about us to learn how scholarships work and information about it.
Then in the sign up button you register as a new user. Later you can sign in with the user created.
When signed in you are redirected to your dashboard page that there is a link to do a questionnaire that can later be updated in the requirements page.
Also in tasks page you are allowed to upload the required documents.

## Authors
Marcos German

## License 
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
Inspiration and resources:

- Django Documentation
- Bootstrap
- Chatgpt


