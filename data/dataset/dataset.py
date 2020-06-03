import torch
import torchvision
from transformation.augmentation import Augmentation
SEED = 1

class DataSet:

  def __init__(self):
    augumentation_obj1 = Augmentation()
    self.transform = augumentation_obj1.getTransform()

  def getDataSet(self, train=False, dataset_name):

      if dataset_name == 'CIFAR10':
          self.dataset = torchvision.datasets.CIFAR10(root='./data', train=train, download=True, transform=self.transform)
          return self.dataset
      elif dataset_name == 'MNIST':
          self.dataset = torchvision.datasets.MNIST(root='./data', train=train, download=True, transform=self.transform)
          return self.dataset
      