public class Context
{
    private Dictionary<string, bool> _variables = new();

    public bool GetValue(string name)
    {
        if (!_variables.ContainsKey(name))
            throw new Exception($"Brak wartości dla zmiennej '{name}'");
        return _variables[name];
    }

    public void SetValue(string name, bool value)
    {
        _variables[name] = value;
    }
}

public abstract class AbstractExpression
{
    public abstract bool Interpret(Context context);
}

public class ConstExpression : AbstractExpression
{
    private bool _value;
    public ConstExpression(bool value) => _value = value;

    public override bool Interpret(Context context) => _value;
}

public class VariableExpression : AbstractExpression
{
    private string _name;
    public VariableExpression(string name) => _name = name;

    public override bool Interpret(Context context) => context.GetValue(_name);
}

public class UnaryExpression : AbstractExpression
{
    private AbstractExpression _expression;
    public UnaryExpression(AbstractExpression expression) => _expression = expression;

    public override bool Interpret(Context context) => !_expression.Interpret(context);
}

public class BinaryExpression : AbstractExpression
{
    private AbstractExpression _left, _right;
    private string _op;

    public BinaryExpression(AbstractExpression left, AbstractExpression right, string op)
    {
        _left = left;
        _right = right;
        _op = op;
    }

    public override bool Interpret(Context context)
    {
        bool leftVal = _left.Interpret(context);
        bool rightVal = _right.Interpret(context);
        return _op switch
        {
            "AND" => leftVal && rightVal,
            "OR" => leftVal || rightVal,
            _ => throw new Exception($"Nieznany operator: {_op}")
        };
    }
}

class Program
{
    static void Main()
    {
        // klient
        Context ctx = new Context();
        ctx.SetValue("x", false);
        ctx.SetValue("y", true);    

        // !(x OR true)
        AbstractExpression expr = new UnaryExpression(
            new BinaryExpression(
                new VariableExpression("x"),
                new ConstExpression(true),
                "OR"
            )
        );

        bool result = expr.Interpret(ctx);  // zaróci false
        Console.WriteLine(result);
    }
}