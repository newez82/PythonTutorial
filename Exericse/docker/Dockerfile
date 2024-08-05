# Docker file provides instructions document out deployment process

# FROM is start from the base image, like import keyword in java / python
# in the scenario, it start from node image that build on top of alpine linux
# platform
FROM node:alpine

# Copy our application or program files
# Copy all the file from current (.) directory into /app directory
# into that image. the image has a file system, we are going to create
# a directory called app inside that file system.
COPY . /app

WORKDIR /app

# Use Command instruction to execute the command, we need to put /app/app.js
# if the WORKDIR didnt specific above
CMD node app.js