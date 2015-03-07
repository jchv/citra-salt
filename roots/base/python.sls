pip3:
  file.managed:
    - name: /usr/local/sbin/get-pip.py
    - source: https://raw.githubusercontent.com/pypa/pip/1.5.6/contrib/get-pip.py
    - source_hash: md5=3f120892a637a59a9c497d516eb2ca76

  cmd.run:
    - name: python3 /usr/local/sbin/get-pip.py
    - unless: which pip3
    - require:
      - file: /usr/local/sbin/get-pip.py

python3:
  pkg.latest:
    - refresh: False
    - pkgs:
      - python3
      - python3-dev
      - build-essential
      - libyaml-dev
      - postgresql-server-dev-9.3
