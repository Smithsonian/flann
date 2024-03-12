#!/bin/bash

echo "Installing flann library"

mkdir "build"

cd "build"

sudo dnf update -y

sudo dnf install epel-release -y

sudo dnf install lz4 lz4-devel -y

sudo dnf install hdf5 hdf5-devel hdf5-static -y

sudo dnf install numpy -y

sudo dnf install pytest -y

sudo dnf install cmake -y

sudo cmake ..

sudo make

sudo make install