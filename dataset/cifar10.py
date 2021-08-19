from torchvision import transforms, datasets

mean = [0.4914005398750305, 0.4821619391441345, 0.44653016328811646]
std = [0.1952536255121231, 0.19247283041477203, 0.1941995918750763]

transform = transforms.Compose([transforms.Resize(224),
								transforms.ToTensor(),
                                transforms.Normalize(mean, std)])

train_dataset = datasets.CIFAR10(root='dataset', train=True, transform=transform, download=True)
valid_dataset = datasets.CIFAR10(root='dataset', train=False, transform=transform, download=True)
