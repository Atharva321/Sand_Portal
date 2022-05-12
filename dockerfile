RUN yum install git -y
RUN yum install python3 -y
RUN pip3 install django django_widget_tweaks pillow
RUN git clone --single-branch --branch sandv3 https://github.com/Atharva321/Sand_Portal.git
EXPOSE 8000

CMD ["python3","./Sand_Portal/manage.py", "runserver", "0.0.0.0:8000"]
