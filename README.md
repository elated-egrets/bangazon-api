# Bangazon
Welcome to the bangazon repository.

## project structure
The django project is the root directory of this repo. The 'Bangazon' directory is the parent project configuration, and django apps should be siblings of that directory.

## virtual environment
Create a pip virtual environment as a sibling of this repo in your own file system. The following packages are required for working on this project.
1. django
1. djangorestframework
1. django-safedelete
1. arrow

## style conventions
1. All directories should have the first letter capitalized. Models, Views, Api etc...
1. All files should be in lower case snake case. user_view.py, product_serializer.py etc...

## Apps

### API
This project is the API for bangazon developers. It contains the following resources
1. Users (to be added)
1. Products (to be added)
1. Categories (to be added)
1. Orders (to be added)
1. Payment options (to be added)

#### API file structure
The models, serializers, and views for the api should each be in a self contained file each containing only one class that deals with that aspect of the relavent model.
For Example...

For the user collection
user_model.py in Api/Models
user_serializer.py in Api/Serializers
user_view.py in Api/Views



