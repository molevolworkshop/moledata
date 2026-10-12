export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y curl software-properties-common ##needs interaction
add-apt-repository -y -c universe 
apt update
apt-get install -y build-essential
apt upgrade -y


apt-get install -y git

