# Hacker news API project

A simple Django project which utilizes the Hacker news API and exposes custom API enpoints to perform CRUD operations. Requests are scheduled to be sent every 5mins and results are synced with a postgres database.

# Live Site
https://hackernews-lus1.onrender.com/

# Repo
https://github.com/de-marauder/Hacker-Newz

# API Endpoints
| URLs   |      Supported HTTP verbs      |
|----------|:-------------:|
| https://ROOTURL/api/v0/posts | GET |
| https://ROOTURL/api/v0/post/:id | GET POST PUT DELETE  |

<br>

# Installation guide
using python3.7 download pip or python-poetry
NOTE: Run all the commands below at the root of the project using a terminal or git bash preferrably for windows
## Using poetry (preferred)
navigate to the root of the project and run the poetry.py script
```sh
python3 ./poetry.py
```
Add the poetry command to your PATH by running this command
```sh
export PATH=${PATH}:${HOME}/.local/bin
```
Note this only works for present terminal session you'll have to add it to your shell config file to be permanent
Run the command `poetry --version` to verify installation
Then activate a virtual environment using poetry
```sh
poetry shell
```

Install dependencies
```sh
poetry install
```

Migrate your database
```sh
python3 manage.py makemigrations
python3 manage.py makemigrations newz # creates migrations for the newz app
python3 manage.py migrate
```

Start up your local server
```sh
python3 manage.py runserver
```


## Using pip
If you have python3 installed on your system then chances are that you already have pip.
Create a virtual environment and activate it
```sh
python3 -m virtualenv <env-name>
source <path-to-env-name>/bin/activate # For linux users
<path-to-env-name>/source/activate # For windows users
```
Install dependencies
```sh
pip install -r requirements.txt
```

Migrate your database
```sh
python3 manage.py makemigrations
python3 manage.py makemigrations newz # creates migrations for the newz app
python3 manage.py migrate
```

Start up your local server
```sh
python3 manage.py runserver
```



## Creator: de-marauder
[linkedin](https://linkedin.com/in/obiajulu-ezike)
<br>
[twitter](https://twitter.com/De_marauder)
