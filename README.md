# Application-Oriented Tutor Recommendation System

## About the repository

This is the final project of the EI447 Mobile Network of SJTU. 

## About the Files

- [FeatureVector](FeatureVector): Stores some encoded feature vectors of supervisors. Here we just put a field map file as a placeholder to maintain the  directory structure.
- [FinalProject](FinalProject): The project directory, contains some settings of the project.
- [RecommendSys](RecommendSys): The app of the project, contains models and views.
- [statics](statics): Static sources.
- [templates](templates): Templates of the web.
- [manage.py](manage.py): An interface to control the project.

## How to use

Run `python ./manage.py xxx` to control the project. For more usages, please refer to [Django](https://docs.djangoproject.com/en/3.0/ref/django-admin/). Here I just list some most frequently used command.

1. `python ./manage.py runserver 0.0.0.0:8080`: run the development server on current device at port 8080.
2. `python ./manage.py makemigrations`: generate migration file of models defined.
3. `python ./manage.py migrate`: migrate django models into tables in database.



