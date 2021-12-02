#!/bin/bash
echo " This script installs the required Python3 modules needed to use the included minio tests"
echo "Installing Minio"
pip3 install minio
echo "Installing DotENV"
pip3 install python-dotenv
echo " "
echo "Done!"
