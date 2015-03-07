latest-source:
  git.latest:
    - name: https://github.com/johnwchadwick/citra-emu.git
    - rev: master
    - target: /opt/citra-web/
    - require:
        - pkg: git
