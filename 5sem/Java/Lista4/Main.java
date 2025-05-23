import obliczenia.*;

public class Main {
   
   public Main() {}

   public static void main(String[] args) {
      
      Zmienna.ustawZmienna("x", 1.618);

      Wyrazenie expr1 = new Odejm(
         new Dod(
            new Liczba(7.0), 
            new Mnoz(new Liczba(5.0), new Liczba(3.0))
         ), 
         new Liczba(1.0)
      );
      System.out.println(expr1 + " = " + expr1.oblicz());

      Wyrazenie expr2 = new Mnoz(
         new Przec(
            new Odejm(new Liczba(2.0), new Zmienna("x"))
         ), 
         new E()
      );
      System.out.println(expr2 + " = " + expr2.oblicz());

      Wyrazenie expr3 = new Dziel(
         new Odejm(
            new Mnoz(new Liczba(3.0), new Pi()), 
            new Liczba(1.0)
         ), 
         new Dod(
            new Odwr(new Zmienna("x")), 
            new Liczba(5.0)
         )
      );
      System.out.println(expr3 + " = " + expr3.oblicz());

      Wyrazenie expr4 = new Sin(
         new Dziel(
            new Mnoz(
               new Dod(new Zmienna("x"), new Liczba(13.0)), 
               new Pi()
            ), 
            new Odejm(new Liczba(1.0), new Zmienna("x"))
         )
      );
      System.out.println(expr4 + " = " + expr4.oblicz());

      Wyrazenie expr5 = new Dod(
         new Exp(new Liczba(5.0)), 
         new Mnoz(
            new Zmienna("x"), 
            new Log(new E(), new Zmienna("x"))
         )
      );
      System.out.println(expr5 + " = " + expr5.oblicz());

   }

}
