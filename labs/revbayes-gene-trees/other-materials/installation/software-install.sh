#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive

## RevBayes
apt-get install -y cmake libboost-all-dev
git clone --depth 1 --branch master https://github.com/revbayes/revbayes.git revbayes
cd revbayes/projects/cmake
./build.sh
cp ./build/rb /usr/local/bin
cd /
rm -rf /tmp/revbayes
apt-get clean
rm -rf /var/lib/apt/lists/*