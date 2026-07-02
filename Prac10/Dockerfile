FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current folder on your computer
# to the current folder inside the container
# Syntax: COPY <source> <destination>
COPY . .

# Install all Python packages listed in requirements.txt
RUN pip install -r requirements.txt

# Start the application by running python app.py
# when the container starts
CMD ["python", "app.py"]