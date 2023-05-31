# Langchain Examples

## Overview

This repository consists of examples using langchain with Azure OpenAI.
The details of each example is recorded in each file.

## How to run

### Set up python enviroment

Highly recommend to leverage [anaconda](https://www.anaconda.com/) to set up
a clean python enviroment.

After installing anaconda, create a new enviroment:

```
conda create --name MYENV
```

Activate this enviroment **MYENV**,

```
conda activate MYENV
```

### Install required packages

In the new created conda enviroment **MYENV**, go to **src** folder, and install required
python packages.

```
pip install -r requirements.txt --user
```

### Set up Azure OpenAI connection

Rename file [api_key_example.py](./src/api_key_example.py) to **api_key.py**,
and update the values of **Az_OpenAI_api_key** and **Az_OpenAI_endpoint**.
Then you could begin to play the examples. Each example has a short description
of sample and the instruction to run the sample.
