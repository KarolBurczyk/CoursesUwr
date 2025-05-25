#lang racket

(define xd (list 1 2 3 4 69))

(define (maximum xs max)
  (cond[(null? xs) max]
       [(> (car xs) max) (maximum (cdr xs) (car xs))]
       [else (maximum (cdr xs) max)]))

(maximum xd -inf.0)