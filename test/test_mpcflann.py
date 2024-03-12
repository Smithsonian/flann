import numpy as np
import os

from pyflann import *

# relative directory structure

testdir = os.getcwd()

inputdir = os.path.join(os.path.dirname(__file__),'input/')
inputdatfile = os.path.join(inputdir,'flanntest.dat')

# expected results
# for radius search
test_radsqr = .000001
match_result00 = np.array([4,11])
match_result01 = np.array([0.00000000e+00, 5.40855993e-07])
match_result10 = np.array([12])
match_result11 = np.array([0.])

# for point removal/addition
dataidx1 = {0:0,1:1,2:2,3:3,5:4,6:5,7:6,8:7,9:8,10:9,11:10,'nextidx':12} # after remove point 4
dataidx2 = {0:0,1:1,2:2,3:3,5:4,6:5,7:6,8:7,9:8,10:9,'nextidx':12} # after remove point 11
dataidx3 = {0:0, 1:1, 2:2, 3:3, 5:4, 6:5, 7:6, 8:7, 9:8, 10:9, 12:10,'nextidx': 13} # after add point 4 again


def test_mpc_pyflann():
    '''
    Test edited Python3 version of pyflann
    for tree construction and addition/removal of leaves
    Test by M. Pan, Jan 2024
    '''

    # read in test data, define test points
    with open(inputdatfile,'r') as fh:
        _ = [x.rstrip().split(',') for x in fh.readlines()]

    dat = np.array([[float(x) for x in y] for y in _])

    # build tree from test data
    flanntree = FLANN()
    params = flanntree.build_index(dat,algorithm="kdtree",checks=16)
    assert np.array_equal(flanntree._FLANN__curindex_data, dat)
    assert flanntree._FLANN__dataidx == dict({x:x for x in range(12)}, **{'nextidx':12})

    # test radius search
    matches0 = flanntree.nn_radius(dat[4],test_radsqr)
    assert np.array_equal(matches0[0],match_result00) and np.allclose(matches0[1],match_result01)
    
    # test point removal
    flanntree.remove_point(4)
    assert np.array_equal(flanntree._FLANN__curindex_data, np.delete(dat, (4), axis=0))
    assert flanntree._FLANN__dataidx == dataidx1

    flanntree.remove_point(11)
    assert np.array_equal(flanntree._FLANN__curindex_data, np.delete(dat, (4,11), axis=0))
    assert flanntree._FLANN__dataidx == dataidx2

    # test point addition
    flanntree.add_points(dat[4])
    assert np.array_equal(flanntree._FLANN__curindex_data, dat[[0,1,2,3,5,6,7,8,9,10,4]])
    assert flanntree._FLANN__dataidx == dataidx3
    
    # test radius search
    matches1 = flanntree.nn_radius(dat[4],test_radsqr)
    assert np.array_equal(matches1[0],match_result10) and np.array_equal(matches1[1],match_result11)
