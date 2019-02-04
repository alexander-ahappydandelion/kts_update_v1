import numpy as np
import mprop

seed = 31337
np.random.seed(seed)
seeds = np.random.randint(100, size=10)

storage_path = '../storage/'
index_prefix = "__kts__index_"
test_call = 0


@property
def feature_path(config):
    return storage_path + 'features/'


@property
def info_path(config):
    return storage_path + 'info/'


@property
def souce_path(config):
    return storage_path + 'sources'


mprop.init()
