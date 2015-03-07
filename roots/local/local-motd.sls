/etc/update-motd.d/20-citraweb-local:
  file.managed:
    - source: salt://files/etc/update-motd.d/20-citraweb-local
    - user: root
    - group: root
    - mode: 775
    - template: jinja

