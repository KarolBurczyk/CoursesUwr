#lang racket

(define (my-foldr f x xs)
  (if (null? xs)
      x
      (f (car xs) (my-foldr f x (cdr xs)))))

( define ( foldr-reverse xs )
( foldr ( lambda ( y ys ) ( append ys ( list y ) ) ) null xs ) )

(foldr-reverse ( build-list 10000 identity ) )

;(1 2 3 4) null
;(2 3 4) append (1)
;(3 4) append (2 append (1))
;(4) append (3 append (2 append (1)))
;(4 append (3 append (2 append (1))))
;(4 3 append (2 append (1)))
;(4 3 2 append (1))
;(4 3 2 1)
;zatem skoro przy 4 elementach tworzy 4 consy, to
;przy n elementahc bedzie ich n