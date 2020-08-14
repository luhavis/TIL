docker run -d \
--name mariadb \
-p 3306:3306 \
-e MYSQL_ROOT_PASSWORD=dahanit12 \
-e LC_ALL=C.UTF-8 \
-v ~/data:/var/lib/mysql \
mariadb:10.4

