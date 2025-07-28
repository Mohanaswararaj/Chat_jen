# Base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit's default port
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
