# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Vagrant box
  config.vm.box = "ubuntu/trusty32"

  # Set network configuration
  config.vm.network "public_network"

  # Provisioning with shell script
  config.vm.provision :shell, path: "bootstrap.sh"
end
