FROM python:3.9.0

WORKDIR /home/

RUN echo 'wolfowlfowlf'
# home 이라는 경로에 모든 git 파일 붙혀넣음
RUN git clone https://github.com/Wolf0605/wolf_class5_janggo.git

WORKDIR /home/wolf_class5_janggo/

# 개발하는 한경과 저 환경을 매칭

RUN echo "SECRET_KEY=django-insecure-62cxbw+*g^rmt%_6a0eh6i1kvkd1sw2_sc^@*q1u$tlloo=*@$"> .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "wolfs_jango_project.wsgi", "--bind", "0.0.0.0:8000"]