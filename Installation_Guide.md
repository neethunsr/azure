# Follow the below commands for the respective installations in UBUNTU...

# AWS Cli Installation 
>Commands to be Followed:
```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```
>Verify the awscli installation:
> `aws --version`

## AWS Configuration
>Command:
>`aws configure
`

>Following output will be shown
AWS Access Key ID [None]: your access key ID
AWS Secret Access Key [None]: your secret access key ID
Default region name [None]: your region
Default output format [None]: json

## Kubectl Installation
>Commands to be followed:
```
$ curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
$ sudo touch /etc/apt/sources.list.d/kubernetes.list 
$ echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
$ sudo apt-get update
$ sudo apt-get install -y kubectl
```

>  **Verify Kubectl Installation**
`kubectl version --client` 

## Accessing to our cluster
>Commands to be followed:
`aws eks --region <region_name> update-kubeconfig --name <cluster_name> `
Ex: <region_name> ----> ap-south-1
<cluster_name> ----> Name of the cluster



## Kotena Lens Installation
 >Commands to be followed: 
```
sudo apt update
sudo apt install snapd
sudo snap install kontena-lens --classic
```

##Helm Installation
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh --version v3.1.1
