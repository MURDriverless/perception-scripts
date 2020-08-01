import torch
from torch.autograd import Variable
from torch.backends import cudnn
from torch import nn
from keypoint_net import KeypointNet

import torch
from torch.autograd import Variable
from torch.backends import cudnn
from torch import nn

import argparse
import os
import sys

'''
Originally forked from
https://github.com/cv-core/MIT-Driverless-CV-TrainingInfra/blob/master/RektNet/pt_to_onnx.py

Adding support for converting to a dynamic shape ONNX model.
See below links for more information.

https://forums.developer.nvidia.com/t/tensorrt-engine-batch-inference-only-has-one-result/126017/5
https://gist.github.com/rmccorm4/b72abac18aed6be4c1725db18eba4930
'''

def main(weights_uri, onnx_name, opset):
    model = KeypointNet(7, (80, 80),onnx_mode=True)

    weights_path = weights_uri

    model.load_state_dict(torch.load(weights_path, map_location='cpu').get('model'))

    dummy_input = torch.randn(10, 3, 80, 80)

    input_names = [ "actual_input_1" ]
    output_names = [ "output1" ]

    # Fixed shape
    torch.onnx.export(model, dummy_input, onnx_name, verbose=True,
        opset_version=opset, input_names=input_names, output_names=output_names)

    # Dynamic shape
    dynamic_axes = {"actual_input_1":{0:"batch_size"}, "output1":{0:"batch_size"}}
    print(dynamic_axes)
    torch.onnx.export(model, dummy_input, "keypoints_dynamic.onnx", verbose=True,
        opset_version=opset, input_names=input_names, output_names=output_names,
        dynamic_axes=dynamic_axes)

    print("onnx file conversion succeed and saved at: " + onnx_name)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='.pt weights file convert to .onnx')

    parser.add_argument('--onnx_name', default='keypoints.onnx',
                        help='the name of output onnx file')

    parser.add_argument('--weights_uri', required=True,
                        help='Path to weights file')

    parser.add_argument('--opset', type=int, default=11, 
                        help="ONNX opset version to generate models with.")
    args = parser.parse_args()
    
    main(weights_uri=args.weights_uri, onnx_name=args.onnx_name, opset=args.opset)
