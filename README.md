# Hood Eye
## Author  
  
>[Wanjiku Karanja](https://github.com/3xistentialcrisis)  
  
# Description  
This a web application that allows the User to be in the loop about everything happening in their neighborhood.  
  
##  Live Link  
 Click [View Site](https://hoodeye.herokuapp.com/)  to visit the site
  
## Screenshots 
###### Home page
 
<img src="https://raw.githubusercontent.com/3xistentialcrisis/Awards/master/static/images/.png" width="900px" height="440px">
 
###### Sign Up
 <img src="https://raw.githubusercontent.com/3xistentialcrisis/Awards/master/static/images/.png" width="900px" height="440px">

###### Login
 <img src="https://raw.githubusercontent.com/3xistentialcrisis/Awards/master/static/images/.png" width="900px" height="440px">

###### Login
 <img src="https://raw.githubusercontent.com/3xistentialcrisis/Awards/master/static/images/.png" width="900px" height="440px">

## User Story  
This app enables user to:

* Sign into the App.
* Set up a profile and a general location and their neighborhood name.
* Find a list of different businesses in their neighborhood
* Find Contact Information for the health department and Police authorities near their neighborhood.
* Create Posts that are  visible to everyone in their neighborhood.
* Change their neighborhood when they decide to move out.
* Only view details of a single neighborhood.

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/3xistentialcrisis/Hood/.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Awards pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
python3 -m venv virtual 
```  
```bash 
source virtual/bin/activate 
```

##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrations 
 ```bash 
python manage.py makemigrations awards
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python3 manage.py runserver 
``` 

##### Testing the application  
 ```bash 
 python3 manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  

## Technology used  
  
* [Python 3.8](https://www.python.org/)  
* [Django 1.11.17](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
* [Postgres](https://www.postgresql.org/)
* [Pip](https://pypi.org/project/pip/)
* Html and CSS (Bootstrap)
  
## Known Bugs  
There are no known bugs at the time of deployment of this application 
  
## CodeBeat
[![codebeat badge](https://codebeat.co/badges/61881488-2da3-4522-be01-0226f8d1a6c6)](https://codebeat.co/projects/github-com-3xistentialcrisis-hood-master) 

## License 
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/3xistentialcrisis/hood/blob/master/LICENSE)

## Contact Information   
If you have any question or contributions, please email the administrator at [administrator@hoodeye.com] 
