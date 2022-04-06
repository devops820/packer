# using configuration mgmt tools with packer

```
➜  customization_with_config_mgmt ansible-galaxy install -r requirements.yml                                                        
Starting galaxy role install process
- downloading role 'nginx', owned by nginxinc
- downloading role from https://github.com/nginxinc/ansible-role-nginx/archive/0.23.0.tar.gz
- extracting nginxinc.nginx to /Users/smarlakunta/.ansible/roles/nginxinc.nginx
- nginxinc.nginx (0.23.0) was installed successfully
```

And then use the playbook to instantiate the role & write post tasks if required.
```
---
- name: nginx playbook
  hosts: all
  roles:
   - role: nginxinc.nginx
  post_tasks:
   - name: upload website files
     copy: src=./files/website/ dest=/usr/share/nginx/html/ mode=644
   - name: Allow all access to tcp port 80
     ufw:
       rule: allow
       port: 80
       proto: tcp
```

You can run packer in debug mode.
```
packer build -debug ubuntu.json
or
export PACKER_LOG='/tmp/packer.log'
or
PACKER_LOG=1 packer build -debug ubunut.json |& tee debug.txt
```