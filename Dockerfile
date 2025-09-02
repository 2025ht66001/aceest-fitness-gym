# Stage 1: Build stage for running tests
FROM python:3.9-slim as builder

# Set the working directory
WORKDIR /app

# Install Tkinter dependencies for unit tests
RUN apt-get update && apt-get install -y --no-install-recommends \
    libtk8.6 \
    tk \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Copy application and test files
COPY ACEest_Fitness.py .
COPY test_ACEest_Fitness.py .

# Run the unit tests. If tests fail command will 
# exit with non zero code thus failing the build
RUN python -m unittest -v test_ACEest_Fitness.py


# Stage 2: Final image for the application
FROM python:3.9-slim as stage-1

# Set the working directory
WORKDIR /app

# Install Tkinter dependencies for GUI
RUN apt-get update && apt-get install -y --no-install-recommends \
    libxext6 \
    libxrender1 \
    libxtst6 \
    libtk8.6 \
    tk \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Copy only the application file from the builder stage
COPY --from=builder /app/ACEest_Fitness.py .

# Since this GUI app is run on a production evronment
# with a display and in Github actions we want only to
# build an image and not run it, the entry point is 
# disabled below by commenting out. Application needs to 
# be started in the production environment after deploying. 
# CMD ["python", "ACEest_Fitness.py"]
