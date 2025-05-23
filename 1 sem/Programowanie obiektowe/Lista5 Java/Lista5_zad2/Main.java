//Karol Burczyk
//Programowanie obiektowe, lista 5: zad. 2, program testowy
//Program pisałem i kompilowałem w IntelliJ IDEA.
// Wystarczy wrzucić obydwa pliki do jednego folderu i uruchomić program Main

public class Main
{
    public static void main(String[] args)
    {
        Leaf.Variable.zmienne.put("x", 11.0);
        Leaf.Variable.zmienne.put("y", 9.5);
        Expression expr = new Root.Add(new Root.Add(new Leaf.Variable("x"), new Leaf.Const(3)),
                new Root.Add(new Leaf.Const(4), new Leaf.Const(3)));
        Expression expr1 = new Root.Subtraction(new Leaf.Const(4), new Leaf.Const(1));
        Expression expr2 = new Leaf.Variable("x");
        Expression expr3 = new Root.Subtraction(new Leaf.Variable("x"), new Leaf.Variable("y"));
        System.out.println(expr.evaluate());
        System.out.println(expr1.evaluate());
        System.out.println(expr2.evaluate());
        System.out.println(expr3.evaluate());
        System.out.println(expr.to_string());
        System.out.println(expr1.to_string());
        System.out.println(expr2.to_string());
        System.out.println(expr3.to_string());

    }
}