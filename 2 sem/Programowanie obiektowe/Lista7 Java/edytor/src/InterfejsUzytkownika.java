//Karol Burczyk
//Programowanie obiektowe, lista 7
//Program pisałem i kompilowałem w IntelliJ IDEA.
// Wystarczy wrzucić obydwa pliki do jednego folderu i uruchomić program Main

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.io.*;
import java.util.Objects;

public class InterfejsUzytkownika {
    //klasa interfejsu graficznego
    public static void start(String typ, String plik) {
        //metoda uruchamiająca interfejs z argumentem, którym jest nazwa klasy,
        //którą chcemy edytować w interfejsie

        JFrame interfejs = new JFrame("Baza książek");
        //zdefiniowanie okna interfejsu

        JButton zapisz = new JButton("Zapisz");
        zapisz.setBounds(570, 50, 80, 20);
        interfejs.add(zapisz);
        //zdefiniowanie przycisku zapisania do pliku zewnętrznego i dodanie
        // do wywoływanego okna

        JButton pobierz = new JButton("Pobierz");
        pobierz.setBounds(570, 80, 80, 20);
        interfejs.add(pobierz);
        //zdefiniowanie przycisku pobrania z pliku zewnętrznego i dodanie do
        // wywoływanego okna

        JTextField f1 = new JTextField("Tytuł");
        f1.setBounds(50, 50, 70, 20);
        interfejs.add(f1);
        //pole z napisem tytuł

        JTextArea poleTekstowe1 = new JTextArea();
        poleTekstowe1.setBounds(130, 50, 200, 20);
        interfejs.add(poleTekstowe1);
        //pole tekstowe do wpisywania tytułu

        JTextField f2 = new JTextField("Autor");
        f2.setBounds(50, 80, 70, 20);
        interfejs.add(f2);
        //pole z napisem autor

        JTextArea poleTekstowe2 = new JTextArea();
        poleTekstowe2.setBounds(130, 80, 200, 20);
        interfejs.add(poleTekstowe2);
        //pole tekstowe do wpisywania autora


        JTextField f3 = new JTextField("Gatunek");
        f3.setBounds(50, 110, 70, 20);
        interfejs.add(f3);
        //pole z napisem gatunek

        JTextArea poleTekstowe3 = new JTextArea();
        poleTekstowe3.setBounds(130, 110, 200, 20);
        interfejs.add(poleTekstowe3);
        //pole tekstowe do wpisywania gatunku


        JTextArea poleTekstowe4 = new JTextArea();
        //zdefiniowania pola do wpisywania 4 argumentu klasy dla klas
        //Czasopismo i WydawnictwoCiagle

        if("Czasopismo".equals(typ))
        {
            //jeżeli wywołaliśmy interfejs dla Czasopisma,to dodajemy
            //tytuł Numer Czasopisma i edytujemy wcześniej zdefiniowane
            //4 pole tekstowe
            JTextField f4 = new JTextField("Numer czasopisma");
            f4.setBounds(50,140,70,20);
            interfejs.add(f4);

            poleTekstowe4.setBounds(130,140,200,20);
            interfejs.add(poleTekstowe4);
        }
        else if("WydawnictwoCiagle".equals(typ))
        {
            //analogicznie jak powyżej, jeżeli interfejs jest wywołany dla
            //WydawnictwoCiagle to dodajemy 4 pole
            JTextField f4 = new JTextField("Rok publikacji");
            f4.setBounds(50, 140, 70, 20);
            interfejs.add(f4);

            poleTekstowe4.setBounds(130, 140, 200, 20);
            interfejs.add(poleTekstowe4);
        }

        zapisz.addActionListener(new ActionListener() {
            //do przycisku zapisz dodajemy funkcjonalność
            public void actionPerformed(ActionEvent e) {
                //po wciśnięciu przycisku definiujemy obiekt klasy książka
                Ksiazka k;
                if("Czasopismo".equals(typ))
                //jeżeli wywołaliśmy interfejs dla Czasopisma, to pod k
                //definiujemy nowy obiekt Czasopismo z argumentami wywołania
                //pobranymi z pól w interfejsie
                {
                    k = new Czasopismo(poleTekstowe1.getText(), poleTekstowe2.getText(),
                            poleTekstowe3.getText(), Integer.parseInt(poleTekstowe4.getText()));
                }
                else if("WydawnictwoCiagle".equals(typ))
                //analogicznie dla WydawnictwaCiaglego
                {
                    k = new WydawnictwoCiagle(poleTekstowe1.getText(), poleTekstowe2.getText(),
                            poleTekstowe3.getText(), Integer.parseInt(poleTekstowe4.getText()));
                }
                else
                //w innym przypadku jest to po prostu obiekt klasy bazowej Ksiazka
                {
                    k = new Ksiazka(poleTekstowe1.getText(), poleTekstowe2.getText(),
                            poleTekstowe3.getText());
                }
                try
                {
                    FileOutputStream fileOut = new FileOutputStream(plik, true);
                    //pod fileOut definiujemy FileOutputStream z nazwą naszego
                    //pliku, do którego zapisujemy obiekty i poprzez argument
                    //true umożliwiamy dopisywanie kolejnych obiektów, bez
                    //usuwania poprzednich
                    ObjectOutputStream out = new ObjectOutputStream(fileOut);
                    //tworzymy strumień wychodzący obiektu out
                    out.writeObject(k);
                    //wypisujemy nasz obiekt do pliku
                    out.close();
                    //zamykamy strumień wyjściowy obiektów
                    fileOut.close();
                    //zamykamy strumień wyjściowy
                    System.out.println("Obiekt został zapisany do pliku " + plik);
                    //informujemy, jeżeli zapisanie się udało
                }
                catch (IOException wyjatek)
                {
                    //wyłapujemy wyjątki wyjścia
                    wyjatek.printStackTrace();
                }
            }
        });

        pobierz.addActionListener(new ActionListener() {
            //do przycisku pobierz dodajemy funkcjonalność
            public void actionPerformed(ActionEvent e) {
                try {
                    FileInputStream fileIn = new FileInputStream(plik);
                    ObjectInputStream in = new ObjectInputStream(fileIn);
                    //otwieramy strumień wejściowy obiektów
                    Object k = in.readObject();
                    //pod k zapisujemy obiekt pobrany z pliku
                    System.out.println(k.toString());
                    //dla naszego obiektu wywołujemy metodę toString i
                    //wypisujemy jego zawartość
                    if(k instanceof Czasopismo)
                    {
                        //jeżeli obiekt jest Czasopismem, to wpisujemy zawartość
                        //również do 4 pola
                        poleTekstowe4.setText("" + ((Czasopismo) k).numerMagazynu);
                    }
                    if(k instanceof WydawnictwoCiagle)
                    {
                        //analogicznie dla WydawnictwaCiaglego
                        poleTekstowe4.setText("" + ((WydawnictwoCiagle) k).rokWydania);
                    }
                    poleTekstowe1.setText(((Ksiazka)k).tytul);
                    poleTekstowe2.setText(((Ksiazka)k).autor);
                    poleTekstowe3.setText(((Ksiazka)k).gatunek);
                    //do pierwszych 3 pól wpisujemy zmienne tytul, autor oraz
                    //gatunek, które są zmiennymi we wszystkich klasach
                    in.close();
                    fileIn.close();
                    //zamykamy strumień wejściowy
                    System.out.println("Obiekt został pobrany z pliku " + plik);
                    //wypisujemy, jeżeli operacja się powiodła
                }
                //wszelkie wyjątki zwracamy poniżej
                catch (IOException i)
                {
                    i.printStackTrace();
                    System.out.println("exception 1");
                }
                catch (ClassNotFoundException ex)
                {
                    throw new RuntimeException(ex);
                }
            }
        });

        interfejs.setSize(800, 400);
        interfejs.setLayout(null);
        interfejs.setVisible(true);
        //ustawiamy wymiary okna i ustawiamy, żeby było widoczne
    }
}
