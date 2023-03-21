#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import json
import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from cloudinary.api import delete_resources_by_tag, resources_by_tag
import configparser
config = configparser.ConfigParser()
config.read('cfg.ini')


def cloudinary_config():
	cloudinary.config(
	  cloud_name = config['CLOUDINARY']['cloud_name'],  
	  api_key = config['CLOUDINARY']['api_key'],
	  api_secret = config['CLOUDINARY']['api_secret']  
	)

def upload_person_image(imagePath,imageName,personName):
	cloudinary_config()
	imageName=os.path.splitext(imageName)[0]
	res=cloudinary.uploader.upload(imagePath, public_id = 'gpk/dataset/'+personName+'/'+imageName)

def upload_image(imagePath,imageName):
	cloudinary_config()
	imageName=os.path.splitext(imageName)[0]
	res=cloudinary.uploader.upload(imagePath, public_id = 'gpk/tmp/'+imageName)
