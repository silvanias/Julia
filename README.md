<h1 align="center">
  <a href="https://github.com/sikorosenai/Julia">
    <img src="docs/images/Screenshot 2023-04-12 at 10.07.32.png" alt="Logo" width="240" height="100">
  </a>
</h1>

<div align="center">
  Julia
  <br />
  <a href="#about"><strong>Checkout the screenshots »</strong></a>
  <br />
  <br />
</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)

</details>

---

## About

> Julia is a website which allows users to create accounts and then uniquely pair coloured renders of the mandelbrot set to said account.
> In the future it would be great to be able to allow a user to zoom into specific parts of the mandelbrot set.
> The website is not meant to have many practical applications, it is simply a demonstration of my technical knowledge.
<details>
<summary>Screenshots</summary>
<br>

|                               Landing Page                               |                                Generate Page                               |
| :-------------------------------------------------------------------: | :--------------------------------------------------------------------: |
| <img src="docs/images/Screenshot 2023-04-12 at 10.06.19.png" title="Landing Page" width="100%"> | <img src="docs/images/Screenshot 2023-04-12 at 10.05.51.png" title="Generate Page" width="100%">|

</details>

### Built With

The front end of the website is all done in plain HTML, CSS and JavaScript. 
The production database is saved on PostgreSQL, with the local db using SQLite. 
The rendering of the Mandelbrot set is done entirely in python with the matplotlib library used for visualisation.
All other backend functions are handled with Flask.

## Getting Started
### Prerequisites

All you need to get started is to have Python 3.10.9 or later installed on your machine.

### Install requirements

```sh
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```
### Add environment variables
Create a .env file in the root directory and add the following variables:
SECRET_KEY='changethissecretkey'
FLASK_APP='julia/main.py'
DATABASE_URL='sqlite:///database.db'
DEBUG=True
E2E_APP_PORT=5001
> To avoid a bug please also run this command:
```sh
$ export FLASK_APP=julia/main.py
``` 

### Set up db

```sh
$ flask db init
$ flask db upgrade
```

### Run the tests
```sh
$ pytest -v
```
> The tests are currently not complete, but they do test the main functionality of the website.
## Usage

> To run the website locally, run the following command:
```sh
$ gunicorn main:app
```
> The website will then be available at http://localhost:8000/, and you will be able to create an account and generate your own mandelbrot set.

## Support

If you need any help please feel free to reach out to me at the email address listed on my GitHub profile 😄.

- [GitHub issues](https://github.com/sikorosenai/Julia/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+)
- Contact options listed on [this GitHub profile](https://github.com/sikorosenai)
