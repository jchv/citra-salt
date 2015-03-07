/etc/nginx/sites-enabled/citra-web.conf:
  file.managed:
    - source: salt://web/etc/nginx/sites-enabled/citra-web.conf
    - template: jinja
    - user: root
    - group: root
    - mode: 644
    - require:
      - pkg: nginx
