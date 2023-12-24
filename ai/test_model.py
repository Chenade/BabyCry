from my_model import DenseNet
import torch
from glob import glob
from dataprocessing.dataprocessing import *
import warnings
import sys
import random

warnings.filterwarnings("ignore")

def model_test(datas,labels,weights):
    net = DenseNet()
    net.load_state_dict(torch.load(weights))
    outputs = net(datas)
    k=[]
    acc = 0.
    total = 0.
    for output in outputs:
        if output[0]>output[1]:
            k .append(0)
        else:
            k.append(1)
    for i in range(len(labels)):
        if k[i] == labels[i].item():
            acc+=1
        total+=1
    accuracy = acc/total
    print('accuracy: ',acc/total)
    return accuracy


def model_test_single(audio_data, weights):
    net = DenseNet()
    net.load_state_dict(torch.load(weights))

    # return random 0 or 1 for now
    return random.randint(0, 1)

    # Assuming create_single_data processes the audio data
    input_data = create_single_data(audio_data)
    print("Input data shape:", input_data.shape)
    input_data = torch.from_numpy(input_data).float()
    input_data = input_data.unsqueeze(0)
    
    output = net(input_data)
    return output

if __name__=='__main__':
    if len(sys.argv) != 2:
        print("Usage: python use_model.py <path_to_wav_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    out = model_test_single(input_file,'./densenet.pth')
    if out[0][0]>out[0][1]:
        print(0)
    else:
        print(1)