import torch
import torch.nn as nn
import torch.optim as optim
import torch.multiprocessing as mp
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.utils.data import Dataset, DataLoader
from torch.utils.data.distributed import DistributedSampler


# Dataset
class RandomDataset(Dataset):
    def __init__(self, size, length):
        self.data = torch.randn(length, size)
        self.targets = torch.randn(length, 1)

    def __getitem__(self, index):
        return self.data[index], self.targets[index]

    def __len__(self):
        return len(self.data)


# DDP setup
def setup(rank, world_size):
    dist.init_process_group(
        backend="gloo",
        init_method="tcp://127.0.0.1:29500",
        rank=rank,
        world_size=world_size
    )

# DDP cleanup
def cleanup():
    dist.destroy_process_group()


# Training function
def train(rank, world_size):
    print(f"Rank {rank} starting")

    setup(rank, world_size)

    # Dataset + DistributedSampler
    dataset = RandomDataset(size=10, length=1000)
    sampler = DistributedSampler(dataset, num_replicas=world_size, rank=rank)

    # DataLoader with multiple workers
    dataloader = DataLoader(
        dataset,
        batch_size=32,
        sampler=sampler,
        num_workers=4
    )

    # Model
    model = nn.Linear(10, 1)
    model = DDP(model)
    model.train()

    optimizer = optim.SGD(model.parameters(), lr=0.01)
    criterion = nn.MSELoss()

    for epoch in range(2):
        sampler.set_epoch(epoch)

        for x, y in dataloader:
            optimizer.zero_grad()
            output = model(x)
            loss = criterion(output, y)
            loss.backward() 
            optimizer.step()

        print(f"Rank {rank}, Epoch {epoch}, Loss {loss.item():.4f}")

    cleanup()


# Entry point
if __name__ == "__main__":
    mp.set_start_method("spawn", force=True)

    WORLD_SIZE = 2

    mp.spawn(
        train,
        args=(WORLD_SIZE,),
        nprocs=WORLD_SIZE,
        join=True
    )