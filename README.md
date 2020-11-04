# Automation Logic Coding Task :ok_hand:

## Task:
- Create 3 instances (1 load balancer and 2 apps) using vagrant
- Configure instances using Ansible
- Produce coherent README.md :eyes:

##### Need to save image onto repot first #####
![alt text](https://github.com/swatson2019/Automation-Logic/blob/master/image.jpg?raw=true)

# The brief:
- All VMs built using the following vagrant box:
https://app.vagrantup.com/ubuntu/boxes/bionic64
- All VMs allow the vagrant user, and users in the admin group, to sudo without a password
- Webservers and load balancer running nginx
- Simple ‘Hello World’ application deployed to both webservers
- Automated tests to show that app is deployed correctly and nginx is load balancing correctly
- Solution is idempotent

# Depreciation warning:
- Sudo - now become
- Python now Python3

# Warnings:
-  The value True (type bool) in a string field was converted to
u'True' (type string)

# Bugs which could fix if have time:
- App only works when I move folders (index & public) into the environment folder - need to find way of telling machine right place to find folders - change directory back to normal after running pm2 command

# Installed software:
- choco
- ruby devkit - installed ansible-provisioner (gem install test-kitchen, gem install kitchen-ansible & gem install kitchen-vagrant)
- vagrant
- virtual box
- chefdk ()
- msys2 - because gem install kitchen-vagrant and kitchen-ansible didn't work unless installed this
