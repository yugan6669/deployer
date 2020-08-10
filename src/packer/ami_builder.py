#!/usr/bin/env python
import os

cmds = ["sudo git clone https://github.com/krishnamaram2/image_builder.git && cd ./image_builder/src", "packer validate -var-file=./image_builder/src/variables.json ./image_builder/src/builders.json && packer build -var-file=./image_builder/src/variables.json ./image_builder/src/builders.json"]

for cmd in cmds:
    print("commnad to execute", cmd)
    os.system(cmd)
    
