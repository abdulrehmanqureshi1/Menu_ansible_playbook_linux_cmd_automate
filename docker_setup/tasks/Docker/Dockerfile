FROM centos
RUN yum -y install httpd
RUN yum clean all
COPY index.html   /var/www/html/
COPY run.sh run.sh
RUN  chmod +x run.sh
CMD ./run.sh
EXPOSE 80
