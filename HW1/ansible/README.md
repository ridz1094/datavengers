# ansible
Using Ansible to automate the process of application deployment

Steps to follow
1. Need to run following commands to perform following actions on the servers described in hosts.yml
  - Install Nginx
  - Open port 8080
  - Deploy nginx server to port 8080
  
ansible-playbook nginx.yml --extra-vars process="deploy"

2. Need to run following commands to perform following actions on the servers described in hosts.yml
  - Uninstall Nginx
  - Close port 8080
  - Undeploy nginx server to port 8080
  
ansible-playbook nginx.yml --extra-vars process="undeploy"
