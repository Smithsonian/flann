FLANN
-------------
FLANN is a library for performing fast approximate nearest neighbor searches in high dimensional spaces. It contains a collection of algorithms we found to work best for nearest neighbor search and a system for automatically choosing the best algorithm and optimum parameters depending on the dataset.
FLANN is written in C++ and contains bindings for the following languages: C, MATLAB, Python, and Ruby.  
FLANN is distributed under the terms of the [BSD License](https://github.com/mariusmuja/flann/blob/master/COPYING).

MPC's fork of FLANN
-------------

This https://github.com/Smithsonian/flann fork of flann is used as a submodule in mpc-software. Specifically, flann is used by mpc-heliolinc to create and traverse KD-trees.  
The latest changes of MPC's forked flann can be pulled into mpc-software by running: `git submodule update --recursive --remote` to bring latest changes from flann:master into flann submodule. 

Changes into forked flann repository SHOULD be pushed ONLY from mpc's forked flann repository directly. `git pull` should be run regularly on branches created from flann:master to make sure the latest changes are applied.

### Shell script installation of flann for Rocky Linux 9  

```
git clone https://github.com/Smithsonian/flann  

cd flann  

./flann_installation.sh  
```  

### Manual installation of flann on Rocky Linux 9

```
git clone https://github.com/Smithsonian/flann  

cd flann  

mkdir build  

cd build  

sudo dnf update  

sudo dnf install epel-release    

sudo dnf install lz4 lz4-devel  

sudo dnf install hdf5 hdf5-devel hdf5-static  

sudo dnf install numpy  

sudo dnf install pytest  

sudo dnf install cmake    

sudo cmake ..  

sudo make  

sudo make install  
```

Good sanity check would be to `cd` to `flann/test` and run:

$ `pytest test_mpcflann.py`  

### Manual installation of flann on non Rocky Linux 9 operating systems.  

To manually install `flann` on your machine, first, install (using package manager as per your operating system) all the required libraries:  
`lz4`, `lz4-devel`, `hdf5`, `hdf5-devel`, `hdf5-static`, `cmake`, `numpy` and `pytest` for running python tests. After all the libraries are installed follow the following steps:  
```
git clone https://github.com/Smithsonian/flann  

cd flann  

mkdir build  

cd build  

cmake ..  

make  

make install  
```
