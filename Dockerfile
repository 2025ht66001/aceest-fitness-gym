# Use a Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the ftness code file into the container at /app
COPY ACEest_Fitness.py .

# The app uses Tkinter, which relies on X11 libraries. Install these dependencies.
RUN apt-get update && apt-get install -y libxext6 libxrender1 libxtst6 && rm -rf /var/lib/apt/lists/*

# Run the command to start the app
CMD ["python", "ACEest_Fitness.py"]
