import torch
import torchvision
from transformation.augmentation import Augmentation
from transformation.train_albumentation import TrainAlbumentation
from transformation.test_albumentation import TestAlbumentation
SEED = 1

class DataSet:

  def __init__(self):
    augumentation_obj1 = Augmentation()
    self.train_album = TrainAlbumentation()
    self.test_album = TestAlbumentation()
    self.aug_transform = augumentation_obj1.getTransform()

  def getDataSet(self, train=False, dataset_name, transform):

      if dataset_name == 'CIFAR10':
          self.dataset = torchvision.datasets.CIFAR10(root='./data', train=train, download=True, transform=transform)
          return self.dataset
      elif dataset_name == 'MNIST':
          self.dataset = torchvision.datasets.MNIST(root='./data', train=train, download=True, transform=self.transform)
          return self.dataset
      