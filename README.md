# livingarchive
Wagtail Living Archive
# Place install notes here - how to setup Wagtail server

#setup virtual environment
python -m venv env
# activating in windows
.\env\Scripts\activate

source env/bin/activate for Mac

python.exe -m pip install --upgrade pip (to upgrade)

pip install -r requirements.txt

python -m pip install --upgrade pip setuptools wheel //upgrade basic
# or Purge the broken cache and reinstall without using it
pip cache purge
python -m pip install --no-cache-dir -r requirements.txt

add .env file to livingarchive/settings/ with API_KEY= (to be sent)

# To update database
python manage.py makemigrations
python manage.py migrate 
python manage.py runserver

# Email setup
DEFAULT_FROM_EMAIL ="Living Archive <bhagwatithakuri77@gmail.com>"
EMAIL_HOST_USER = 'bhagwatithakuri77@gmail.com'
EMAIL_HOST_PASSWORD = 'tjyp zofa pfaw vmmc'
# Create Superuser
Python manage.py createsuperuser //input yourself

# Wagtail Superuser
Username=Wagtail
Password=Wagtail1


