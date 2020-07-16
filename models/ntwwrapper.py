import torch 
import torch.nn as nn
import attention as attn
import numpy as np

def inputs(n):
    
    base_size = 2
    vec = np.arange(n)
    x, y = vec[0], vec[int(n/2)]
    
    B_keys = torch.Tensor(base_size+x)
    mem_z = torch.Tensor(y)
    padding = torch.zeros(mem_z.shape)    
    padding[:B_keys.shape[0]] = B_keys 
    return padding, mem_z, torch.dot(padding, mem_z )

def precieve_attn(inp):
    key_z, mem_z, dot = inp 
    size = key_z.shape[0]
    
    hidden = 1 if len(key_z.shape) < 2 else key_z.shape[1]
    
    base=attn.memory_attention(size, size, hidden) 
    base.forward(mem_z,mem_z)
    return base.insideForward()

def demo_train(d1,d2):
    inp = inputs
    x,y  =  precieve_attn(inp(d1)), precieve_attn(inp(d2))
    print(x,y)
    while x!=y:

        x,y  =  precieve_attn(inp(10)), precieve_attn(inp(5))
        print(x,y)


demo_train(10,20)
