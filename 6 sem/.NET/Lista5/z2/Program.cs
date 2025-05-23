using System;
using System.Dynamic;
using System.Linq.Expressions;

public class MyDynamic : DynamicObject
{
    private Dictionary<string, object> _members = new();
    private Dictionary<int, object> _index = new();

    public override bool TrySetMember(SetMemberBinder binder, object value)
    {
        _members[binder.Name] = value;
        return true;
    }

    public override bool TryGetMember(GetMemberBinder binder, out object result)
    {
        return _members.TryGetValue(binder.Name, out result);
    }

    public override bool TrySetIndex(SetIndexBinder binder, object[] indexes, object value)
    {
        _index[(int)indexes[0]] = value;
        return true;
    }

    public override bool TryGetIndex(GetIndexBinder binder, object[] indexes, out object result)
    {
        return _index.TryGetValue((int)indexes[0], out result);
    }

    public override bool TryInvoke(InvokeBinder binder, object[] args, out object result)
    {
        result = "Called as function!";
        return true;
    }

    public override bool TryInvokeMember(InvokeMemberBinder binder, object[] args, out object result)
    {
        result = $"Called method: {binder.Name}";
        return true;
    }

    public override bool TryUnaryOperation(UnaryOperationBinder binder, out object result)
    {
        if (binder.Operation == ExpressionType.Negate)
        {
            result = "- negated";
            return true;
        }
        result = null;
        return false;
    }

    public override bool TryBinaryOperation(BinaryOperationBinder binder, object arg, out object result)
    {
        if (binder.Operation == ExpressionType.Add)
        {
            result = "added " + arg;
            return true;
        }
        result = null;
        return false;
    }
}


public class Program
{
    static void Main()
    {
        dynamic obj = new MyDynamic();
        obj.Name = "X";
        Console.WriteLine(obj.Name);

        obj[0] = 420;
        Console.WriteLine(obj[0]);

        Console.WriteLine(obj());
        Console.WriteLine(obj.DoSomething());
        Console.WriteLine(-obj);
        Console.WriteLine(obj + " test");
    }
}