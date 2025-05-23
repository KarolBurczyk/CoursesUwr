import java.io.Console;
//Karol Burczyk
//Programowanie obiektowe, lista 6: zad. 4, program testowy
//Program pisałem i kompilowałem w IntelliJ IDEA.
// Wystarczy wrzucić obydwa pliki do jednego folderu i uruchomić program Main
public class Main {
    public static void main(String[] args)
    {
        Merge a = new Merge(new Comparable []{"a", "b", "avd", "xyz", "pppp", "pp", "pad", "dddo"});
        System.out.println("Przed sortowaniem: ");
        a.print();
        System.out.println();
        a.sort(0, a.getLenght()-1);
        System.out.println("Po sortowaniu: ");
        a.print();
        System.out.println();

        Merge b = new Merge(new Comparable []{99, 78, 11, -1, 9, 88, 19, 52, -14});
        System.out.println("Przed sortowaniem: ");
        b.print();
        System.out.println();
        b.sort(0, b.getLenght()-1);
        System.out.println("Po sortowaniu: ");
        b.print();
    }
}