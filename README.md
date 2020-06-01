# Raptor
Computer Vision Pytorch Project

## INSTALLATION

    // install virtualenv
    $ python3 -m pip install --user virtualenv

    // create environment
    $ python3 -m venv myenv

    // activate environment
    $ source myenv/bin/activate

    // install dependencies from requirements.txt
    $ pip install -r requirements.txt

    // deactivate environment
    $ deactivate

## Folder Structure
    .
    ├── train // define training 
    │   ├──
    │   ├── 
    │   └── 
    ├── test // define testing 
    │   ├──
    │   ├── 
    │   └── 
    │
    ├── configs // store networks configuration parameters
    │   ├── 
    │   └── 
    │
    ├── data // raw, processed data + test images
    │
    ├── experiments // store checkpoints, logs and outputs for experiment
    │   └── 
    │       ├── 
    │       └── 
    │
    ├── data // initialize and fetch dataset
    │   ├── dataset // defining custom dataset class
    │   ├── transformation // custom transformation class
    │   └── loader // data loader
    │       └── 
    │
    │
    ├── models // define our network
    │   ├── resnet_net.py
    │   ├── mnist_net.py
    │   └── utils.py
    │
    ├── notebooks // jupyter notebooks for experiments
    │   └── 
    │
    ├── utils // helper functions
    ├── README.md
    ├── requirements.txt
    ├── 
    └── 
