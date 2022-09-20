import h5py
import os
import numpy as np

ENCODING='utf-8'
class HDF5:
    def __init__(self, hdf5_file_path):
        self.filepath = hdf5_file_path

        if (not os.path.exists(hdf5_file_path)):
            self.hdf = h5py.File(hdf5_file_path, "w")
        else:
            self.hdf = h5py.File(hdf5_file_path, "a")
        

    def store(self, storage_path, dict):
        """
        Stores items from dictionary in hdf5.
        Data can only be saved in string format.

        Args:
            storage_path (string): Path to dataset in hdf5
            dict (dict): Key value dictionary
        """
        dt = h5py.string_dtype(encoding=ENCODING)
        
        if (storage_path not in self.hdf):
            # Create new path
            dset = self.hdf.create_dataset(storage_path, (100,100), dtype=dt)
        else:
            # Append existing path
            dset = self.hdf[storage_path]
        
        # Save data in blob
        for k, v in dict.items():
            if (v):
                binary_blob = bytes(v, encoding=ENCODING)
                dset.attrs[k] = np.void(binary_blob)
                
        return [storage_path, dict]

        
    def get(self, storage_path):
        """
        Fetch items from dictionary in hdf5 using key

        Args:
            storage_path (string): Path to dataset in hdf5
            key (string): Key to access from path
        """
        try:
            key = storage_path.split('/')[-1]
            directory = storage_path.replace(key, '')

            dset = self.hdf[directory] # Get directory path without key
            out = dset.attrs[key] # Select key from directory

            binary_blob = out.tobytes() # Encode to bytes
            return binary_blob.decode(ENCODING) # Decode from bytes into string
        except KeyError:
            return None

    