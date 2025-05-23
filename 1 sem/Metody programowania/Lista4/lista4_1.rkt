#lang racket

(define-struct leaf () #:transparent)
(define-struct node (l elem r) #:transparent)

( define t
   ( node
     ( node ( leaf ) 2 ( leaf ) )
     5
     ( node ( node ( leaf ) 6 ( leaf ) )
            8
            ( node ( leaf ) 9 ( leaf ) ) ) ) )

;Drzewo:
;            5
;      2          8
;    L   L    6      9
;            L  'L   L  L

;Po wstawieniu 7:
;            5
;      2          8
;    L   L    6       9
;           L   '7   L  L
;              'L 'L
;Drzewa roznia sie zacytowanymi elementami 