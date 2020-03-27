# SellYoShit

SellYoShit is an application for selling your things online, written in Python 3.7 using the Django framework.

## Installation

Download and install the latest version of [Python](https://www.python.org/downloads/) (version 3.7 or newer).

Download and install the latest version of [Git](https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/).

The source code of the application is hosted at [Gitlab](https://gitlab.stud.iie.ntnu.no/tdt4140-2020/52). Download the project repository and enter it by running the following commands in your preferred shell (CMD/PowerShell in Windows, Bash in Mac/Linux):

```bash
git clone https://gitlab.stud.idi.ntnu.no/tdt4140-2020/52.git
cd 52
```

Input your GitLab username and password if prompted. The [pip](https://pypi.org/project/pip/) and [venv](https://docs.python.org/3/library/venv.html) modules should be included in the default Python installation. Create a virtual environment and activate it:

Windows
```bash
python -m venv myvenv
myvenv\Scripts\activate
```

Linux/Mac
```bash
python3 -m venv myvenv
source myvenv/bin/activate
```

Ensure that you're using the latest version of PIP, and install Django and other project dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Authenticate use of GitLab servers by connecting through NTNU's [VPN](https://innsida.ntnu.no/wiki/-/wiki/English/Install+vpn). Input **vpn.ntnu.no** in the Cisco AnyConnect text field, click Connect, input your NTNU user credentials, and click OK and Accept.


Next, run the Django server:

```bash
cd src
python manage.py runserver
```

Lastly, open your preferred browser and go to the locally hosted web page by entering:
```bash
http://127.0.0.1:8000/
```
