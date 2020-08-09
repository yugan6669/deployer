# Deployer
this repo is used to do deployments using automation tools like Python

Step 0: add public keys

 #!/bin/bash
 
 ssh-keygen -q -t rsa -N '' -f /home/centos/.ssh/id_rsa <<<y 2>&1 >/dev/null

 cat /home/centos/.ssh/id_rsa.pub >> /home/centos/.ssh/authorized_keys

 ssh -o StrictHostKeyChecking=no centos@localhost


step 1: clone repo

$git clone https://github.com/krishnamaram2/Configuration_Manager.git

Step 2:

$cd Configuration_Manager/src/plays

$ansible-playbook -i hosts opsstack.yml

$ansible-playbook -i hosts devstack.yml

$ansible-playbook -i hosts webapp.yml






