install-ssmtp:
  pkg.installed:
    - pkgs:
      - ssmtp

ssmtp-conf:
  file.managed:
    - name: /etc/ssmtp/ssmtp.conf
    - source: salt://files/etc/ssmtp/ssmtp.conf
    - template: jinja
    - require:
      - pkg: install-ssmtp

php-ssmtp-conf:
  file.managed:
    - name: /etc/php5/fpm/conf.d/30-ssmtp.ini
    - source: salt://files/etc/php5/fpm/conf.d/30-ssmtp.ini
    - require:
      - pkg: install-php-fpm
