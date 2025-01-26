# Use Python 3.10 as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port Django runs on (default 8000)
EXPOSE 8000

# Set the default command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
