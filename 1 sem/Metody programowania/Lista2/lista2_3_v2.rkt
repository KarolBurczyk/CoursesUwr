#lang racket

(define-struct matrix (a b c d))

(define m (make-matrix 1 2 3 4))
(define n (make-matrix 1 2 3 4))

(define (matrix-mult m n)
  (define x (+ (* (matrix-a m) (matrix-a n)) (* (matrix-b m) (matrix-c n))))
  (define y (+ (* (matrix-a m) (matrix-b n)) (* (matrix-b m) (matrix-d n))))
  (define z (+ (* (matrix-c m) (matrix-a n)) (* (matrix-d m) (matrix-c n))))
  (define w (+ (* (matrix-c m) (matrix-b n)) (* (matrix-d m) (matrix-d n))))
  (define iloczyn (make-matrix x y z w))
  iloczyn)

;(define iloczyn (matrix-mult m n))
;(matrix-a iloczyn)
;(matrix-b iloczyn)
;(matrix-c iloczyn)
;(matrix-d iloczyn)
      
(define (matrix-id)
  (define id (make-matrix 1 0 1 0))
  id)

(define (matrix-expt m res k)
  (cond [( = k 0) (matrix-id)]
        [( = k 1) res]
        [else (matrix-expt m (matrix-mult res m) (- k 1))]))
  
;(define potega (matrix-expt m m 2))
;(matrix-a potega)
;(matrix-b potega)
;(matrix-c potega)
;(matrix-d potega)


(define (fib-matrix k)
  (cond [(= k 0) 0]
        [(= k 1) 1]
        [(= k 2) 1]
        [else
         (define fib-empty (make-matrix 1 1 1 0))
         (matrix-a (matrix-expt fib-empty fib-empty k))]))

(fib-matrix 6)


  
  









  
  





  