#lang racket


(define xd (list 70 2 3 4 69))

(define (select xs min ys)
  (cond[(null? xs) (cons min ys)]
       [(< (car xs) min) (select (cdr xs) (car xs) (cons min ys))]
       [else (select (cdr xs) min (cons (car xs) ys))]))


(define (select-sort xs)
  (if (null? xs)
      '()
      (let ([x (select xs (car xs) (list))])
        (cons (car x) (select-sort (cdr x))))))

(select-sort xd)