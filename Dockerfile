FROM centos:centos7
COPY . /app
RUN yum -y update; yum install -y python3; pip3 install flask; yum install -y cronie; yum clean all
RUN cp app/app/python_rest_api.service /etc/systemd/system;\
mkdir /usr/local/lib/python_service/;\
cp app/app/python_service.py /usr/local/lib/python_service/;\
systemctl enable python_rest_api.service
RUN echo "0 0 * * *  systemctl restart python_rest_api.service" | crontab -
