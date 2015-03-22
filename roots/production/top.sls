production:
  '*':
    - nginx
    - python
    - supervisor
    - paths
    - git
    - zsh
    - users

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
