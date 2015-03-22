citra-db:
  postgres_user.present:
    - name: {{ pillar['db']['username'] }}
    - password: {{ pillar['db']['password'] }}
    - createdb: True
    - require:
      - service: postgresql
  postgres_database.present:
    - name: {{ pillar['db']['name'] }}
    - encoding: UTF8
    - lc_ctype: en_US.UTF-8
    - lc_collate: en_US.UTF-8
    - template: template0
    - owner: {{ pillar['db']['username'] }}
    - require:
      - postgres_user: {{ pillar['db']['username'] }}
