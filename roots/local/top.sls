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
