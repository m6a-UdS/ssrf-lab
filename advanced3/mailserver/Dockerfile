FROM ubuntu:16.04

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install postfix

COPY main.cf /etc/postfix/main.cf

COPY ./run.sh /run.sh
RUN chmod +x /run.sh
CMD ["/run.sh"]

EXPOSE 25
