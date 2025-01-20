# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /appl
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run the Streamlit app
CMD ["streamlit", "run", "appl.py", "--server.port=8080", "--server.address=0.0.0.0"]
