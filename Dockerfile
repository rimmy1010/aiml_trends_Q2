FROM python:3.9-slim
WORKDIR /q2
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY housing.py .
CMD ["python", "housing.py"]
