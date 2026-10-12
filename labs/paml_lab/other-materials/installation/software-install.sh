#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive

### PAML
git clone --depth 1 https://github.com/abacus-gene/paml
cd paml/src
make -f Makefile
cp baseml /usr/local/bin/baseml
cp codeml /usr/local/bin/codeml
cp ds /usr/local/bin/ds