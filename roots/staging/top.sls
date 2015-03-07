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
    - web.nginx
    - web.django
    - web.uwsgi
    - web.repo
