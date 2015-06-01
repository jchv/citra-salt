s3fs-prereqs:
  pkg.installed:
    - pkgs:
      - build-essential
      - automake
      - autoconf
      - make
      - libcurl4-openssl-dev
      - libxml2-dev
      - libfuse-dev
      - libssl-dev
      - git

s3fs-source:
  git.latest:
    - name: https://github.com/s3fs-fuse/s3fs-fuse.git
    - target: /usr/src/s3fs
    - require:
      - pkg: s3fs-prereqs

s3fs-autogen:
  cmd.run:
    - name: /usr/src/s3fs/autogen.sh
    - unless: test -f /usr/src/s3fs/configure
    - cwd: /usr/src/s3fs
    - require:
      - git: s3fs-source

{# TODO: Out of tree build, non-root build #}
s3fs-configure:
  cmd.run:
    - name: /usr/src/s3fs/configure
    - unless: test -f /usr/src/s3fs/Makefile
    - cwd: /usr/src/s3fs
    - require:
      - cmd: s3fs-autogen

s3fs-make:
  cmd.run:
    - name: make -C /usr/src/s3fs
    - unless: test -f /usr/src/s3fs/src/s3fs
    - cwd: /usr/src/s3fs
    - require:
      - cmd: s3fs-configure

s3fs-install:
  cmd.run:
    - name: make -C /usr/src/s3fs install
    - unless: which s3fs
    - cwd: /usr/src/s3fs
    - require:
      - cmd: s3fs-make

s3fs-passwd:
  file.managed:
    - name: /etc/passwd-s3fs
    - contents: "{{ pillar['aws_key'] }}:{{ pillar['aws_secret_key'] }}"
    - mode: 600
    - user: root
    - group: root
