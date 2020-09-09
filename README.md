# Team-213-A-Back-End

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/583729e1583144708378b2e8520d3c2f)](https://app.codacy.com/gh/BuildForSDGCohort2/Team-213-A-Back-End?utm_source=github.com&utm_medium=referral&utm_content=BuildForSDGCohort2/Team-213-A-Back-End&utm_campaign=Badge_Grade_Dashboard)

## Installation and Setup

### Fork the repo

You first need to fork the repo from either [Team-213-A-Back-End](https://github.com/BuildForSDGCohort2/Team-213-A-Back-End) or [Team-213-A-Front-End](https://github.com/BuildForSDGCohort2/Team-213-A-Front-End) depending on your stack.

### Clone the repo

Clone the forked repo

`git clone git@github.com:[username]/Team-213-A-Back-End.git`  
or  
`git clone git@github.com:[username]/Team-213-A-Front-End.git`

### Create a virtual environment

There are several ways depending on the OS and package you choose. Here's my favorite  
`sudo apt-get install python3-pip`  
`pip3 install virtualenv`  
Then either  
`python3 -m venv venv`  
or  
`python -m venv venv`  
or  
`virtualenv venv` (you can call it venv or anything you like)

#### Activate the virtual environment  

`source venv/bin/activate`  

### Install the requirements

Within the activated virtual environment run:

`pip3 install -r requirements.txt`  
or  
`pip install -r requirements.txt`  

#### Environment tweaks

Environment Variables are handled by `python-decouple`.  
In the same folder as `manage.py`, add a file called `.env`.  
Inside it, set the variables in this format:  

>```python
>SECRET_KEY=s3cr3tk3y
>DEBUG=True
>ALLOWED_HOSTS=127.0.0.1, .localhost, .herokuapp.com
>```

Access the variables within `settings.py`, example:  

>```python
>from decouple import config
>...
>...
>SECRET_KEY = config('SECRET_KEY')
>DEBUG = config('DEBUG', cast=bool)
>TIME_ZONE = config('TIME_ZONE')
>```

Read the [Python Decouple Documentation](https://pypi.org/project/python-decouple/) for more information.

### Run the surver locally

`python manage.py migrate`  
`python manage.py runserver`  

## Contributors

- [Tim](https://github.com/wwangwe)

## License

The project is licensed under the MIT License
