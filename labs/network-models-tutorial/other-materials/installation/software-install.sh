#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive

##PhyloNetworks lab
apt-get install -y r-base
curl -fsSL https://install.julialang.org | sh -s -- -y #install julia thru juliaup
export PATH="/root/.juliaup/bin:$PATH"
julia -e 'using Pkg; Pkg.add("PhyloNetworks"); Pkg.add("PhyloPlots"); Pkg.add("SNaQ"); Pkg.add("RCall"); Pkg.add("CSV"); Pkg.add("DataFrames"); Pkg.add("StatsModels")'
