#lang racket

(( lambda ( x y ) (+ x (* x y ) ) ) 1 2)
;oblicza sie do 3, bo 1*2+1 = 3
(( lambda ( x ) x ) ( lambda ( x ) x ) )
;lambda oblicza sie do samej siebie, czyli pokazuje procedure 
(( lambda ( x ) ( x x ) ) ( lambda ( x ) x ) )
;tutaj podobnie jak wyzej 
(( lambda ( x ) ( x x ) ) ( lambda ( x ) ( x x ) ) )
; ( x x)
;za (x x) podstawia sie:
;(( lambda ( x ) ( x x ) ) ( lambda ( x ) ( x x ) ))
;zatem otrzymujemy to co mielismy na poczatku i
;funkcja sie zapetla w nieskonczosnosc