import numpy as numpy
import matplotlib.pyplot as plt

# Function to visualize the images
def imshow(img):
    img = img / 2 + 0.5
    npimg = img.numpy() #converting tensor to numpy as matplotlib support only numpy
    plt.imshow(np.transpose(npimg, (1, 2, 0)))


# Function to plot the Training and Test Accuracy 
def plot_graph(train_acc, test_acc):
    fig, axs = plt.subplots(2)
    axs[0].plot(train_acc)
    axs[0].set_title("Train Accuracy")
    axs[0].set_xlabel("Batch")
    axs[0].set_ylabel("Accuracy")
    axs[1].plot(test_acc)
    axs[1].set_title("Test Accuracy")
    axs[1].set_xlabel("Batch")
    axs[1].set_ylabel("Accuracy")