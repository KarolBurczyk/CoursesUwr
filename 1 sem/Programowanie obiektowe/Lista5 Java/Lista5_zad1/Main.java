//Karol Burczyk
//Programowanie obiektowe, lista 5: zad. 1, program testowy
//Program pisałem i kompilowałem w IntelliJ IDEA.
// Wystarczy wrzucić obydwa pliki do jednego folderu i uruchomić program Main
public class Main {
    public static void main(String[] args)
    {
        OrderedList lista1 = new OrderedList();
        lista1.add_element(new As());
        lista1.add_element(new King());
        lista1.add_element(new Queen());
        lista1.add_element(new Jack());
        System.out.println(lista1.get_first());
        System.out.println(lista1.to_String());
    }
}