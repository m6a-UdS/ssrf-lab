FROM ubuntu:16.04

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install apache2
RUN apt-get -y install php libapache2-mod-php php-mcrypt

COPY www/ /var/www/html/
CMD ["apachectl", "-D", "FOREGROUND"]
EXPOSE 80 443