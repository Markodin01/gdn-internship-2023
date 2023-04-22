# Set the arch to amd64 for linux
FROM --platform=linux/amd64  alpine:3.10

# Set base image (host OS)
FROM python:3.8-alpine

# By default, listen on port 8080
EXPOSE 8080/tcp

# Set the working directory in the container
WORKDIR /

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD [ "sh", "-c", "python api/services/app.py"] 