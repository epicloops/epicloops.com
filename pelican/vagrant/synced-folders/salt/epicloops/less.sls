include:
  - epicloops.nodejs

install_less:
  cmd:
    - run
    - name: npm install -g less
    - require:
      - sls: epicloops.nodejs
