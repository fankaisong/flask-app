# flask-template
A web template using flask framework

This app demonstrates simple CRUD operations and the purpose of this website is to record grocery price for users to keep track of price changes and comparison



## Installation

The app uses Python3 and all packages can be installed using

```bash
pip install -r requirements.txt
```

## Setup the database in MYSQL

In **config.py** file, 
- change *SQLALCHEMY_DATABASE_URI="mysql://username:password@server/db"* to link to your MYSQL
- change the secret key **SECRET_KEY = "this is the key"**
- Under **application** directory, run following command to create database
```python
from app import db
db.create_all()
```


## Run app

``` bash
Python3 app.py
```

**Login Page:**
![Pages](images/img1.png)




**Create a user**
![Pages](images/img2.png)


**Upload or search** 
![Pages](images/img3.png)
