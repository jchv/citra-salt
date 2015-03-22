citra-web:
  supervisord:
    - running
    - require:
      - pkg: supervisor
      - cmd: citra-deps
      - user: citraweb
    - watch:
      - file: /etc/supervisor/conf.d/citra-web.conf
      - file: /etc/citra-web/settings.yaml
      - file: /etc/citra-web/uwsgi.yml

/etc/supervisor/conf.d/citra-web.conf:
  file.managed:
    - source: salt://web/etc/supervisor/conf.d/citra-web.conf
    - template: jinja
    - user: root
    - group: root
    - mode: 644
    - require:
      - pkg: supervisor

/etc/citra-web/uwsgi.yml:
  file.managed:
    - source: salt://web/etc/citra-web/uwsgi.yml
    - template: jinja
    - user: root
    - group: root
    - mode: 644
