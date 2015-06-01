install-php-fpm:
  pkg.installed:
    - pkgs:
      - php5-fpm
      - php5-gd
      - php5-pgsql
      - php5-memcached
