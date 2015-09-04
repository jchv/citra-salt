/usr/local/bin/devserver:
  file.managed:
    - user: root
    - group: root
    - mode: 755
    - contents: |
        #!/bin/sh
        python3 /opt/citra-web/manage.py runserver 0.0.0.0:8000 $*

/usr/local/bin/migrate:
  file.managed:
    - user: root
    - group: root
    - mode: 755
    - contents: |
        #!/bin/sh
        python3 /opt/citra-web/manage.py migrate $*

/usr/local/bin/makemigrations:
  file.managed:
    - user: root
    - group: root
    - mode: 755
    - contents: |
        #!/bin/sh
        python3 /opt/citra-web/manage.py makemigrations $*

/usr/local/bin/collectstatic:
  file.managed:
    - user: root
    - group: root
    - mode: 755
    - contents: |
        #!/bin/sh
        python3 /opt/citra-web/manage.py collectstatic $*
