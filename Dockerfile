# Use a Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files
COPY . /app

# Expose the port for Flask
EXPOSE 5000

# Command to run the bot
CMD ["python", "bot.py"]
