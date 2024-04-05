# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install the required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Expose port 5006 for the Panel app
EXPOSE 5006

# Start the Panel app
CMD ["panel", "serve", "app.py", "--allow-websocket-origin=*"]
