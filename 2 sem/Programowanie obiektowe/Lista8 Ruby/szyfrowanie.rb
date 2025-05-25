#Karol Burczyk
#Programowanie obiektowe, Lista 8, zadanie 4
#Program pisałem i uruchamiałem w witrynie internetowej ReplIt

class Jawna
  #klasa jawna
  def initialize(x)
    #konstruktor klasy Jawna z jedynm argumentem
    @tekst = x
    #argument z konstruktora przypisujemy do pola klasy @tekst
  end
  def Jawna=(x)
    @tekst = x.tekst
    #operator przypisania 
  end
  def zaszyfruj(key)
    #metoda do zaszyfrowania jawnego tekstu ze słownikiem jako argumentem
    s = ""
    i = 0 
    while i < @tekst.length
      #dla każdej litery w tekście szukamy wartości mu przypisanej w słowniku
        s = s + key[@tekst[i]]
        # 'doklejamy' zaszyfrowaną literkę do s
        i = i + 1
    end
    szyfr = Zaszyfrowana.new(s.to_s)
    #na koniec pod 'szyfr' zapisujemy obiekt klasy Zaszyfrowana z argumentem s
    #zamienionym na ciąg znaków
    szyfr
    #zwracamy nowo utworzony obiekt
  end
  def to_s
    @tekst.to_s
    #metoda zwracjąca tekst jawny
  end
  
end

class Zaszyfrowana
  #klasa Zaszyfrowana identyczna z Jawna
  def initialize(x)
    @tekst = x
  end
  def Zaszyfrowana=(x)
    @tekst = x.tekst
  end
  def odszyfruj(klucz)
    s = ""
    i = 0 
    while i < @tekst.length
      s = s + klucz.key(@tekst[i])
      #jedyną różnicą jest to, że w słowniku szukamy klucza, który odpowiada
      #podanej przez nas wartości, żeby prawidłowo odszyfrować tekst
      i = i + 1
    end
    odszyfrowany = Jawna.new(s.to_s)
    odszyfrowany
  end
  def to_s
    @tekst
  end
end

#przykładowy słownik, dla którego przeprowadzałem testy
kodowanie = 
{
  'a' => 'b',
  'b' => 'c',
  'c' => 'd',
  'd' => 'e',
  'e' => 'f',
  'f' => 'g',
  'g' => 'h',
  'h' => 'i',
  'i' => 'j',
  'j' => 'k',
  'k' => 'l',
  'l' => 'm',
  'm' => 'n',
  'n' => 'o',
  'o' => 'p',
  'p' => 'r',
  'r' => 's',
  's' => 't',
  't' => 'u',
  'u' => 'w',
  'w' => 'x',
  'x' => 'y',
  'y' => 'z',
  'z' => 'a',
}

#tworzę nowy obiekt t klasy Jawna z argumentem "ruby"
t = Jawna.new("ruby")
puts t.to_s
#wypisuję tekst w obecnej formie
ts = Zaszyfrowana.new("nic")
#tworzę nowy obiekt klasy Zaszyfrowana z argumentem "nic"
ts = t.zaszyfruj(kodowanie)
#przypisuję mu zaszyfrowany tekst z obiektu zapisengo pod t
puts ts.to_s
#wypisuję zaszyfrowany tekst
tx = Jawna.new("nic")
#kolejny obiekt klasy Jawna
tx = ts.odszyfruj(kodowanie)
#przypisuję odszyfrowany tekst pod tx
puts tx.to_s
#wypisuję odszyfrowany tekst

