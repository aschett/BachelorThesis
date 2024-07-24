# BachelorThesis

## Overview

This repository contains the code and data for my bachelor thesis project, which focuses on fine-tuning machine learning models to predict the memorability of text. The project involves preprocessing data, training and fine-tuning models, and evaluating their performance. The scripts are provided as Jupyter Notebooks.

## Preconditions

1. You have to download the dataset from [here](https://www.cs.cornell.edu/~cristian/memorability_files/cornell_movie_quotes_corpus.zip) and have to extract it. Afterwards create a new folder in the root called "dataset" and put the file from the archive with the name "moviequotes.memorable_nonmemorable_pairs.txt" in there.

## Datasets

The dataset used in this project can be found and downloaded [here](https://www.cs.cornell.edu/~cristian/memorability.html).

## Setting Up Environment for Fine-Tuning Llama3 with UnsLoth

### Step 1: Install CUDA
Download and install CUDA to ensure your environment is prepared for fine-tuning. Refer to the official [CUDA installation guide](https://github.com/sithu31296/CUDA-Install-Guide) for detailed instructions.

### Step 2: Download Llama3
Download Llama3 and its weights from the [Llama GitHub repository](https://github.com/meta-llama/llama3).

### Step 3: Create a Conda Environment
Create a new Conda environment specifically for fine-tuning Llama3.

```shell
conda create -n finetune_llama3_unsloth python=3.10
```

### Step 4: Install UnsLoth Framework
Follow the installation steps to set up UnsLoth for fine-tuning. Refer to the [UnsLoth GitHub repository](https://github.com/unslothai/unsloth) for download and installation details.

#### Step 4.1 Install Pytorch and CUDA
Install the necessary PyTorch and CUDA packages.

```shell
conda install pytorch-cuda=<12.1/11.8> pytorch cudatoolkit xformers -c pytorch -c nvidia -c xformers
```

#### Step 4.2: Install UnsLoth
Install the UnsLoth framework from the GitHub repository.

```shell
pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
```

#### Step 4.3 Install Additional Dependencies
Install additional necessary packages.

```shell
pip install --no-deps trl peft accelerate bitsandbytes
pip install scikit-learn
```

### Step 5: Activate the Environment
Activate your newly created Conda environment.

```shell
conda activate finetune_llama3_unsloth
```

