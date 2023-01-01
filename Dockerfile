# 
FROM python:3.9


WORKDIR /home

# 
COPY requirements.txt requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
COPY . /home

# 
CMD ["python", "manage.py", "make_migrations", " &&" , "python", "manage.py", "migrate", "&&","python", "manage.py", "runserver", "0.0.0.0:80"]
