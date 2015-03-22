citra-deps:
  cmd.run:
    - name: pip3 install -r /opt/citra-web/requirements/{{ env }}.txt
    - require:
      - cmd: pip3
      - pkg: nginx
      - pkg: git

/etc/citra-web/settings.yaml:
  file.managed:
    - source: salt://web/etc/citra-web/settings.yaml
    - template: jinja
    - user: root
    - group: root
    - mode: 644
    - context: { env: {{ env }} }
    - require:
      - file: /etc/citra-web

migrations:
  cmd.run:
    - name: /opt/citra-web/manage.py migrate
    - user: root
    - require:
      - cmd: citra-deps
      - postgres_database: {{ pillar['db']['name'] }}

collectstatic:
  cmd.run:
    - name: /opt/citra-web/manage.py collectstatic --noinput
    - user: root
    - require:
      - cmd: citra-deps
