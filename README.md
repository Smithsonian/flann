FLANN
-------------
FLANN is a library for performing fast approximate nearest neighbor searches in high dimensional spaces. It contains a collection of algorithms we found to work best for nearest neighbor search and a system for automatically choosing the best algorithm and optimum parameters depending on the dataset.
FLANN is written in C++ and contains bindings for the following languages: C, MATLAB, Python, and Ruby.  
FLANN is distributed under the terms of the [BSD License](https://github.com/mariusmuja/flann/blob/master/COPYING).

MPC forked FLANN
-------------

This https://github.com/Smithsonian/flann fork of flann is used as a submodule in mpc-software. Specifically, flann is used by mpc-heliolinc to create and traverse KD-trees.  
The latest changes of MPC's forked flann can be pulled into mpc-software by running: `git submodule update --recursive --remote` to bring latest changes from flann:master into flann submodule. 

Changes into forked flann repository SHOULD be pushed ONLY from mpc's forked flann repository directly. `git pull` should be run regularly on branches created from flann:master to make sure the latest changes are applied.

Initial installation of MPC's FLANN on Rocky Linux
-----------------

```console
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

Testing the above installation
-----------------

A good sanity check would be to run `test_mpcflann.py` test after executing the above commands:  

`cd flann/test`  

`pytest test_mpcflann.py`
