# SellYo'Shit

[![pipeline status](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/52/badges/master/pipeline.svg)](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/52/-/commits/master)
[![coverage report](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/52/badges/master/coverage.svg)](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/52/-/commits/master)
<!-- repo size --> 
<!-- language distribution --> 
<!-- code style pep8 --> 
<!-- contributors --> 
<!-- number of commits --> 
<!-- license --> 

SellYo'Shit is an application for selling your things online, written in Python 3.7 using the Django framework.


## Motivation

This group project is developed for the NTNU course [TDT4140 Software Engineering](https://www.ntnu.edu/studies/courses/TDT4140) during the spring of 2020.


## Features

- Establish your own account
- Create and publish your own ads
- Browse and search for ads of your interest
- Contact and communicate with sellers
- Rate other sellers in the application


## Prerequisites

Download and install the latest version of [Python](https://www.python.org/downloads/) (version 3.7 or newer).

Download and install the latest version of [Git](https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/).


## Installation

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

## Tests

Run the Django test suite to validate the implementation of each module:

```
python manage.py test <directory>
```

Replace `<directory>` with the module name (`ads`, `contact`, `login`, `search`, `sellyoshit`, `stats`, or `users`).


## Usage

### Adding a default advertisement image

Add an image with the file name `default.png` into the folder `src/media/ads`. This image will be shown for each advertisement if no picture is added by the seller.

### Connecting to GitLab

Authenticate use of GitLab servers by connecting through NTNU's [VPN](https://innsida.ntnu.no/wiki/-/wiki/English/Install+vpn). Input **vpn.ntnu.no** in the Cisco AnyConnect text field, click Connect, input your NTNU user credentials, and click OK and Accept.


### Running the server

Next, run the Django server:

```
python manage.py runserver
```

### Adding database categories

Run the following commands in order to activate the interactive Python Console and create advertisement categories for the application:

```
py manage.py shell
from ads.models import Category
Category.objects.create(name=<category name>)
```

Replace `<category name>` with your desired category name. Run the last line for each category to be added.


### Accessing the application web page

Finally, open your preferred browser and go to the locally hosted web page by entering the following URL in the address bar:
```
http://127.0.0.1:8000/
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
