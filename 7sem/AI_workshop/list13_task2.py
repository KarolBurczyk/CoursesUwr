import time
import torch
import torch.multiprocessing as mp

def x(n: int) -> float:
    """
    Costly numerical function.
    """
    t = torch.randn(n)
    for _ in range(5):
        t = t * t + 1.0
    return t.sum().item()

def run_sequential(tasks: int, n: int) -> float:
    """
    Run function x sequentially.
    Returns execution time.
    """
    start = time.time()

    for _ in range(tasks):
        x(n)

    end = time.time()
    return end - start

def run_multiprocessing(tasks: int, n: int, workers: int) -> float:
    """
    Run function x using multiprocessing POOL (szybkie!).
    Returns execution time.
    """
    start = time.time()

    with mp.Pool(processes=workers) as pool:
        _ = pool.map(x, [n] * tasks)
    
    end = time.time()
    return end - start

if __name__ == "__main__":
    mp.set_start_method("spawn", force=True)

    TASKS = 8           # liczba zadań
    N = 50_000_000      # 10x WIĘKSZY workload (było 5M)
    WORKERS = 8         # Dopasowane do typowego CPU (sprawdź: nproc
    
    t_seq = run_sequential(TASKS, N)
    t_mp = run_multiprocessing(TASKS, N, WORKERS)

    print("\n=== SUMMARY ===")
    print(f"Sequential:      {t_seq:.2f} s")
    print(f"Multiprocessing: {t_mp:.2f} s")
    print(f"Speedup:         {t_seq / t_mp:.2f}x")
