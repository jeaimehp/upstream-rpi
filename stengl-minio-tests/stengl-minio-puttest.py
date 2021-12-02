#######################################
# Progam Name: stengl-minio-puttest.py
# Written By: Je'aime Powell (jpowell@tacc.utexas.edu)
# Original Date: 12/2/21
# Language: Python3
# Purpose: This progam is to be used on UPSTREAM-RPI
#    sensors to test if the unit can write to the 
#    TACC Corral filesystem remotely.
#    Corral Path from Stampede2: /corral/utexas/Stengl-Wyer-Remote-S/S3/sensor-test-logs/
#
# !!!NOTE BEFORE UPLOADING TO REPOSITORY!!!
# Be sure to censor the access and secret keys from the "MiniIO API Setup" Section if written in clear text!
#
# Tested Platforms:
#    - MacOS
#    - RPI400 with Raspbian Buster (32-bit)
#	
# Required Libraries:
#    os - builtin 
#    minio - Installed with "pip3 install minio"
#    dotenv - Installed with "pip3 install python-dotenv"
#
# Usage: "python3 stengl-minio-puttest.py"
#
# Example output:
#    jhpowell@jhpowell-mbp21 stengl-minio-tests % python3 stengl-minio-puttest.py
#    Sensor filename: test-jhpowell-mbp21.local
#    Buckets found:
#    [Bucket('sensor-test-logs'), Bucket('upstream-recordings')]
#
#    Copying [putting] the testfile from this computer to the bucket sensor-test-logs
#    Done copying.
#
#    Listing all objects (files/directories) now found in bucket sensor-test-logs
#    test-jhpowell-mbp21.local
#    Removing local test file: test-jhpowell-mbp21.local
#    
#    All Done!
########################################

from minio import Minio
import os

# Importing API keys from .env file
# Ref: Tutorial https://www.youtube.com/watch?v=YdgIWTYQ69A
# Ref: Dot-env library: https://github.com/theskumar/python-dotenv

from dotenv import load_dotenv
# Imports enviromental variables
load_dotenv() 

# Commands to get output for the test file
hostname_cmd = "hostname"
date_cmd = "date"

hostname_txt = os.popen(hostname_cmd).read()
date_txt = os.popen(date_cmd).read()
testfilename = "test-"+hostname_txt.strip()
print("Sensor filename:",testfilename)

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

# Create a test file
with open(testfilename, 'wb') as file_data:
  file_data.write(date_txt.encode('utf-8'))
  file_data.write(hostname_txt.encode('utf-8'))
file_data.close()

# Print the available buckets
print("Buckets found:")
print(client.list_buckets())
print(" ")
 
# Put the test file in the "sensor-test-logs" bucket
print("Copying [putting] the testfile from this computer to the bucket sensor-test-logs")
client.fput_object('sensor-test-logs', testfilename, testfilename)
print("Done copying.\n")

# Print Objects (files) in the "sensor-test-logs" bucket
print("Listing all objects (files/directories) now found in bucket sensor-test-logs")
objects = client.list_objects("sensor-test-logs", prefix='/')
for obj in objects:
  print(obj.object_name) 

# Cleanup by removing the test file
print("Removing local test file:",testfilename)
os.remove(testfilename)

# Done statement
print("\nAll Done!")
