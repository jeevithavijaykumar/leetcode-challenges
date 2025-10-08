# Create a DataProcessor class that handles numerical data analysis:

import numpy as np

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def get_stats(self):

        self. result = {}
        mean = float(np.mean(self.data))
        median = float(np.median(self.data))
        std_dev = float(np.std(self.data))

        self.result['mean'] = round(mean, 2)
        self.result['median'] = round(median, 2)
        self.result['std_dev'] = round(std_dev, 2)

        return self.result

    def filter_outliers(self, threshold=2):

        if not self.result:
            self.get_stats()

        lower_bound = self.result['mean'] - threshold * (self.result['std_dev'])
        upper_bound = self.result['mean'] + threshold * (self.result['std_dev'])

        return [ num for num in self.data if num >= lower_bound and num <= upper_bound]


processor = DataProcessor([1, 2, 3, 4, 5, 100])
stats = processor.get_stats()
print('Stats:', stats)
filtered = processor.filter_outliers(threshold=2)
print('Data after filtering:' , filtered)