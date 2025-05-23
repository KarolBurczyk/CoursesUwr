//Karol Burczyk
//Programowanie obiektowe, lista 5: zad. 2, program zawierający klasy

import java.util.Hashtable;
//biblioteka do tablic haszowych, do zapisywania zmiennych
public class Expression
//klasa wyrażenia
{
    public double evaluate()
    //metoda zwracania wartości wyrażenia
    {
        return 0;
    }
    String to_string()
    //metoda zwracania wyrażenia zapisanego jako string
    {
        return null;
    }
}

class Leaf
//klasa liścia
{
    public static class Const extends Expression
        //podklasa liścia do zapisu stałych
    {
        double stala;
        public Const(double x)
                //konstruktor stałych
        {
            stala = x;
            //przypisanie jej wartości
        }
        public double evaluate() {
            return stala;
            //zwracamy zapisaną wartość
        }
        String to_string()
        {
            return Double.toString(stala);
            //zwracamy zapisaną wartość jako string
        }
    }
    public static class Variable extends Expression
            //podklasa liścia do zapisu zmiennych
    {
        String zmienna;
        //klucz zmiennej zapisujemy w tym miejscu pod stringiem
        static Hashtable<String, Double> zmienne = new Hashtable<>();
        //tworzona jest tablica z kluczami w postaci stringów i wartości
        //pod nimi zapisanych
        public Variable(String x)
        {
            //konstruktor, w którym zapisujemy klucz naszej zmiennej
            zmienna = x;
        }
        public double evaluate() {
            //przy wyliczaniu wartości wyrażenia zwracamy wartość zapisaną pod kluczem
            return zmienne.get(zmienna);
        }
        String to_string()
        {
            return zmienna;
            //do reprezentacji wyrażenia w stringu zwracamy klucz
        }
    }
}

class Root
    //klasa węzła
{
    public static class Add extends Expression
        //podklasa węzła odpowiadająca za dodawanie
    {
        Expression a;
        Expression b;
        //dwie zmienne Expression pod którymi zapisujemy dowolne dwa
        //podwyrażenia, które będziemy dodawać
        public Add(Expression x, Expression y)
        {
            a = x;
            b = y;
            //konstuktor definujący te podwyrażenia
        }
        public double evaluate() {
            return (a.evaluate() + b.evaluate());
            //chcąc uzyskać wartość wyrażenia wywołujemy funkcję evaluate
            //dla podwyrażeń, sumujemy je oraz zwracamy
        }
        String to_string()
        {
            return ("(" + a.to_string() + " + " + b.to_string() + ")");
            //zwracamy stringa stworzonego z podwyrażeń zamienionych na stringi
            //oddzielonych znakiem dodawania i ograniczonych nawiasami
            //(dla większej czytelnośći
        }
    }
    public static class Subtraction extends Expression
        //podklasa Root'a analogiczna do tej odpowiadającej za dodawanie
    {
        Expression a;
        Expression b;
        public Subtraction(Expression x, Expression y)
        {
            a = x;
            b = y;
        }
        public double evaluate() {
            return (a.evaluate() - b.evaluate());
        }
        String to_string()
        {
            return ("(" + a.to_string() + " - " + b.to_string() + ")");
        }
    }
}
