#!/usr/bin/env python
import os

cmds = ["sudo git clone https://github.com/krishnamaram2/infrastructure_manager.git && cd ./infrastructure_manager/src/webapp", "sudo terraform init ./infrastructure_manager/src/webapp/ && sudo terraform  validate ./infrastructure_manager/src/webapp  && sudo terraform apply -auto-approve  ./infrastructure_manager/src/webapp"]

for cmd in cmds:
    print("commnad to execute", cmd)
    os.system(cmd)
