# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app

# Expose the Streamlit default port
EXPOSE 8501

# Command to run the Streamlit app when the container starts
CMD ["streamlit", "run", "app.py"]
