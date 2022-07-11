import torch
x = torch.rand(5, 3)
print(x)
if torch.cuda.is_available():
    print("CUDA ENABLED!!!!!")
