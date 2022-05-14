import torch

x = torch.rand(2,2)
y = torch.rand(2,2)

print(x)
print(y)
print(x.size())

# Plus
z = x + y 
print(z)
print(torch.add(x,y))

# Subtract
z = x - y
print(z)
print(torch.sub(x, y))

# Multiply
z = x * y
print(z)
print(x.multiply(y))