from database.seeds.definitions import seed_word_definitions
from database.hdf5 import HDF5


def test_definitions_seeder():
    seed_word_definitions()
    hdf = HDF5('lexicon.hdf5')

    assert hdf.get('dune/meaning') == 'a ridge of sand created by the wind; found in deserts or near lakes and oceans'