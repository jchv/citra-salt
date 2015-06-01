staging:
  '*':
    - nginx
    - python
    - supervisor
    - paths
    - git
    - zsh

  'roles:database':
    - match: grain
    - database.postgres
    - database

  'roles:web':
    - match: grain
    - web.users
    - web.nginx
    - web.django
    - web.uwsgi
    - web.repo

  'roles:forum':
    - match: grain
    - php
    - forum.mybb
    - s3fs
