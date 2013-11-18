.aws:
  file:
    - managed
    - name: /home/vagrant/.aws/config
    - source: salt://.aws/config
    - user: vagrant
    - group: vagrant
