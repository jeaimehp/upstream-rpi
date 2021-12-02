import os
from minio import Minio

# Importing API keys from .env file
# Ref: Tutorial https://www.youtube.com/watch?v=YdgIWTYQ69A
# Ref: Dot-env library: https://github.com/theskumar/python-dotenv

from dotenv import load_dotenv
# Imports enviromental variables
load_dotenv()

#######################################
# MiniIO API setup                    #
#######################################
# !!!NOTE BEFORE UPLOADING TO REPOSITORY!!!
# Be sure to censor the access and secret keys from the "MiniIO API Setup" Section if written in clear text!
# This example uses python-dotenv for this purpose with the SERVER, ACCESS_KEY, and SECRET_KEY set in an .env file
# in the same directory as this python file with the format:
#
# SERVER = "server_url:port"
# ACCESS_KEY = "key_for_user"
# SECRET_KEY = "secret_for_user"
#
# If using git/github ensure the .gitignore has ".env" so as to not include it in uploads
#
######################################

# These can be changed to clear text but it is not recommended
SERVER = os.getenv("SERVER")
ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")


client = Minio(SERVER, ACCESS_KEY, SECRET_KEY)

# Print the available buckets
print("Buckets found:")
buckets = client.list_buckets()
print(buckets)

# Print Objects (files) in the buckets

for bucket in buckets:
  print("\n----------")
  print(f"Bucket \"{bucket.name}\" files/directories (objects) found.")
  print("FILE NAME \t| FILE SIZE(bytes) \t| LAST MODIFIED DATE")
  print("-----------------------------------------------------------")
  objects = client.list_objects(bucket.name, prefix='/')
  for obj in objects:
    print(f"{obj.object_name} \t {obj.size} \t {obj.last_modified}")
