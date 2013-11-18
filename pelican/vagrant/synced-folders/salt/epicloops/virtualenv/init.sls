include:
  - langs.python2.virtualenv

/home/vagrant/virtualenvs/epicloops.com:
  virtualenv:
    - managed
    - no_site_packages: True
    - system_site_packages: False
    - runas: vagrant
    - requirements: salt://epicloops/virtualenv/requirements.txt
    - require:
      - sls: langs.python2.virtualenv
