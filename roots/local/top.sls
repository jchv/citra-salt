local:
  '*':
    - nginx
    - python
    - supervisor
    - paths
    - git
    - zsh
    - ssmtp

  'roles:database':
    - match: grain
    - database.postgres
    - database

  'roles:web':
    - match: grain
    - local-motd
    - dev-server
    - web.users
    - web.nginx
    - web.django

  'roles:forum':
    - match: grain
    - php
    - forum.mybb
    - s3fs
