#lang racket

(define xd (list 1 2 3 4))

(define (elem x xs)
  (cond[(null? xs) #f]
       [(equal? x (car xs)) #t]
       [else (elem x (cdr xs))]))

(elem 0 xd)
  