#lang racket


(define xd (list 1 3 3 4 69))

(define (sorted xs)
  (cond[(null? (cdr xs)) #t]
       [(<= (car xs) (car (cdr xs))) (sorted (cdr xs))]
       [else #f]))

(sorted xd)