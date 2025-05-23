#lang racket

( let ([ x 3]) 
   (+ x y ) ) ;zwiazany x, y pozostaje przy wartosci globalnej 

( let ([ x 1]
       [ y (+ x 2) ])
   (+ x y ) ) ;zwiazany x i y, bo x jest definiowany jako 1, a y przyjmuje wartosc x+2
;dla globalnej wartosci x

( let ([ x 1])
   ( let ([ y (+ x 2) ])
      (* x y ) ) ) ;zwiazany x i y, bo y=x+2 znajduje sie w ciele poprzedniego let
;dlatego x zachowuje wartosc 1

( define ( f x y )
   (* x y z ) ) ;zadna zmienna nie jest zwiazana, wszystkie przyjmuja wartosci globalne

( define ( f x )
   ( define ( g y z )
      (* x y z ) )
   ( f x x x ) ) ;zwiazane jest g, zdefiniowane w funkcji f, reszta przyjmuje wartosci globalne