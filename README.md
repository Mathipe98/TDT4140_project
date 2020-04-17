# SellYo'Shit

[![platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey)](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/52/-/commits/master)
[![python version](https://img.shields.io/badge/python-3.7-blue)](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/52/-/commits/master)
[![django version](https://img.shields.io/badge/django-3.0.2-blue)](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/52/-/commits/master)
[![size](https://img.shields.io/badge/size-128%20kB-blue)](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/52/-/commits/master)
[![license](https://img.shields.io/badge/license-MIT-green)](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/52/-/commits/master)
[![coverage](https://img.shields.io/badge/coverage-82%25-yellowgreen)](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/52/-/commits/master)
[![pipeline](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/52/badges/master/pipeline.svg)](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/52/-/commits/master)

SellYo'Shit is an application for selling your things online, written in Python 3.7 using the Django framework.


## Motivation

This group project is developed for the NTNU course [TDT4140 Software Engineering](https://www.ntnu.edu/studies/courses/TDT4140) during the spring of 2020.


## Features

- Establish your own account
- Create and publish your own ads
- Browse and search for ads of your interest
- Contact and communicate with sellers
- Rate other sellers in the application

## Code style
- [PEP8](https://www.python.org/dev/peps/pep-0008/) conventions for Python code
- [PEP257](https://www.python.org/dev/peps/pep-0257/) conventions for docstrings documentation

Additionally, the [Inspection checklist](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/52/uploads/9ee820e5ca3316d6f3dc375178e39e10/Inspection_checklist.pdf) is used to control specific standards related to this product before merge. 

## Prerequisites

Download and install the latest version of [Python](https://www.python.org/downloads/) (version 3.7 or newer).

Download and install the latest version of [Git](https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/).


## Installation

### 1. Cloning the repository and creating a virtual environment

The source code of the application is hosted at [GitLab](https://gitlab.stud.iie.ntnu.no/tdt4140-2020/52). Download the project repository and enter it by running the following commands in your preferred shell (CMD/PowerShell in Windows, Bash in Mac/Linux):

```
git clone https://gitlab.stud.idi.ntnu.no/tdt4140-2020/52.git
cd 52
```

Input your GitLab username and password if prompted. The [pip](https://pypi.org/project/pip/) and [venv](https://docs.python.org/3/library/venv.html) modules should be included in the default Python installation. Create a virtual environment and activate it:

Windows
```
python -m venv myvenv
myvenv\Scripts\activate
```

Linux/Mac
```
python3 -m venv myvenv
source myvenv/bin/activate
```

Ensure that you're using the latest version of PIP, install Django and other project dependencies and navigate into the source folder:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
cd src
```

### 2. Configuration of the database

You can either connect to the preconfigured database created on the NTNU server or connect to your own database.

**Connecting to the preconfigured database**

To use this configuration you must have access to a [NTNU user account](https://innsida.ntnu.no/wiki/-/wiki/English/Create+a+user+account). 

1. Authenticate use of NTNU servers by connecting through NTNU's [VPN](https://innsida.ntnu.no/wiki/-/wiki/English/Install+vpn).
2. Input **vpn.ntnu.no** in the Cisco AnyConnect text field, click Connect. 
3. Input your NTNU user credentials, and click OK and Accept.


**Connection to your own database**

Your database must use MySQL or SQLite in order to work with this product. 

1. Navigate to `default.py` located in `src/pu/settings`
2. Modify the dictionary `DATABASES = {}` according to your own database settings. More specific instructions can be found [here](https://docs.djangoproject.com/en/3.0/ref/settings/#databases).
3. Run the following command in your virtual environment to configure your database with the product:
```
python manage.py migrate
```

### 3. Creating a system administrator
Generate a Django "superuser" with all administrator permissions:

```
python manage.py createsuperuser
```

Input desired admin username and password when prompted, and confirm the password. This superuser is also initiated as an administrator account for the application website.

### 4. Running the server
Next, run the Django server:

```
python manage.py runserver
```

### 5. Accessing the application web page
Finally, open your preferred browser and go to the locally hosted web page by entering the following URL in the address bar:
```
http://127.0.0.1:8000/
```

## Tests

If you're still running the server, press CTRL-BREAK inside the shell to quit. 

Run the Django test suite to validate the implementation of each module:

```
python manage.py test <directory>
```

Replace `<directory>` with the module name (`ads`, `contact`, `login`, `search`, `sellyoshit`, `stats`, or `users`). If you want to test all modules, simply leave `<directory`> empty.

Be aware that running the tests without being connected to a database will cause errors. If you are using the preconfigured database you must also be connected to NTNU's [VPN](https://innsida.ntnu.no/wiki/-/wiki/English/Install+vpn) in order to run the tests.


## Usage

### Adding a default advertisement image

Add an image with the file name `default.png` into the folder `src/media/ads`. This image will be shown for each advertisement if no picture is added by the seller.

### Adding database categories

Run the following commands in order to activate the interactive Python Console and create advertisement categories for the application:

```
python manage.py shell
from ads.models import Category
Category.objects.create(name=<category name>)
```

Replace `<category name>` with your desired category name. Run the last line for each category to be added. 

You can also add categories by using the Django administrator panel with this URL:
```
http://127.0.0.1:8000/admin/ads/category
```

## Contributors

The following students have contributed to this project:

- Alf Berger Husem ([alfbhu@stud.ntnu.no](mailto:alfbhu@stud.ntnu.no))
- Giske Naper Freberg ([giskenf@stud.ntnu.no](mailto:giskenf@stud.ntnu.no))
- Mathias Pettersen ([mathipe@stud.ntnu.no](mailto:mathipe@stud.ntnu.no))
- Mathias Sørensen ([mathiaws@stud.ntnu.no](mailto:mathiaws@stud.ntnu.no))
- Simon Blindheim ([simon.blindheim@ntnu.no](mailto:simon.blindheim@ntnu.no))
- Sivert Hognes ([siverhog@stud.ntnu.no](mailto:siverhog@stud.ntnu.no))
- Thor-Herman van Eggelen ([theggele@stud.ntnu.no](mailto:theggele@stud.ntnu.no))


## License

This project uses the [MIT](https://choosealicense.com/licenses/mit/) license.
