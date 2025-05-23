import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.atomic.AtomicInteger;

class Task {
    public int l, r, m, parent;
    public boolean sort;

    public Task(boolean sort, int l, int r, int m, int parent) {
        this.sort = sort;
        this.l = l;
        this.r = r;
        this.m = m;
        this.parent = parent;
    }
}

class PoisonPill extends Task {
    public PoisonPill() {
        super(false, -1, -1, -1, -1);
    }
}

public class Main {
    public static void main(String[] args) {
        int[] array = {9, 4, 7, 2, 5, 8, 3, 5, 1, 3};
        int[] helper = new int[array.length];

        AtomicInteger sorted = new AtomicInteger(0);
        AtomicInteger[] sort_done = new AtomicInteger[array.length];

        for (int i = 0; i < array.length; i++) {
            sort_done[i] = new AtomicInteger(0);
        }

        AtomicInteger merge_index = new AtomicInteger(0);

        Task[] merges = new Task[array.length];

        LinkedBlockingQueue<Task> tasks = new LinkedBlockingQueue<>();

        int MAX_TASKS = 8;
        Thread[] workers = new Thread[MAX_TASKS];

        for (int i = 0; i < MAX_TASKS; i++) {
            workers[i] = new Thread(() -> {
                try {
                    while (true) {
                        Task t = tasks.take();

                        if (t instanceof PoisonPill) {
                            break;
                        }

                        // sort
                        if (t.sort) {
                            if (t.l == t.r) {
                                if (sort_done[t.parent].getAndIncrement() == 1) {
                                    tasks.put(merges[t.parent]);
                                }
                            } else {
                                int idx = merge_index.getAndIncrement();
                                t.m = (t.l + t.r) / 2;

                                merges[idx] = new Task(false, t.l, t.r, t.m, t.parent);

                                tasks.put(new Task(true, t.l, t.m, 0, idx));
                                tasks.put(new Task(true, t.m + 1, t.r, 0, idx));
                            }

                        // merge
                        } else {
                            int leftPosition = t.l;
                            int rightPosition = t.m + 1;
                            int arrPosition = t.l;

                            for (int j = t.l; j <= t.r; j++) {
                                helper[j] = array[j];
                            }

                            int leftEnd = t.m;
                            int rightEnd = t.r;

                            while (leftPosition <= leftEnd && rightPosition <= rightEnd) {
                                if (helper[leftPosition] <= helper[rightPosition]) {
                                    array[arrPosition++] = helper[leftPosition++];
                                } else {
                                    array[arrPosition++] = helper[rightPosition++];
                                }
                            }

                            while (leftPosition <= leftEnd) {
                                array[arrPosition++] = helper[leftPosition++];
                            }

                            while (rightPosition <= rightEnd) {
                                array[arrPosition++] = helper[rightPosition++];
                            }

                            if (t.parent == -1) {
                                sorted.getAndIncrement();
                            } else {
                                if (sort_done[t.parent].getAndIncrement() == 1) {
                                    tasks.put(merges[t.parent]);
                                }
                            }
                        }
                    }
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });

            workers[i].start();
        }

        try {
            tasks.put(new Task(true, 0, array.length - 1, 0, -1));

            while (sorted.get() == 0) {}

            for (int i = 0; i < MAX_TASKS; i++) {
                tasks.put(new PoisonPill());
            }

        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        for (Thread worker : workers) {
            try {
                worker.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        for (int i : array) {
            System.out.printf("%d ", i);
        }
    }
}
