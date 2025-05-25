#lang plait
( define ( apply f x ) ( f x ) )
;jako argumenty podajemy funkcję f i jakiś argument x, który jest również argumentem
;funkcji f, zatem zwracanym typem jest tym zwracany przez funkcję f
;(('a -> 'b) 'a -> 'b)
( define ( compose f g ) ( lambda ( x ) ( f ( g x ) ) ) )
;do funkcji compose wrzucamy dwie funkcje f i g, a zwracamy ich złączenie f(g(x))
;(('a -> 'b) ('c -> 'a) -> ('c -> 'b))
( define ( flip f ) ( lambda ( x y ) ( f y x ) ) )
;(('a 'b -> 'c) -> ('b 'a -> 'c))
;wywołuje funkcję f dla podanych argumentów ale w odwróconej kolejnosći
( define ( curry f ) ( lambda ( x ) ( lambda ( y ) ( f x y ) ) ) )
;(('a 'b -> 'c) -> ('a -> ('b -> 'c)))
;jako argument dostajemy funkcję, do której dostajemy 2 argumenty i konwertujemy ją na
;funkcję jednoargumentową, która zwraca funkcję jednoargumentową