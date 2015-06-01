local:
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
    - local-motd
    - web.users
    - web.nginx
    - web.django

  'roles:forum':
    - match: grain
    - php
    - forum.mybb
    - s3fs
