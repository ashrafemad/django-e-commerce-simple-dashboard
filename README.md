# Django Simple E-Commerce Dashboard (Structure)

This is a simple dashboard for an e-commerce `no templates or APIs added` just a Django-Jet Dashboard

Please note that this project was supposed to be live for a client so you may find unuseful fields/admin structure

# Who can use this?

Actually, you can only use this while practising on building django models/admin
also you can use this if you need a quick/ready models so you can start building your templates or APIs easily


``` This project can be deployed to heroku by just adding postgres configurations instead of SQLite like this: ```

`DATABASES = {'default': dj_database_url.config(default=dj_database_url.config('postgres://XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'))}`


` This app has i18n enabled (Arabic / English) with translations added`


# What is included?

1- Cutomers App:
  - Customer info
  
  - Seller Info
  
  - Customer/Seller Payments

2- Expenses App:
  
  - Other Expenses info
  
  - Other Revenues info
  
  - Insurance info (bussiness matter)

3- Orders App: 
  
  - Containing Customers/Sellers orders / Order items

4- Reports App (supposed to be a big one if the work continued hehe..)
  
  - Containing just a view showing all needed data for a date range

5- Settings App:
  
  - Should contain all required configurations (Such as Starting Balance, Project Version ...etc)

6- Stock App:
  
  - Contains Products Management (Categories, Product Details, Product Attributes) 
  
  PS: `i tried to follow django-oscar product hierarchy`
  
# How to run it
1- Create a Python3 Virtual Environment and activate it

2- install requirements `pip install -r requirements.txt`

3- run migrations `python manage.py migrate`

4- Create a superuser account to access the dashboard `python manage.py createsuperuser`

5- `python manage.py runserver` TADAAA


Feel free to ask anything, modify anything :)
