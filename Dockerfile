FROM php:8.2-apache

# Enable mod_rewrite
RUN a2enmod rewrite

# Install required PHP extensions + composer
RUN apt-get update && apt-get install -y \
    libicu-dev \
    git \
    unzip \
    && docker-php-ext-install intl \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set document root
ENV APACHE_DOCUMENT_ROOT=/var/www/html/public
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf

# Allow .htaccess overrides
RUN sed -i '/<Directory \/var\/www\/>/,/<\/Directory>/ s/AllowOverride None/AllowOverride All/' /etc/apache2/apache2.conf

# Copy base (already cloned in workflow)
COPY base/ /var/www/html/

# Copy site files on top (overlay)
COPY . /var/www/html/

# Install CodeIgniter via Composer
WORKDIR /var/www/html
RUN composer install --no-dev --optimize-autoloader

# Set permissions for writable
RUN chown -R www-data:www-data /var/www/html/writable || true

EXPOSE 80
