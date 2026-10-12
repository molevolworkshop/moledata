#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive


apt-get install -y autoconf automake 
apt-get install -y pkg-config zlib1g-dev openmpi-bin libopenmpi-dev
git clone --depth 1 https://github.com/pbeerli/migrate-5.0.7.git
cd migrate-5.0.7

autoreconf -i
./configure
make
cp ./src/migrate-n /usr/local/bin/migrate-n