using System;
using System.Collections;
using System.Collections.Generic;

public class BinaryTree<T>
{
    public T Value { get; set; }
    public BinaryTree<T> Left { get; set; }
    public BinaryTree<T> Right { get; set; }

    public BinaryTree(T value)
    {
        Value = value;
        Left = null;
        Right = null;
    }

    public IEnumerable<T> DepthFirstTraversal()
    {
        yield return Value;

        if (Left != null)
        {
            foreach (var value in Left.DepthFirstTraversal())
            {
                yield return value;
            }
        }

        if (Right != null)
        {
            foreach (var value in Right.DepthFirstTraversal())
            {
                yield return value;
            }
        }
    }

    public IEnumerable<T> BreadthFirstTraversal()
    {
        Queue<BinaryTree<T>> queue = new Queue<BinaryTree<T>>();
        queue.Enqueue(this);

        while (queue.Count > 0)
        {
            BinaryTree<T> node = queue.Dequeue();
            yield return node.Value;

            if (node.Left != null)
            {
                queue.Enqueue(node.Left);
            }

            if (node.Right != null)
            {
                queue.Enqueue(node.Right);
            }
        }
    }
}

class main
{
    static void Main()
    {
        BinaryTree<int> root = new BinaryTree<int>(1)
        {
            Left = new BinaryTree<int>(2)
            {
                Left = new BinaryTree<int>(4),
                Right = new BinaryTree<int>(5)
            },
            Right = new BinaryTree<int>(3)
            {
                Left = new BinaryTree<int>(6),
                Right = new BinaryTree<int>(7)
            }
        };

        Console.WriteLine("DFS (InOrder):");
        foreach (var value in root.DepthFirstTraversal())
        {
            Console.Write(value + " ");
        }
        Console.WriteLine();

        Console.WriteLine("BFS:");
        foreach (var value in root.BreadthFirstTraversal())
        {
            Console.Write(value + " ");
        }
        Console.WriteLine();
    }
}