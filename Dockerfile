# 
FROM python:3.9


WORKDIR /home

# 
COPY requirements.txt requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
COPY . .

#port
EXPOSE 80

# 
RUN ["python" , "manage.py", "makemigrations"]

#
RUN ["python" , "manage.py", "migrate"]

#
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
