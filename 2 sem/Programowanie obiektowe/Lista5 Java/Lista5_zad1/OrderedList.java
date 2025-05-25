//Karol Burczyk
//Programowanie obiektowe, lista 5: zad. 1, program zawierający klasy
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

interface T extends Comparable<T>
        //interfejs comparable do porównywania elementów OrderList
{
    int get_t();
    //zwraca klucz sortowania
    @Override
    int compareTo(T object);
    //funkcja porównująca
}

public class OrderedList
{
    List<T> list = new ArrayList<>();
    //inicjacja nowej listy typu T
    //zdecydowałem się na domyślny konstruktor, dlatego nie tworzę własnego
    public void add_element(T elem)
    {
        //metoda dodająca nowy element do listy
        list.add(elem);
        Collections.sort(list);
        //po dodaniu sortujemy ponownie listę
    }
    public String get_first()
    //metoda zwracająca pierwszy element z listy
    {
        return list.get(0).getClass().getName();
        //zwracam nazwę klasy w stringu
    }
    public String to_String()
    //metoda zwracająca nazwy wszystkich elementów listy w formie
    //jednego stringa
    {
        String res = "";
        //tworzego stringa, do którego będę "doklejał" kolejne nazwy
        for (T elem : list) {
            res += elem.getClass().getName();
            //biorę nazwy elementów w stringach
            res += " ";
            //rozdzielam spacją
        }
        return res;
        //zwracam stringa "sklejonego" z nazw elementów listy
    }
}
//poniżej tworzę 4 klasy z nazwami kart
class As implements T
{
    @Override
    public int get_t() {
        return 14;
    }
    //każda zawiera "moc" karty w incie

    @Override
    public int compareTo(T other) {
        return Integer.compare(this.get_t(), other.get_t());
    }
    //compareTo zwraca porównanie na podstawie Intiger'a, który jest "mocą"
    //danej karty
}
class King implements T
{
    @Override
    public int get_t() {
        return 13;
    }

    @Override
    public int compareTo(T other) {
        return Integer.compare(this.get_t(), other.get_t());
    }
}
class Queen implements T
{
    @Override
    public int get_t() {
        return 12;
    }

    @Override
    public int compareTo(T other) {
        return Integer.compare(this.get_t(), other.get_t());
    }
}
class Jack implements T
{
    @Override
    public int get_t() {
        return 11;
    }

    @Override
    public int compareTo(T other) {
        return Integer.compare(this.get_t(), other.get_t());
    }
}
