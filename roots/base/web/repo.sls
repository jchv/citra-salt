latest-source:
  git.latest:
    - name: git://github.com/johnwchadwick/citra-web.git
    - rev: master
    - target: /opt/citra-web/
    - require:
        - pkg: git
    - require_in:
        - cmd: citra-deps
