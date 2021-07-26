# Alert Messenger

# Getting Started

The following steps will set up the project. Alert messages are user specific. 
Hence user level authentications are created. In order to provision a new user please run the below command

python manage.py createsuperuser

If you want to create more users, the admin panel will comes in handy usin the above created username / password

The alert messages can be created in two methods
1. Through the admin panel                                                                                                                 
2. Call api                                                                                         

# Requirements

Python3                                                                                                                     
Django==3.1.7                                                                                                                     
djangorestframework==3.12.2                                                                                                         

# Installation

Clone this repository : git clone https://github.com/Neema-francis/alert-messenger.git                                                                                               

Install pip.                                                                                                                   
Install pip-virtualenv.                                                                                                                        

python3 -m venv <virtual name> : python3 -m venv env_messenger                                                                       
Activate virtual : Source env_messenger/bin/activate                                                                            

cd into alert_messenger: cd alert_messenger.                                                                                                  

Install all packages mentioned in the requirements.txt : pip install -r requirements.txt                                                            

python manage.py createsuperuser

Run : python manage.py runserver
