import numpy as np

def load_npz_data(in_file):
    copy_data = np.load(in_file)['arr_0']
    print(copy_data.shape)
    return copy_data