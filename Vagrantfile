# Install required plugins
required_plugins = ["vagrant-hostsupdater"]
required_plugins.each do |plugin|
    exec "vagrant plugin install #{plugin}" unless Vagrant.has_plugin? plugin
end

# Vagrant box instructed to use
BOX_IMAGE = "ubuntu/bionic64"

# How many apps you want to deploy
APP_COUNT = 2

Vagrant.configure("2") do |config|
  config.vm.define "lb" do |lb|
    lb.vm.box = BOX_IMAGE
    lb.vm.network "private_network", ip: "192.168.10.100"
    lb.hostsupdater.aliases = ["development.local"]
    lb.vm.synced_folder "environment/lb", "/home/ubuntu/environment"
    lb.vm.provision "ansible_local"  do |ansible|
      ansible.playbook = "provisioning/lb/nginx.yml"
      # replaced sudo with become - depreciation warning
      ansible.become = true
    end
  end

  (1..APP_COUNT).each do |i|
    config.vm.define "app#{i}" do |app|
      app.vm.box = BOX_IMAGE
      app.vm.network "private_network", ip: "192.168.10.10#{i}"
      app.hostsupdater.aliases = ["deployment.local"]
      app.vm.synced_folder "app", "/home/ubuntu/app"
      app.vm.provision "ansible_local"  do |ansible|
        ansible.playbook = "provisioning//app/app.yml"
        ansible.become = true
    end
 end
end
end
