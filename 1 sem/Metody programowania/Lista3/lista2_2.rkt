#lang racket
(require rackunit)

(define (my-foldl f x xs)
  (define (it xs acc)
    (if (null? xs)
        acc
        (it (cdr xs) (f (car xs) acc))))
  (it xs x))

(define (product xs)
  (my-foldl * 1 xs))

(check-equal? (product '()) 1)
(check-equal? (product (list 1 2 3 4 5)) 120)
(check-equal? (product (list 1 1 1 1 1)) 1)
(check-equal? (product (list 2 2 2 2 2)) 32)
