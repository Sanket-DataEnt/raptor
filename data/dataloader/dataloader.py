import torch
import torchvision

from dataset.dataset import Data

class DataLoader:

    def __init__(self):
        data_obj = DataSet()
        self.dataset = data_obj.getDataSet()

    def getDataLoader(self, dataset, batch_size):
    # checking CUDA
    self.cuda = torch.cuda.is_available()
    # For reproducibility
    torch.manual_seed(SEED)
    if self.cuda:
      torch.cuda.manual_seed(SEED)

    # dataloader arguments - something you'll fetch these from cmdprmt
    ## These configurations have to be shifted to another file 
    dataloader_args = dict(shuffle=True, num_workers=4, pin_memory=True) if self.cuda else dict(shuffle=True, batch_size=32)

    # train dataloader
    self.dataset_loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, **dataloader_args)

    return self.dataset_loader

