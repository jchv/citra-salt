postgresql:
  pkg:
    - name: postgresql-9.3
    - installed
  service.running:
    - enable: True
    - watch:
      - file: /etc/postgresql/9.3/main/pg_hba.conf

/etc/postgresql/9.3/main/pg_hba.conf:
  file.managed:
    - source: salt://database/files/etc/postgresql/9.3/main/pg_hba.conf
    - user: postgres
    - group: postgres
    - template: jinja
    - mode: 644
    - require:
      - pkg: postgresql
