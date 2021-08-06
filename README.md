# Welcome
=> This is a simple blog website in which user can post blogs and read other users blogs

## This project is only configured for Development build.

**======> *DO NOT USE IT ON PRODUCTION WITHOUT PROPER MEASURES* <======**

###### Instructions for using this project in Development.
- 1. Download this project, pull it or clone it. Your Choice.
- 2. Create a new python environment for this project from "python -m venv __*environment_name*__ "
- 3. Activate the virtual environment by " __*environment_name*__/Script/activate"
- 4. Run "python -m pip install -r "requirements.txt" to install all of project dependencies.
- 5. Delete the db.sqlite3 database already present in this project to start fresh.
- 6. After deleting, run migrate command to create a new SQL database.
- 7. Run "python manage.py createsuperuser" to create a new Super User.
- 8. To start the project in development server run "python manage.py runserver"
- 9. Browse to the link _http://localhost:8000/_ to access the website.
- 10. To use Forgot Password Feature You have to setup your own SMTP server.Take reference from internet to use it.

###### To use this project in production. Most important Measures are:
- 1. Set *DEBUG=False*.
- 2. Hide *SECRET_KEY*.
- 3. Hide passwords, username or any other important information in environment variables.

# This project is not licensed. Use and Modify it on your will