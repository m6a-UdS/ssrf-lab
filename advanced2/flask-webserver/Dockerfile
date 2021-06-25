FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y apache2 \
    libapache2-mod-wsgi \
    build-essential \
    python \
    python-dev \
    python-pip
RUN apt-get install -y telnet
RUN apt-get clean
RUN apt-get autoremove
RUN rm -rf /var/lib/apt/lists/*

# Copy over and install the requirements
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade "pip < 21.0"
RUN pip install -r /requirements.txt

# Copy over the apache configuration file and enable the site
COPY ./ssrf-app.conf /etc/apache2/sites-available/ssrf-app.conf
RUN a2ensite ssrf-app
RUN a2enmod headers

# Copy over the wsgi file
COPY ./backend/SSRFApp/ /var/www/SSRFApp/SSRFApp/
COPY ./backend/SSRFApp.wsgi /var/www/SSRFApp/SSRFApp.wsgi
COPY ./frontend/ /var/www/html

RUN a2dissite 000-default.conf
RUN a2ensite ssrf-app.conf

EXPOSE 80

WORKDIR /var/www/SSRFApp

CMD  /usr/sbin/apache2ctl -D FOREGROUND
