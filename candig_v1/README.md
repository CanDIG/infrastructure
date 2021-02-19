If you'd like to install CanDIG on a virtual machine using [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads):

* install those two packages on your local machine
* clone this repo
* `export SHARED_DIR=/some/local/directory` to assign a local directory to be shared with your vm
* run `vagrant up` from within the repo

After provisioning is complete, you should be able to `vagrant ssh` to access your vm.

Once in, you can `source candig-server-env/bin/activate` to start the virtualenv for candig_server, then follow the instructions at https://candig-server.readthedocs.io/en/v1.4.0/development.html#standalone-candig-server-setup to proceed.
