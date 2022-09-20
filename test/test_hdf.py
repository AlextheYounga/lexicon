import pytest
from database.hdf5 import HDF5
import os


TEST_HDF5_FILE = 'test.hdf5'

def test_hdf5_setup():
    """hdf5 class properly sets up new hdf5 file"""
    HDF5(TEST_HDF5_FILE)

    assert os.path.exists(TEST_HDF5_FILE)

def test_hdf5_write():
    """hdf5 file properly writes data and returns array of path and dataset"""
    test_data = {
        'description': 'the spice extends life, the spice expands consciousness.'
    }
    hdf = HDF5(TEST_HDF5_FILE)
    hdf5_response = hdf.store('product', test_data)

    assert hdf5_response == ['product', test_data]

    
def test_hdf5_fetch():
    """hdf5 file properly fetches data from storage path"""
    test_data = {
        'description': 'the spice extends life, the spice expands consciousness.'
    }
    hdf = HDF5(TEST_HDF5_FILE)
    hdf.store('product', test_data)

    fetched_from_hdf5 = hdf.get('product/description')

    assert test_data['description'] == fetched_from_hdf5

def test_hdf5_nested_storage():
    """hdf5 file properly fetches data from storage path"""
    test_storage_path = 'product/dune/spice-melange'
    test_data = {
        'description': 'the spice extends life, the spice expands consciousness.'
    }
    hdf = HDF5(TEST_HDF5_FILE)
    hdf.store(test_storage_path, test_data)

    fetched_from_hdf5 = hdf.get(f"{test_storage_path}/description")

    assert test_data['description'] == fetched_from_hdf5




@pytest.fixture(autouse=True)
def run_after():
    yield
    os.remove(TEST_HDF5_FILE)