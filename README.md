<h1 align="center">
  <a href="https://julia-y16w.onrender.com">
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
  - [Architecture](#architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)

</details>

---

## About
Please setup the project as detailed in the getting started section and run locally (by $ gunicorn main:app). The hosting service I am using is incredibly slow, and working on bugs relating to it are not a priortity for me currently.
<br>
<br>
<a href="https://julia-y16w.onrender.com">Julia </a> is a website which allows users to create accounts and then uniquely pair coloured renders of the mandelbrot set to said account.
In the future it would be great to be able to allow a user to zoom into specific parts of the mandelbrot set.
The website is not meant to have practical applications, and is simply a fun project to test myself. The website is currently deployed, however it is highly recommended to run locally as it will avoid errors.
<details>
<summary>Screenshots</summary>
<br>

|                               Landing Page                               |                                Generate Page                               |
| :-------------------------------------------------------------------: | :--------------------------------------------------------------------: |
| <img src="docs/images/Screenshot 2023-04-12 at 10.06.19.png" title="Landing Page" width="100%"> | <img src="docs/images/Screenshot 2023-04-12 at 10.05.51.png" title="Generate Page" width="100%">|

</details>

### Built With

I am using the Python Flask framework for all handling of routing and backend logic. The front end of the website is all done in plain HTML, CSS and JavaScript. 
The production database is saved on PostgreSQL, with the development db using SQLite. 
The rendering of the Mandelbrot set is done entirely in python with the matplotlib library used for visualisation.
Anything not mentioned uses Python. <br>

I tried to experiment with a wide range of testing in this project and attempt to apply best practices in regards to the testing pyramid/mocking/coverage, and so am using a variety of technologies relating to this. 
Currently I am using pytest/unittest for all integration and unit tests, Playwright for E2E, Selenium for screenshot testing, Mutagen for mutation testing and Coverage.py for measuring the coverage of my tests.  

### Architecture
The below diagram does not show all endpoints and functions, but it does show the primary ones relating to displaying and rendering fractals.
<img src="docs/images/juliaArchitecture.drawio (1).png" title="Landing Page" width="100%"> 

  +---------------------------------------+  
  |           User Interface (HTML, CSS, JS)    |  
  +---------------------------------------+  
                          ^                  ^  
                           |                   |    
                          v                  v  
  +---------------------------------------+  
  |                          Flask App                           |  
  +---------------------------------------+  
  |                           /generate                          |   
  |                        generate() API                     |  
  |               /mandelbrot/\<query params>       |  
  |                      mandelbrot(slug)                  | <--> Renders Mandelbrot Set and returns image  
  +---------------------------------------+  
                          ^                  ^  
                           |                   |    
                          v                  v  
  +---------------------------------------+   
  |                         PostgreSQL                        |  
  +---------------------------------------+  
  |                         Users Table                        |  
  |                       Fractals Table                      |  
  +---------------------------------------+

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
> To avoid a bug please also run this command in the root directory:
```sh
$ export FLASK_APP=main.py
``` 

### Set up db

```sh
$ flask db upgrade

# Only run this next command if the first fails

$ flask db init
```

## Usage

> To run the website locally, run the following command:
```sh
$ gunicorn main:app
```
> The website will then be available at http://localhost:8000/, and you will be able to create an account and generate your own mandelbrot set.

### Run the tests
```sh
$ pytest -v
$ mutatest
$ coverage run -m pytest -v
$ coverage report -i 
```
> Make sure that you are running a local instance to allow e2e tests to interface.

## Support

If you need any help please feel free to reach out to me at the email address listed on my GitHub profile 😄.

- [GitHub issues](https://github.com/sikorosenai/Julia/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+)
- Contact options listed on [this GitHub profile](https://github.com/sikorosenai)
