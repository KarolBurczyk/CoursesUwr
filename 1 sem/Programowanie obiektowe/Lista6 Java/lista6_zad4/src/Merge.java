//Karol Burczyk
//Programowanie obiektowe, lista 6: zad. 4, program testowy
//Program pisałem i kompilowałem w IntelliJ IDEA.
// Wystarczy wrzucić obydwa pliki do jednego folderu i uruchomić program Main
public class Merge<Object extends Comparable<Object>>
    //klasa Merge z implementacją Comparable
{
    private Object[] array;
    //tablica obiektów typu Object
    public int length = 0;
    //długość tablicy

    public Merge(Object[] arr)
    {
        this.array = arr;
        length = arr.length;
        //konstruktor, który przypisuje tablicę i jej rozmiar pod zadeklarowane
        //powyżej zmienne
    }

    public int getLenght()
    {
        return length;
    }
    //funkcja zwracająca długość tablicy

    public Comparable[] getArray()
    {
        return array;
    }
    //funkcja zwracająca tablicę

    public void sort(int low, int high)
            //funkcja sortująca
    {
        if (low < high) {
            //jeżeli jest więcej niż jeden element to wykonujemy poniższe
            //operacje
            int mid = (low + high) / 2;
            //wyznaczamy środek tablicy

            Thread firstThread = new Thread(new Runnable() {
                public void run() {
                    sort(low, mid);
                }
            });
            Thread secondThread = new Thread(new Runnable() {
                public void run() {
                    sort(mid + 1, high);
                }
            });
            //towrzymy dwa wątki i pod każdego z nich przypisujemy sortowanie
            //jednej z dwóch połówek tablicy

            firstThread.start();
            secondThread.start();
            //uruchamiamy nasze wątki

            try {
                firstThread.join();
                secondThread.join();
                //czekamy na wykonanie każdego z nich
                merge(low, mid, high);
                //kiedy się wykonają
            } catch (InterruptedException exeption) {
                exeption.printStackTrace();
                //w razie przerwania wątku wyrzucamy wyjątek
            }
        }
    }

    public void merge(int low, int mid, int high) {
        //funkcja złączająca fragmenty list
        int i = low;
        //pod i zapisujemy dolny indeks pierwszej tablicy
        int j = mid + 1;
        //pod j zapisujemy dolny indeks drugiej tablicy
        int k = 0;
        //k będzie indeksem nowo utworzonej tablicy, która będzie zawierać dwie
        //już posortowane, których indeksy podaliśmy na wejściu

        Object[] temp = (Object[]) new Comparable[high - low + 1];
        //nowa tablica o rozmiarze dwóch, które łączymy

        while (i <= mid && j <= high) {
            //wykonujemy dopóki indeksy są mniejsze od górnych indeksów
            //naszych dwóch mniejszych tablicy
            if (array[i].compareTo(array[j]) < 0) {
                //jeżeli element o indeksie i jest mniejszy od elementu o
                // indeksie j, to przepisujemy i-ty element do temp
                temp[k++] = array[i++];
            } else {
                temp[k++] = array[j++];
                //w innym przypadku przpisujemy element o indeksie j do temp
            }
        }
        while (j <= high) {
            temp[k++] = array[j++];
        }
        //jeżeli indeks i zrównał się z mid, a j nie zrównał się z high, to
        //w pętli przepisujemy jeszcze dalej aż j nie dojdzie do high
        while (i <= mid) {
            temp[k++] = array[i++];
        }
        //analogicznie robimy jeżeli miała miejsce sytuacja odwrotna z i
        for (int x = 0; x < temp.length; x++) {
            array[low + x] = temp[x];
        }
        //przepisanie nowo utworzonej tablicy do tej zadeklarowanej w klasie
    }
    public void print()
            //metoda do drukowania tablicy
    {
        for(int i=0 ;i< array.length;i++)
        {
            System.out.print(array[i] + " ");
            //dla każdego indeksu tablicy wypisujemy wartość pod nim zapisaną
        }
        System.out.println();
        //drukuję pustą linię, żeby zwiększyć estetykę programu
    }
}