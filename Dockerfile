# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files
RUN python vaikystes_lobiai/manage.py collectstatic --noinput

# Expose port 8000 to the host
EXPOSE 8000

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=vaikystes_lobiai.settings

# Run gunicorn server
CMD ["gunicorn", "vaikystes_lobiai.wsgi:application", "--bind", "0.0.0.0:8000"]
