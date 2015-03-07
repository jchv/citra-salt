nginx:
  pkg:
    - installed
  service:
    - running
    - require:
      - pkg: nginx
    - watch:
      - pkg: nginx
      - file: /etc/nginx/sites-enabled/*

/etc/nginx/sites-enabled/default:
  file.absent:
    - require:
      - pkg: nginx
