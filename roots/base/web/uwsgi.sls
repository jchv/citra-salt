citra-web:
  supervisord:
    - running
    - require:
      - pkg: supervisor
      - cmd: citra-deps
    - watch:
      - file: /etc/supervisor/conf.d/citra-web.conf
      - file: /etc/citra-web/settings.yaml

/etc/supervisor/conf.d/citra-web.conf:
  file.managed:
    - source: salt://web/etc/supervisor/conf.d/citra-web.conf
    - template: jinja
    - user: root
    - group: root
    - mode: 644
    - require:
      - cmd: citra-deps
      - file: /etc/citra-web/settings.yaml
