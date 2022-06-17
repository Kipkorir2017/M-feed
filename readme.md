## M-feed
# Application description
    enable organizations and institutions to adopt data driven decision making in identifying gaps and areas of need in curriculum development and implementation.
.

    admin does the management.

# Setup process
* Clone this repository using the link from the clone button
* Open the downloaded folder in a text editor of your preference
# To install virtual environment:
* python3.10 -m venv --without-pip virtual
# Activate virtual environment
* source virtual/bin/activate
# Install latest pip version inside virtual environment
* curl https://bootstrap.pypa.io/get-pip.py | python
# Installing the dependencies
* pip install -r requirements.txt
# Starting up the application
* python3 manage.py runserver

Navigation
Open port *http://127.0.0.1:8000/ * to interact with the application
To access the admin site go to:*http://127.0.0.1:8000/admin *
The api endpoints:*http://127.0.0.1:8000/api *
Swagger:*http://127.0.0.1:8000/swagger *
Technologies Used
PYTHON
DJANGO 4.0.5 
HTML5
POSTGRESQL
MARKDOWN for the README.md file
License
<a href="">MIT License</a>