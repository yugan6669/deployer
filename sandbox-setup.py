#!/usr/bin/env python

# importing statements
import subprocess

# Linux commands to execute
#yum update -y && yum upgrade -y && yum install epel-release -y
cmds = ["sudo yum install git -y && sudo yum install wget -y && sudo yum install curl -y && sudo yum install unzip -y",
"sudo wget https://releases.hashicorp.com/packer/1.5.5/packer_1.5.5_linux_amd64.zip && sudo unzip packer_1.5.5_linux_amd64.zip && mv packer /bin/ && rm -rf ./packer*",
"sudo wget https://releases.hashicorp.com/terraform/0.12.24/terraform_0.12.24_linux_amd64.zip && sudo unzip terraform_0.12.24_linux_amd64.zip && mv terraform /bin/ && rm -rf ./terraform*",
"sudo cp ./ansible.repo /etc/yum.repos.d/ && sudo yum install ansible -y"]

for cmd in cmds:
    print("command name", cmd)
    cmd_execution = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.STDERR, shell = True)
    cmd_output, cmd_error = cmd_execution.communicate()
    print("output of the command", cmd_output)

    
