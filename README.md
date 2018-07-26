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

Technologies used

**Django:** an application framework written in Python. After installing the basic Django starter project and creating a Django app called Api, we modified the Api app files as follows:

- Models
  - Created a class that contains a representation of the database structure.
  - [List of possible fields](https://docs.djangoproject.com/en/2.0/ref/models/fields/)
  
- Serializers
  - Created a class that converts SQLite data, as gathered by the Model, into Python datatypes. 
  - [More info on serializers](http://www.django-rest-framework.org/api-guide/serializers/)
 
- View
  - View receives Python data from the Serializer, and is where we can filter and manipulate that data
  - [More info on views](https://docs.djangoproject.com/en/2.0/topics/http/views/)
  
- URLs
  - Connects a url to a view. When a URL matches a defined string in urls.py, the corresponding View runs. 
  - [More info on urls](https://docs.djangoproject.com/en/2.0/topics/http/urls/)
  
While Django can normally serve HTML, we're using the **Django REST** framework to serve JSON for use alongside an app. 

**Serializers, Views, and URLs** are importing from the Django REST framework. Namely, the Serializers and Views classes inherit from Django REST, and URLs router uses a Django REST router. 
