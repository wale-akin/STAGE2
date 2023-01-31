'''
Concrete IO class for a specific dataset
'''

# Copyright (c) 2017-Current Jiawei Zhang <jiawei@ifmlab.org>
# License: TBD

from code.base_class.dataset import dataset
from code.base_class.setting import setting
import numpy as np
import csv


class Dataset_Loader(dataset, setting):
    data = None
    dataset_source_folder_path = None
    dataset_source_file_name = None
    
    def __init__(self, dName=None, dDescription=None):
        super().__init__(dName, dDescription)
    
    def load(self):
        print('loading data...')
        X = []
        y = []
        f = open(self.dataset_source_folder_path + self.dataset_source_file_name, 'r')
        # strip the
        i = 0
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            elements = [int(i) for i in line[0].split(',')]
            # print(i, "\t", line)
            X.append(elements[1:]) # load features into list
            y.append(elements[0]) # load labels into list

        f.close()
        X = np.array(X) # change feature list into matrix
        y = np.array(y) # change # labels list into matrix
        print(X_train.shape)

        return {'X': X, 'y': y}
