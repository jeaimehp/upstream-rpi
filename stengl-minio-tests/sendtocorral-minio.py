#######################################
# Progam Name: sendtocorral-minio.py
# Written By: Je'aime Powell (jpowell@tacc.utexas.edu)
# Original Date: 12/2/21
# Language: Python3
# Purpose: This progam is to be used on UPSTREAM-RPI
#    writes the given file to the  
#    TACC Corral filesystem remotely and then verifies.
#    Corral Path from Stampede2: /corral/utexas/Stengl-Wyer-Remote-S/S3/
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
#    sys - builtin
#    minio - Installed with "pip3 install minio"
#    dotenv - Installed with "pip3 install python-dotenv"
#
# Usage: "python3 sendtocorral-minio.py filepath/filename"
#
# Example output:
#    pi@raspberrypi-dev:~/upstream/stengl-minio-tests $ python3 sendtocorral-minio.py /home/pi/upstream/sound/1638493265.wav
#    Copying [putting] the /home/pi/upstream/sound/1638493265.wav from this computer into the bucket upstream-recordings
#    Done copying.
#
#    Checking for 1638493265.wav in the bucket upstream-recordings
#
#    FILE NAME 	| FILE SIZE(bytes) 	| LAST MODIFIED DATE 	| MD5 CHECKSUM
#    -----------------------------------------------------------
#    1638493265.wav 	 1764044 	 2021-12-03 02:01:30.370000+00:00 	 762beb5f700f26346723756002b37e55
#
#    Checking File Sizes and MD5 Checksum's between the local and remote versions of 1638493265.wav
#    Local ---> 1638493265.wav size: 1764044 	 MD5: 762beb5f700f26346723756002b37e55
#    Remote --> 1638493265.wav size: 1764044 	 MD5: 762beb5f700f26346723756002b37e55
#    Looks Good!
#
#    All Done!
########################################

from minio import Minio
import os
import sys

bucketName = 'upstream-recordings'
envPath = '/home/pi/upstream/stengl-minio-tests/.env'

if len(sys.argv) < 2:
  print("\nERROR: Filename and Path Needed \nUSAGE: python3 sendtocorral-minio.py path/to/file/filename\n")
  sys.exit()
elif os.path.exists(sys.argv[1]) == False:
  print("\nERROR: File does not exist \nUSAGE: python3 sendtocorral-minio.py path/to/file/filename\n")
  sys.exit()

fileName = sys.argv[1]

# Importing API keys from .env file
# Ref: Tutorial https://www.youtube.com/watch?v=YdgIWTYQ69A
# Ref: Dot-env library: https://github.com/theskumar/python-dotenv

from dotenv import load_dotenv
# Imports enviromental variables
load_dotenv(dotenv_path=envPath) 


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

# Put the test file in the identified bucket
print(f"Copying [putting] the {fileName} from this computer into the bucket {bucketName}")
client.fput_object(bucketName, os.path.split(fileName)[1], fileName)
print("Done copying.\n")

# Print Objects (files) in the bucket
print(f"Checking for {os.path.split(fileName)[1]} in the bucket {bucketName}")
objects = client.list_objects(bucketName, prefix='/')

# This bit of code checks the bucket for the uploaded file then shows the size of the local verses the remote file
foundFile = False
for obj in objects:
  if obj.object_name == os.path.split(fileName)[1]:
    foundFile = True
    print("\nFILE NAME \t| FILE SIZE(bytes) \t| LAST MODIFIED DATE \t| MD5 CHECKSUM")
    print("-----------------------------------------------------------")
    print(f"{obj.object_name} \t {obj.size} \t {obj.last_modified} \t {obj.etag}")
    
    # Comparing sizes between local and remote files
    print(f"\nChecking File Sizes and MD5 Checksum's between the local and remote versions of {os.path.split(fileName)[1]}")
    localFileMD5 = os.popen("md5sum %s" %fileName).read()
    print (f"Local ---> {os.path.split(fileName)[1]} size: {os.path.getsize(fileName)} \t MD5: {localFileMD5.split()[0]}")
    print (f"Remote --> {os.path.split(fileName)[1]} size: {obj.size} \t MD5: {obj.etag}")
    if os.path.getsize(fileName) == obj.size and localFileMD5.split()[0] == obj.etag:
      print("Looks Good!")
      
    else:
        print("WARNING: THE LOCAL AND REMOTE FILES ARE DIFFERENT!!")
        foundFile = False
if foundFile == False:
  print(f"ERROR: Could not find {os.path.split(fileName)[1]} in the remote bucket {bucketName} or the local and remote versions do not match")
  print("\n## THE TRANSFER FAILED ##\n")

# Done statement
print("\nAll Done!")
