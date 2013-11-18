#!/bin/bash

#==============================================================================
# Variables
#==============================================================================
VM_NAME=epicloops
SALT_MASTER=localhost
SALT_VERSION=v0.17.0

#==============================================================================
# Helper Functions
#==============================================================================
countdown () {
  w=$1
  x=$1
  while [ $x -gt 0 ]; do
    echo -ne "Wait $w seconds:    \r"
    echo -ne "Wait $w seconds: $x\r"
    sleep 1
    x=$(($x-1))
  done
  # Leave evidence of countdown in output
  echo -ne "Wait $w seconds:    \r"
  echo "Wait $w seconds: $x"
}

#===  Salt Functions  =========================================================
# A few functions related to Salt.
# From install, to config files, to restarting services, to calling highstate.
#==============================================================================
install_salt () {
  # Download and install master and minion
  wget -O - http://bootstrap.saltstack.org | sudo sh -s -- -M -P git $1
}

minion_keys () {
  echo " *** GENERATING AND PRESEEDING MINION KEYS ***"
  salt-key --gen-keys=$1 --gen-keys-dir=/tmp/salt-keys/
  cp /tmp/salt-keys/$1.pub /etc/salt/pki/master/minions/$1
  cp /tmp/salt-keys/$1.pub /etc/salt/pki/minion/minion.pub
  cp /tmp/salt-keys/$1.pem /etc/salt/pki/minion/minion.pem
  rm -rf /tmp/salt-keys
}

minion_config () {
echo " *** UPDATING MINION CONFIG ***"
cat > /etc/salt/minion <<EOL
master: $1
id: $2

EOL
}

master_config () {
echo " *** UPDATING MASTER CONFIG ***"
cat > /etc/salt/master <<EOL
fileserver_backend:
  - roots
  - git

file_roots:
  base:
    - /srv/salt/base
    - /srv/salt/dotfiles-protected

gitfs_remotes:
  - git://github.com/ajw0100/dev-vm-saltfs.git
  - git://github.com/ajw0100/dotfiles.git

ext_pillar:
  - git: master git://github.com/ajw0100/dev-vm-pillar.git

EOL
}

restart_minion () {
  service salt-minion restart
  countdown $1
}

restart_master () {
  service salt-master restart
  countdown $1
}

state_highstate () {
  salt -l debug '*' state.highstate
}

#===  Python Packaging  =======================================================
# Install the latest python packaging system according to PyPA:
# https://python-packaging-user-guide.readthedocs.org/en/latest/setup.html
#==============================================================================
install_setuptools () {
  echo " *** INSTALLING SETUPTOOLS ***"
  wget --output-document=/home/vagrant/ez_setup.py \
  https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py

  python /home/vagrant/ez_setup.py
  rm -rf /home/vagrant/ez_setup.py /home/vagrant/setuptools-1.1.6.tar.gz
}

install_pip () {
  echo " *** INSTALLING PIP ***"
  wget --output-document=/home/vagrant/get-pip.py \
  https://raw.github.com/pypa/pip/master/contrib/get-pip.py

  python /home/vagrant/get-pip.py
  rm -rf /home/vagrant/get-pip.py
}

#===  GitFS Requirements  =====================================================
# GitFS requires both git and GitPython to be installed.
# We are installing git using apt-get and GitPython using pip.
#==============================================================================
install_git () {
  echo " *** INSTALLING GIT USING APT_GET ***"
  apt-get install -y git
}

install_git_python () {
  echo " *** INSTALLING GITPYTHON ***"
  pip install GitPython==0.3.2.RC1
}

#==============================================================================
# Proceed with bootstrap
#==============================================================================
install_salt $SALT_VERSION

# Config minion
#   - Generate and preseed minion keys
#   - Update config to contain id and look for master on localhost
minion_keys $VM_NAME
minion_config $SALT_MASTER $VM_NAME
restart_minion 5

# Config master
#   - install git, setuptools, pip, and GitPython
#   - update config to use github for the fileserver and pillar
install_git
install_setuptools
install_pip
install_git_python
master_config
restart_master 15

state_highstate
