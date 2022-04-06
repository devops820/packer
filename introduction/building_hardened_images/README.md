# Hardened base os image
ami-026a5c99e7895e5f0

# install the required ansible roles using ansible-galaxy
ansible-galaxy install -r requirements.yml

# this is the jenkins server image which is having the dev-sec hardened image as its base.
ami-05739ed1c6fe60809

# run an instance of jenkins server

# add a rule so that you can access the security group
sg-039ffb3bdf3d644fe
aws ec2 authorize-security-group-ingress --group-id sg-039ffb3bdf3d644fe --protocol tcp --port 8080 --cidr 49.37.152.248/32

# hardened mariadb image
ami-08cb97ab192dc05e1