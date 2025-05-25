#lang racket

(define xd (list 1 2 3 4 699))

(define (suffixes xs lista)
  (cond [(null? xs) (list xs)]
        [else (append lista (list xs) (suffixes (cdr xs) lista))]))

(suffixes xd (list))