FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y apache2 \
    libapache2-mod-wsgi \
    build-essential \
    python \
    python-dev \
    python-pip
RUN apt-get clean
RUN apt-get autoremove
RUN rm -rf /var/lib/apt/lists/*

# Copy over and install the requirements
COPY ./backend/requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Copy over the apache configuration file and enable the site
COPY ./ssrf-app.conf /etc/apache2/sites-available/ssrf-app.conf
RUN a2ensite ssrf-app
RUN a2enmod headers

# Copy over the wsgi file
COPY ./backend/SSRFApp.wsgi /var/www/SSRFApp/SSRFApp.wsgi
COPY ./backend/ssrf_app /var/www/SSRFApp/ssrf_app/

RUN a2dissite 000-default.conf
RUN a2ensite ssrf-app.conf

EXPOSE 80

WORKDIR /var/www/SSRFApp

# CMD ["/bin/bash"]
CMD  /usr/sbin/apache2ctl -D FOREGROUND
# The commands below get apache running but there are issues accessing it online
# The port is only available if you go to another port first
# ENTRYPOINT ["/sbin/init"]
# CMD ["/usr/sbin/apache2ctl"]
