# Automation Logic Coding Task :ok_hand:

### Task:
- Create 3 instances (1 load balancer and 2 apps) using vagrant
- Configure instances using Ansible
- Produce coherent README.md :eyes:

### The brief:
- All VMs built using the following vagrant box:
https://app.vagrantup.com/ubuntu/boxes/bionic64
- All VMs allow the vagrant user, and users in the admin group, to sudo without a password
- Webservers and load balancer running nginx
- Simple ‘Hello World’ application deployed to both webservers
- Automated tests to show that app is deployed correctly and nginx is load balancing correctly
- Solution is idempotent



## Let's get started

### Installation requirements:
- vagrant - https://www.vagrantup.com/docs/installation - Version 2.2.10
- virtual box - https://www.virtualbox.org/wiki/Downloads - Version 6.1
- python - https://www.python.org/downloads/ - Version 3.7.4

### Running the infrastructure
- Git clone repo into your own folder - ``git clone https://github.com/swatson2019/Automation-Logic.git``
- ``CD`` into newly created 'Automation-Logic' folder
- Run ``vagrant up`` - at first required plugins may install and then it will exit so just run ``vagrant up`` again

### Processes explained
- The ``vagrant up`` command runs the vagrant file which contains the information on how the 3 virtual machines will be configured
- The vagrant file uses the ansible playbooks located in the provisioning folder to install various software onto the machines
- If all goes well there will be 3 VMs in your virtual box (1 load balancer & 2 web app instances)

### The result
- Now when you search the load balancer IP address (http://192.168.10.100) or the set host alias (development.local) into your search engine it will present you with the web app from the first web server (http://192.168.10.101)
- If you refresh twice the load balancer will then present you with the app from the second web server (http://192.168.10.102) and then another refresh will send you back to the first web server - this is because of the way I configured the nginx 'loadbalancer.conf' file with a weight of 2 on the first server (https://upcloud.com/community/tutorials/configure-load-balancing-nginx)
- In this example the apps are identical (due to using the same configuration and app setup) and therefore it will not be obvious that the load balancing is working - in order to make this clear you can make different apps

### Running tests
- Now ``CD`` into tests folder and run ``pytest``
- This tests whether simple url get requests return a 200 status code (aka working website)

### Depreciation warnings:
- [1.1] Sudo - now become --Fixed
- [1.2] Python - now Python3 --Needs attention

### Room for improvement!
- Automated testing would be the priority - trialled and wrestled with various methods such as test-kitchen, pytests and maven but couldn't find a way to test the nginx loadbalancer without actually changing one of the apps and refreshing load balancer page manually
- I tried to get the web apps to post their IPs on the web page to differentiate between the two but couldn't find a way of doing this on a html/ejs file - if I were doing this again I might use a different type of file (maybe php)
- Incorporate more features into the app - e.g. add a database connection or fibonacci sequence feature

### Learned skills:
- How to configure multiple identical virtual machines without writing out the configurations repeatedly
- How to use nginx as a load balancer and different ways of load balancing
