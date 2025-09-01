# Stage 1: Build stage for running tests
FROM python:3.9-slim as builder

# Set the working directory
WORKDIR /app

# Copy application and test files
COPY ACEest_Fitness.py .
COPY test_ACEest_Fitness.py .

# Run the unit tests. If tests fail command will 
# exit with non zero code thus failing the build
RUN python -m unittest -v test_ACEest_Fitness.py



# Stage 2: Final image for the application
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install Tkinter dependencies for GUI
RUN apt-get update && apt-get install -y libxext6 libxrender1 libxtst6 && rm -rf /var/lib/apt/lists/*

# Copy only the application file from the builder stage
COPY --from=builder /app/ACEest_Fitness.py .

# Command to run the application
CMD ["python", "ACEest_Fitness.py"]
