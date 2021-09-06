FROM python:3.9.0

WORKDIR /home/
# home 이라는 경로에 모든 git 파일 붙혀넣음
RUN git clone https://github.com/Wolf0605/wolf_class5_janggo.git

WORKDIR /home/wolf_class5_janggo/

RUN pip install -r requirements.txt
# 개발하는 한경과 저 환경을 매칭

RUN python manage.py migrate