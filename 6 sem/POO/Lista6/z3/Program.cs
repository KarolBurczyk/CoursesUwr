public abstract class Tree { }

public class TreeNode : Tree
{
    public Tree Left { get; set; }
    public Tree Right { get; set; }
}

public class TreeLeaf : Tree
{
    public int Value { get; set; }
}

public abstract class TreeVisitor
{
    public abstract int Visit(Tree tree);
    public abstract int VisitNode(TreeNode node);
    public abstract int VisitLeaf(TreeLeaf leaf);
}

public class DepthVisitor : TreeVisitor
{
    public override int Visit(Tree tree)
    {
        if (tree is TreeNode node)
            return VisitNode(node);
        if (tree is TreeLeaf leaf)
            return VisitLeaf(leaf);
        return 0;
    }

    public override int VisitNode(TreeNode node)
    {
        int leftDepth = node.Left != null ? Visit(node.Left) : 0;
        int rightDepth = node.Right != null ? Visit(node.Right) : 0;
        return 1 + Math.Max(leftDepth, rightDepth);
    }

    public override int VisitLeaf(TreeLeaf leaf)
    {
        return 1;
    }
}

class Program
{
    static void Main()
    {
        Tree root = new TreeNode()
        {
            Left = new TreeNode()
            {
                Left = new TreeLeaf() { Value = 1 },
                Right = new TreeLeaf() { Value = 2 }
            },
            Right = new TreeLeaf() { Value = 3 }
        };

        DepthVisitor depthVisitor = new DepthVisitor();
        int depth = depthVisitor.Visit(root);
        Console.WriteLine($"Głębokość drzewa: {depth}");
    }
}
