FROM centos

RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
      && yum update -y

COPY requirements.txt .

RUN yum install -y python-pip \
      && pip install -r requirements.txt


COPY . src/

EXPOSE 8080

CMD ["python","/src/app.py"]
