# adminService
This is the admin service for the project. It is a RESTful service to manage the products and categories.:

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
You need to have installed:
* Python 3.9
* pip
* virtualenv
* MySQL
* Docker
* Docker-compose
* rabbitmq

### Installing
1. First, you need to clone the repository:

    ```git clone```

2. Then, you need to create a virtual environment:

    ```python -m venv venv```

3. Activate the virtual environment:

    ```source venv/bin/activate```
4. Run
    
    ```Docker-compose build```
5. Run
    
    ```Docker-compose up```
6. Open another terminal and run
    
    ```docker-compose exec db bash```
7. In the container, run
    
    ```mysql -u root -p```
8. Create the database
    
    ```CREATE DATABASE admin;```
