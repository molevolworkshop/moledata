export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y curl software-properties-common ##needs interaction
add-apt-repository -y -c universe 
apt update
apt-get install -y build-essential
apt upgrade -y


apt-get install -y git

cd ~
mkdir 



##PhyloNetworks lab
apt-get install -y r-base
curl -fsSL https://install.julialang.org | sh -s -- -y #install julia thru juliaup
 . /root/.bashrc #update the path?
julia -e 'using Pkg; Pkg.add("PhyloNetworks"); Pkg.add("PhyloPlots"); Pkg.add("SNaQ"); Pkg.add("RCall"); Pkg.add("CSV"); Pkg.add("DataFrames"); Pkg.add("StatsModels")'
#Phyloplots installation breaks without R


## Migrate lab
apt-get install -y autoconf automake 
apt-get install -y pkg-config zlib1g-dev openmpi-bin libopenmpi-dev
git clone --depth 1 https://github.com/pbeerli/migrate-5.0.7.git
cd migrate-5.0.7

autoreconf -i
./configure
make
#migrate-n lives in src


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


### PAML
git clone --depth 1 https://github.com/abacus-gene/paml
cd paml/src
make -f Makefile