FROM python:3.9.0

WORKDIR /home/

RUN echo 'asdfasdvdvf'
# home 이라는 경로에 모든 git 파일 붙혀넣음
RUN git clone https://github.com/Wolf0605/wolf_class5_janggo.git

WORKDIR /home/wolf_class5_janggo/

# 개발하는 한경과 저 환경을 매칭

RUN echo "SECRET_KEY=django-insecure-62cxbw+*g^rmt%_6a0eh6i1kvkd1sw2_sc^@*q1u$tlloo=*@$"> .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=wolfs_jango_project.settings.deploy && python manage.py migrate --settings=wolfs_jango_project.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=wolfs_jango_project.settings.deploy wolfs_jango_project.wsgi --bind 0.0.0.0:8000"]