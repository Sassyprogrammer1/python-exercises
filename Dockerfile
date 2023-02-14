FROM python:3.9-alpine

WORKDIR /app

COPY stringify.py .
# COPY requirements.txt /app

RUN pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run when starting the container
CMD ["python", "stringify.py"]