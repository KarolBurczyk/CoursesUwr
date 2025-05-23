import figury.*;

public class TestFigur {
    public static void main(String[] args) {
        
        Wektor v = new Wektor(1, 1);
        
        Prosta prosta1 = new Prosta(1, -1, 0); // y = x      
        Prosta prosta2 = new Prosta(1, -1, 1); // y = x + 1 (równoległa do prosta1)
        Prosta prosta3 = new Prosta(-1, -1, 2); // y = -x + 2 (prostopadła do prosta1)  
        
        Punkt punktObrotu = new Punkt(1, 1);
        double kat = 90; 


        System.out.println("Czy prosta1 jest równoległa do prosta2? " + Prosta.czyRownolegle(prosta1, prosta2));
        System.out.println("Czy prosta1 jest prostopadła do prosta3? " + Prosta.czyProstopadle(prosta1, prosta3));
        
        Punkt punktPrzeciecia1 = Prosta.punktPrzeciecia(prosta1, prosta3);
        if (punktPrzeciecia1 != null) {
            System.out.println("Punkt przecięcia prosta1 i prosta3: " + punktPrzeciecia1);
        } else {
            System.out.println("Proste są równoległe, nie mają punktu przecięcia.");
        }
        Punkt punktPrzeciecia2 = Prosta.punktPrzeciecia(prosta2, prosta3);
        if (punktPrzeciecia2 != null) {
            System.out.println("Punkt przecięcia prosta1 i prosta3: " + punktPrzeciecia2);
        } else {
            System.out.println("Proste są równoległe, nie mają punktu przecięcia.");
        }



        Punkt p1 = new Punkt(0, 0);
        Punkt p2 = new Punkt(3, 0);
        Punkt p3 = new Punkt(1, 5);
        Trojkat trojkat = new Trojkat(p1, p2, p3);

        System.out.println("Trójkąt przed przesunięciem: " + trojkat);
        trojkat.przesun(v);
        System.out.println("Trójkąt po przesunięciu: " + trojkat);
        trojkat.odbij(prosta1);
        System.out.println("Trójkąt po odbiciu: " + trojkat);
        trojkat.obroc(punktObrotu, kat);
        System.out.println("Trójkąt po obrocie: " + trojkat);

        

        Punkt p4 = new Punkt(10, 20);
        Punkt p5 = new Punkt(20, 20);
        Odcinek odcinek = new Odcinek(p4, p5);

        System.out.println("Odcinek przed przesunięciem: " + odcinek);
        odcinek.przesun(v);
        System.out.println("Odcinek po przesunięciu: " + odcinek);
        odcinek.odbij(prosta1);
        System.out.println("Odcinek po odbiciu: " + odcinek);
        odcinek.obroc(punktObrotu, kat);
        System.out.println("Odcinek po obrocie: " + odcinek);
    }
}
