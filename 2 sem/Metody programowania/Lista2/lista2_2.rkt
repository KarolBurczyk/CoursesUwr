#lang racket
(require rackunit)
;(define (fib n)
;  (define (rek i prev new)
;   (if (<= (- i 2) 0)
;       (+ prev new)
;       (rek (- i 1) new (+ prev new))))
;  (cond [(or (= n 1) (= n 2)) 1]
;        [else (rek n 0 1)]))
(define (fib n)
  (cond [(= n 0) 0]
        [(= n 1) 1]
        [else (+ (fib (- n 1)) (fib (- n 2)))]))

(define (fib-iter n)
  (define (iter i prev new)
    (if (<= (- i 2) 0)
        (+ prev new)
        (iter (- i 1) new (+ prev new))))
  (if (= n 0)
      0
      (iter n 0 1)))




;(check-equal? (fib 3) 2)
(check-equal? (fib-iter 0) 0)
(check-equal? (fib-iter 3) 2)
(check-equal? (fib-iter 1) 1)
