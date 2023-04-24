# Installing a python3.9 slim image
FROM python:3.9-slim
# Setting working directory
WORKDIR /app/
# Copy requirements file to image
COPY requirements.txt .
# Installing requirements
RUN pip install --no-cache-dir -r requirements.txt
# Copying root files
COPY . .
# Expose Port 3031
EXPOSE 3031
# Increasing number of open files
RUN ulimit -n 100000
# Starting the server
CMD [ "uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "3031"]