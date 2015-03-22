citraweb:
  group:
    - system: True
    - present
  user:
    - system: True
    - present
    - groups:
      - citraweb
    - require:
      - group: citraweb
