import torch
import torch.multiprocessing as mp


def worker(rank, shared_tensor):
    for _ in range(100):
        shared_tensor[0] += 1


if __name__ == "__main__":
    mp.set_start_method("spawn", force=True)

    tensor = torch.zeros(4)
    tensor.share_memory_()

    processes = []

    for rank in range(4):
        p = mp.Process(
            target=worker,
            args=(rank, tensor)
        )
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("Final tensor:", tensor)