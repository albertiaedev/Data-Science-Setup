# Data Science Setup

The Data Science Setup (DSS) is an open-source repository where you can find the initial setup that you need to start your data science path 🔬 

You'll find the source code for starting your project, plus several  CSV datasets for practising your data science skills 🤓 

Follow the next steps to clone this repo:


## Clone this repository

The first thing you need to do is to open your terminal/cmd, access to the directory where you want to keep your project, then copy and paste this code:

### HTTPS

```git clone https://github.com/jesusalberto18/Data-Science-Setup.git```

### SSH

```git clone git@github.com:jesusalberto18/Data-Science-Setup.git```

And that's it! It creates a local copy of this repository in your machine...
Or maybe you'd rather create a virtual environment for that, if so follow the instructions below.

## Create a virtual environment

### Why a virtual environment?

<em>A virtual environment helps you separate the system of your local machine from the one you need to run a specific project (similar to a virtual machine, to make it easier, but it's different). That way you avoid the problem of conflicting packages and ensure it all works well.</em>

 - Create a folder for this cloned repo by typing ```mkdir <name_of_repo>```
   i.e. ```mkdir datascience```

 - Inside your folder create the virtual environment, for this we'll need a package called ```virtualenv```,
   you can install this package by typing ```pip3 install virtualenv```

 - Create the virtual environment by typing ```python3 -m virtualenv venv```,
   then type ```source venv/bin/activate``` in order to activate your virtual environment.

 - Clone this repo following the instructions above.

 - Once inside your cloned repo, just type ```pip3 install -r requirements.txt``` to install all the dependencies needed to run this project.

 - Open a new notebook by typing ```jupyter notebook```,
   and start browwsing your files!

## Donate

<a href="https://www.paypal.com/paypalme/j2al444">
<img src="https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white" />
</a>
