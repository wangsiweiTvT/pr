import torch

# 构造两个Tensor
x = torch.tensor([1.0, 2.0], requires_grad=True)
y = torch.tensor([1.0, 2.0], requires_grad=True)

# 模拟网络计算过程
z = x ** 2 + y ** 2
# z = z.sum()

# 反向传播
z.backward()

# 得到梯度
print(f"gradient of x is:{x.grad}")
print(f"gradient of y is:{y.grad}")

# 梯度裁剪
torch.nn.utils.clip_grad_norm_([x, y], max_norm=10, norm_type=2)

# 再次打印裁剪后的梯度
# 直接修改了原x.grad的值
print("---clip_grad---")
print(f"clip_grad of x is:{x.grad}")
print(f"clip_grad of y is:{y.grad}")

