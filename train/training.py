from tqdm import tqdm
import torch
import torch.nn.functional as F
import torch.nn as nn


train_losses = []

def train(model, device, train_loader, optimizer, epoch, criterion):
    model.train()
    pbar = tqdm(train_loader)
    
    for batch_idx, (data, target) in enumerate(pbar):
        
        correct = 0
        processed = 0
    
        # get samples
        data, target = data.to(device), target.to(device)

        # Init
        optimizer.zero_grad()
        # In PyTorch, we need to set the gradients to zero before starting to do backpropragation because PyTorch accumulates the gradients on subsequent backward passes. 
        # Because of this, when you start your training loop, ideally you should zero out the gradients so that you do the parameter update correctly.

        # Predict
        y_pred = model(data)

        # Calculate loss
        # loss = F.nll_loss(y_pred, target)
        #criterion = nn.CrossEntropyLoss()
        loss = criterion(y_pred, target)

        train_losses.append(loss)

        # Backpropagation
        loss.backward()
        optimizer.step()

        # Update pbar-tqdm

        pred = y_pred.argmax(dim=1, keepdim=True)  # get the index of the max log-probability
        correct += pred.eq(target.view_as(pred)).sum().item()
        processed += len(data)

        pbar.set_description(desc= f'Loss={loss.item()} Batch_id={batch_idx} Accuracy={100*correct/processed:0.2f}')
        # pbar.update(1)
    
    train_acc = 100*correct/processed

    return train_acc
