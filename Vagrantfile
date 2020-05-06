# -*- mode: ruby -*-
# vi: set ft=ruby :

#########################
$CPU = 2
$MEMORY = 4096
$CPUEXECUTIONCAP = 50 # does not work with hyper-v
$IP = "192.168.0.7"   # does not work with hyper-v # https://www.vagrantup.com/docs/hyperv/limitations.html
$BASEOS = "centos/7"
$SSH=2227
#########################

Vagrant.configure("2") do |config|

  # config.vbguest.auto_update = false

  config.vm.box = $BASEOS

  config.vm.provider "virtualbox" do |v|
    v.memory = $MEMORY
    v.cpus = $CPU
    v.customize ["modifyvm", :id, "--cpuexecutioncap", $CPUEXECUTIONCAP]
    v.customize ["modifyvm", :id, "--vram", "128"]
  end
  
  config.vm.provider "hyperv" do |v|
    v.memory = $MEMORY
    v.cpus = $CPU
  end

  config.vm.provider "libvirt" do |v|
    v.memory = $MEMORY
    v.cpus = $CPU
  end

  config.vm.synced_folder ".", "/vagrant/ansible-role-basics", type: "rsync"

  config.vm.network "private_network", ip: $IP
  config.vm.network "forwarded_port", guest: 22, host: $SSH, id: 'ssh'

  config.vm.provision "ansible.cfg", type: "shell", privileged: false, 
    inline: "printf '[defaults]\nroles_path=/vagrant/' >ansible.cfg"
  
  config.vm.provision "ansible", type: "ansible_local" do |ansible|
    ansible.playbook = "/vagrant/playbook.yml"
    ansible.become = true
  end
  
end
