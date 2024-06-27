# masters_prject_chandu_fuldev "The project going on full stack development with devops"

## kubernetes and kubectl download guide.
### this is for linux X86-64 that i am using now
- curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
Validate the binary
- curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
### Validate the kubectl binary against the checksum file:
- echo "$(cat kubectl.sha256) kubectl" | sha256sum --check
### if you validate the output as "kubectl: OK" then its fine.
- install Kubectl
- sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
### check the version
- kubectl version --client

### kubernetes command to install minikube
- curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
- sudo dpkg -i minikube_latest_amd64.deb

### Start minikube 
- minikube start --force

- minikube status

