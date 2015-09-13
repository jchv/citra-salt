latest-source:
  git.latest:
    - name: git://github.com/citra-emu/www.git
    - rev: master
    - target: /opt/citra-web/
    - require:
        - pkg: git
    - require_in:
        - cmd: citra-deps
