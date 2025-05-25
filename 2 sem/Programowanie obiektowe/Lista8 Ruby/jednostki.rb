#Karol Burczyk
#Programowanie obiektowe, Lista 8, zadanie 1
#Program pisałem i uruchamiałem w wirtualn

class Masa
  #klasa Masa
  def initialize(x)
    #w konstruktorze przypisujemy kilogramy pod @kg
    @kg = x
  end
  def kilogram
    #metoda do wypisywania kilogramów (w każdym wypisaniu poniżej zaokrąglam)
    #do 2 miejsc po przecinku 
    @kg.round(2)
  end
  def funt
    #tutaj wypisuję funty (kg * 2,2) również w zaokrągleniu 
    (@kg * 2.2).round(2)
  end
end

class Dlugosc
  #klasa długości
  def initialize(x)
    #w konstruktorze przypisuję metry pod @m
    @m = x
  end
  def metr
    @m.round(2)
    #metoda do wypisywania długości w metrach
  end
  def cal
    (@m * 39.37).round()
    #wypisywanie cali (m * 39,37)
  end
end

class Powierzchnia
  #klasa Powierzchnia analogiczna do poprzednich z odpowiednimi przelicznikami
  def initialize(x)
    @hektar = x
  end
  def hektar
    @hektar.round(2)
  end
  def cal2
    (@hektar * 15503875.97).round(2)
  end
end

class Cisnienie
  #klasa Cisnienie
  def initialize(obszar, waga)
    #konstruktor z argumentami: waga i obszar
    @powierzchnia = Powierzchnia.new(obszar)
    #pole @powierzchnia jest obiektem klasy Powierzchnia z argumentem 
    #konstruktora: obszar
    @waga = Masa.new(waga)
    #analogiczna sytuacja dla @waga i Masa
  end
  def bary
    (@waga.kilogram * 9.81) / (@powierzchnia.hektar * 10000).round(2)
    #metoda bary zwraca kilogramy pomnożone przez wartość przyspieszenia 
    #ziemskiego 9,81 i dzieli przez hektary przeliczone na m^2
  end
  def psi
    ((@waga.kilogram * 9.81) / (@powierzchnia.hektar * 10000) * 14.503774).round(2)
    #metoda psi zwraca identyczną wartość jak bary, pomnożoną przez odpowiedni
    #przelicznik
  end
end

#Poniżej wypisuję tabelkę z jednej strony z jednostkami SI, a z drugiej
#anglosaskimi
print "SI   Imperialne \n"

c = Cisnienie.new(9.81, 10000)
print c.bary
print "  "
print c.psi
print "\n"

p = Powierzchnia.new(1.1)
print p.hektar
print "  "
print p.cal2
print "\n"

d = Dlugosc.new(1.1)
print d.metr
print "  "
print d.cal
print "\n"

m = Masa.new(1.1)
print m.kilogram
print "  "
print m.funt
print "\n"



    
