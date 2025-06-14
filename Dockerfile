# Dockerfile

# Use the official slim Python 3.9 image as a base.
# The 'slim' version is smaller, reducing our final image size.
FROM python:3.9-slim

# Set the working directory inside the container.
WORKDIR /code

# IMPORTANT OPTIMIZATION:
# First, copy and install only the dependency list.
# This prevents reinstalling hundreds of MBs of libraries every time we change
# our application code. Docker caches this layer.
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Now, copy our application code into the container.
COPY ./app /code/app

# Inform Docker that the application will run on port 8000.
EXPOSE 8000

# The default command to run when the container starts.
# We start the server on 0.0.0.0 to make it accessible from outside the container.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]