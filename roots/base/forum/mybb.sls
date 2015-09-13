download-mybb-source:
  archive.extracted:
    - name: /usr/src/mybb-1805/
    - source: http://resources.mybb.com/downloads/mybb_1805.zip
    - source_hash: md5=80a24a9a434e0c70e2a21e3b1744378f
    - archive_format: zip

link-mybb-upload-dir:
  file.symlink:
    - name: /opt/mybb
    - target: /usr/src/mybb-1805/Upload
    - require:
      - archive: download-mybb-source

set-mybb-cache-dir-permissions:
  file.directory:
    - name: /opt/mybb/cache
    - user: www-data
    - group: www-data
    - dir_mode: 777
    - file_mode: 666
    - require:
      - file: link-mybb-upload-dir

mybb-config-php:
  file.managed:
    - name: /opt/mybb/inc/config.php
    - source: salt://forum/files/opt/mybb/inc/config.php
    - template: jinja
    - require:
      - file: link-mybb-upload-dir

mybb-settings-php:
  file.managed:
    - name: /opt/mybb/inc/settings.php
    - mode: 666
    - user: www-data
    - group: www-data
    - require:
      - file: link-mybb-upload-dir

mybb-upload-dir-mount:
  mount.mounted:
    - name: /opt/mybb/uploads/
    - device: s3fs#static.citra-emu.org:/forum/uploads
    - fstype: fuse
    - opts: nonempty,allow_other
    - require:
      - file: link-mybb-upload-dir
      - file: s3fs-passwd
      - cmd: s3fs-install

/etc/nginx/sites-enabled/citra-forum.conf:
  file.managed:
    - source: salt://forum/files/etc/nginx/sites-enabled/citra-forum.conf
    - template: jinja
    - user: root
    - group: root
    - mode: 644
    - require:
      - pkg: nginx

/opt/mybb/install/lock:
  file.managed:
    - contents: ''
    - require:
      - file: link-mybb-upload-dir
