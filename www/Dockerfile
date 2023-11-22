FROM php:7-apache

COPY . /var/www/html

ENV API_ENDPOINT http://api:5000/api

RUN chown -R www-data:www-data /var/www/html

EXPOSE 80

CMD ["apache2-foreground"]