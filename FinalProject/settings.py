# -*- coding: UTF-8 -*-
"""
Django settings for FinalProject project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import numpy as np
import pickle as pkl

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g1@#!#vf7^b!3o*7c2(qji3(yze$9imxoy_w=h7t&#11aq7dho'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'RecommendSys',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FinalProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+"/templates",],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'FinalProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'project',
        'USER': 'root',
        'PASSWORD': '147789qaz',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    },
    'remotedb': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'am_paper',
        'USER': 'mobilenet',
        'PASSWORD': 'mobilenet',
        'HOST': '202.120.36.29',
        'PORT': '13307',
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [ 
    os.path.join(BASE_DIR, "statics"), 
]


VECTOR_DIR = os.path.join(BASE_DIR,"FeatureVector")
FIELD_TO_VECTOR = np.load(os.path.join(VECTOR_DIR,"field2vec.npz"))
WEIGHTS = FIELD_TO_VECTOR["weight"]
BIAS = FIELD_TO_VECTOR["bias"]

FIELDS_FILE = os.path.join(VECTOR_DIR, "sort_field_count.txt")
f = open(FIELDS_FILE, "r")
lines = f.readlines()
FIELDS = []
for line in lines:
    line.rstrip("\n")
    tmp_line = line.split("\t")
    FIELDS.append(int(tmp_line[1]))
f.close()

FIELD_MAP = {}
FIELD_MAP_FILE = os.path.join(VECTOR_DIR, "fieldmap.pkl")
with open(FIELD_MAP_FILE, "rb") as f:
    FIELD_MAP = pkl.load(f)
