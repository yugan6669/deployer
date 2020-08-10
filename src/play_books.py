#!/usr/bin/env python
import os

cmds = ["sudo git clone https://github.com/krishnamaram2/configuration_manager.git && cd ./configuration_manager/src", "sudo ansible-palybook -i  ./configuration_manager/src/webapp  ./configuration_manager/src/webapp/plays/webapp.yml"]

for cmd in cmds:
    print("commnad to execute", cmd)
    os.system(cmd)
