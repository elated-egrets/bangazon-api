# Bangazon
Welcome to the bangazon repository.

## Developer Resources

The following are the endpoints and http methods included in this API:

### Order
1. GET (single order)
   - /order/<user_id>
   - GET a single JSON object back with the proper information.
       - NOTE: This should return a nested list of all products in the order, and details for each product.
1. GET (List)
   - /order/
   - returns a list of current orders.
1. POST
   - Create a new order.
   - /order/
1. PUT
   - Edit existing order.
   - /order/<order_id>
   - All keys and fields required to edit.
1. DELETE
   - /order/<order_id>
   - Delete from the Order table and cascade where necessary.
   - Sets Foreign Key on Order products to Null.

### Payment
1. GET (single)
   - /payment/<payment_id>
   - Get a single payment type
   - Payment type has the following resources
     - name (str) user defined short description of the payment type
     - payment_type (str) either card or bank account
     - account_number (int) number for card or bank account
     - expiration (date) expiration for cards
     - security_code (int) security code for cards
     - user_id (int, FK) references to user who registered the payment type
1. GET (list)
   - /payment/
   - Returns a list of all payment types 
3. POST
   - creates a new payment type
4. PUT
   - updates information about a payment type
5. DELETE
   - Safe Delete, payment should be masked from general queries, but still be accessible by primary key lookup
   - Deleting a payment type will make it no longer be listed in a general query for payment types on /api/payment
   - Individual deleted payment types are still accessible by primary key lookup on path /api/payment/[id] where id is the integer id for the payment type object
6. Routes
   - Payment type lives on the route /api/payment from the root directory of the project. 
   - Detailed view (as well as PUT, DELETE methods) can be requested from route /api/payment/[id] where id is the integer id for the payment type object


### Product
1. GET (Single Item)
   - /product/<id>
   - returns a JSON object with a single product
1. GET (List)
   - User should be able to GET a list, and GET a single item.
   - returns an array of objects
1. POST
   - Create a new product
   - /product/
1. PUT
   - Edit an existing product
   - /product/<id>
   - All keys are required when editing
1. DELETE
   - Safe cascade delete from intersection table
   - /product/<id>

### Product Category
1. GET (Single Item)
   - /category/<category_id>
   - returns a JSON object with a single category
1. GET (List)
   - /category/
   - returns a list of categories as an array of objects
1. POST
   - Create a new product
   - /category/
1. PUT
   - Edit an existing product
   - /category/<id>
   - All keys are required when editing
1. DELETE
   - /category/<id>
   - Deletes from Category table
   - Sets Foreign Key of deleted category on products to NULL

###Users
1. GET (single user)
   - /users/<user_id>
   - sends back: 
     JSON object: id, first_name, last_name, date_created, active, password, email
1. GET (list of all users)
   - [#11](https://github.com/elated-egrets/bangazon-api/projects/2#card-11583296) On querying for users who have never made a purchase
   - /users/
   - sends back: returns an array of JSON objects
1. POST
   - /users/
   - creates a new user
1. PUT
   - /users/<user_id>
   - all fields are required: first_name, last_name, password, email






## project structure
The django project is the root directory of this repo. The 'Bangazon' directory is the parent project configuration, and django apps should be siblings of that directory.

## virtual environment
Create a pip virtual environment as a sibling of this repo in your own file system. The following packages are required for working on this project.
1. django
2. djangorestframework
3. django-safedelete
4. arrow

### steps to create virtual environment
1. cd into the directory you wish the environment to live (this should be outside your git repo)
1. run the following commands
```
virtualenv [name_of_environment]
```

### steps to activate environment
to resume development and reactivate your virtual env
1. cd into directory in which you created the environment
1. run the following command
```
source [name_of_environment]/bin/activate
```
1. you should now be in your virtual environment

## style conventions
1. All directories should not have the first letter capitalized. 'models', 'views', etc...
2. All files should be in lower case snake case. user_view.py, product_serializer.py etc...

## Apps

### API
This project is the API for bangazon developers. It contains the following resources
1. Users
2. Products
3. Categories
4. Orders
5. Payment options

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
