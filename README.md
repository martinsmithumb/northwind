# northwind
Northwind database converted to a website with visualizations
# To recreate database

1. Running the scripts below will delete all the cache and migrations folders, the db.sqlite3 file, create migrations, and then migrate.
   rmdir /s /q "orders/__pycache__"
   rmdir /s /q "orders/migrations"
   rmdir /s /q "customers/__pycache__"
   rmdir /s /q "customers/migrations"
   rmdir /s /q "employees/__pycache__"
   rmdir /s /q "employees/migrations"   
   rmdir /s /q "pages/__pycache__"
   rmdir /s /q "pages/migrations"
   rmdir /s /q "products/__pycache__"
   rmdir /s /q "products/migrations"
   rmdir /s /q "shippers/__pycache__"
   rmdir /s /q "shippers/migrations"
   del "db.sqlite3"
   python manage.py makemigrations customers employees orders pages shippers products
   python manage.py migrate
2. create new query 
3. paste in scripts from db_Scripts.sql
4. right click and run scripts

