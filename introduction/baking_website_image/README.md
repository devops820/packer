# packer

get your aws cli credentials.

can you the below query with filter criteria to get a list of ami's from aws.

```
aws ec2 describe-images --filters "Name=virtualization-type,Values=hvm" "Name=root-device-type,Values=ebs" "Name=owner-id,Values=099720109477" "Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-*" --query 'Images[*].[ImageId]' --output text

aws ec2 describe-images --region us-west-1 --image-ids ami-0f93593c7794d31f1

aws ec2 describe-images --owner self --query 'Images[*].[ImageId]' 

```

de-register the amis

```
aws ec2 deregister-image --image-id  ami-04b1dbe4dc3dd6303
aws ec2 deregister-image --image-id  ami-098e8829b9a9bad03
aws ec2 deregister-image --image-id  ami-017204da9f4434856
aws ec2 deregister-image --image-id ami-08b61b703a4308fb9
```

using variables on the command line

```
packer validate -var "aws_access_key=key" -var "aws_secret_key=secret" custom_ubuntu_ami.json
packer build -var "aws_access_key=key" -var "aws_secret_key=secret" custom_ubuntu_ami.json
```

use a variables file instead to build the image
```
packer build -var-file variables.json custom_ubuntu_ami.json
packer validate -var-file variables.json custom_ubuntu_ami.json
```

use an aws run instance command to launch an ami into a running virtual machine.
```
mariadb instance
aws ec2 run-instances --instance-type t2.micro --count 1 --key-name SaiKeyPair --image ami-017204da9f4434856

nginx instance
aws ec2 run-instances --instance-type t2.micro --count 1 --key-name SaiKeyPair --image ami-071ecaa89f58cc95b

aws ec2 describe-instances --filters "Name=image-id,Values=ami-071ecaa89f58cc95b"
aws ec2 terminate-instances --instance-ids i-01cfd5227f919c5e4
aws ec2 terminate-instances --instance-ids i-0d3883942127c4491
```

To list the instances run with specific ami run the following aws cli command
```
aws ec2 describe-instances --filters "Name=image-id,Values=ami-08b61b703a4308fb9"
aws ec2 describe-instances --filters "Name=image-id,Values=ami-002d7270745ee59ce"
```

Add the following ingress rules so that you can ssh into the ec2 machine
```
Get the security group information from the following query

aws ec2 describe-security-groups --group-ids sg-0c047509b36299d77

Inbound rules

aws ec2 authorize-security-group-ingress --group-id sg-0c047509b36299d77 --protocol tcp --port 80 --cidr 49.37.152.248/32
aws ec2 authorize-security-group-ingress --group-id sg-0c047509b36299d77 --protocol tcp --port 22 --cidr 49.37.152.248/32
```  