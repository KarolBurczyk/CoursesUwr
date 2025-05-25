#lang plait
( define ( apply f x ) ( f x ) )
( define ( compose f g ) ( lambda ( x ) ( f ( g x ) ) ) )
( define ( flip f ) ( lambda ( x y ) ( f y x ) ) )
( define ( curry f ) ( lambda ( x ) ( lambda ( y ) ( f x y ) ) ) )

(define (add1 x) (+ x 1))
(define (mult2 x) (* x 2))


;( curry compose )
;curry: (('a 'b -> 'c) -> ('a -> ('b -> 'c)))
;compose: (('x -> 'y) ('z -> 'x) -> ('z -> 'y))
;zatem skoro funkcja compose jest argumentem curry, to podstawiamy:
;'a = ('x -> 'y)
;'b =  ('z -> 'x)
;'c = ('z -> 'y)
;i otrzymujemy w typie:
;(('x -> 'y) -> (('z -> 'x) -> ('z -> 'y)))



;(( curry compose ) ( curry compose ) )
;(curry compose): (('x -> 'y) -> (('z -> 'x) -> ('z -> 'y)))
;(curry compose): (('a -> 'b) -> (('c -> 'a) -> ('c -> 'b)))
;a więc skoro (curry compose) jest pierwszym argumentem to podstawiamy:
;'a = ('x -> 'y)
;'b = (('z -> 'x) -> ('z -> 'y))
;i do całości:
;((('c -> ('x -> 'y)) -> ('c -> (('z -> 'x) -> ('z -> 'y))))



;(( curry compose ) ( curry apply ) )
;(curry compose): (('a -> 'b) -> (('c -> 'a) -> ('c -> 'b)))
;curry:(('a 'b -> 'c) -> ('a -> ('b -> 'c)))
;apply:(('x -> 'y) 'x -> 'y)
;a' = ('x -> 'y)
;b' = 'x
;'c = 'y
;(curry apply): (('x -> 'y) -> ('x -> 'y))
;podstawiamy (curry apply) do (curry compose)
;'a = ('x -> 'y)
;'b = ('x -> 'y)
;i podstawiamy do wyniku typu:
;(('c -> ('x -> 'y)) -> ('c -> ('x -> 'y)))



;(( curry apply ) ( curry compose ) )
;(curry apply): (('x -> 'y) -> ('x -> 'y))
;(curry compose): (('a -> 'b) -> (('c -> 'a) -> ('c -> 'b)))
;podstawienie:
;'x =('a -> 'b)
;'y = (('c -> 'a) -> ('c -> 'b))
;i do typu końcowego:
;(('a -> 'b) -> (('c -> 'a) -> ('c -> 'b)))




;( compose curry flip )
;compose: (('x -> 'y) ('z -> 'x) -> ('z -> 'y))
;compose: curry compose -> 
;curry: (('b 'a -> 'c) -> ('b -> ('a -> 'c)))
;flip: (('a 'b -> 'c) -> ('b 'a -> 'c))
;podstawiamy 
;'x = ('b 'a -> 'c)
;'y = ('b -> ('a -> 'c))
;'z = ('a 'b -> 'c)
;podstawiamy do końcowego typu:
;(('a 'b -> 'c) -> ('b -> ('a -> 'c)))


