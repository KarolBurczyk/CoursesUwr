#lang racket

(define-struct matrix (a b c d))


(define (matrix-mult m n)
  (define x (+ (* (matrix-a m) (matrix-a n)) (* (matrix-b m) (matrix-c n))))
  (define y (+ (* (matrix-a m) (matrix-b n)) (* (matrix-b m) (matrix-d n))))
  (define z (+ (* (matrix-c m) (matrix-a n)) (* (matrix-d m) (matrix-c n))))
  (define w (+ (* (matrix-c m) (matrix-b n)) (* (matrix-d m) (matrix-d n))))
  (define iloczyn (make-matrix x y z w))
  iloczyn)


(define (matrix-expt m res k)
  (if (= k 0)
      res 
      (if (= (remainder k 2) 1)
          (matrix-expt (matrix-mult m m) (matrix-mult res m) (quotient k 2))
          (matrix-expt (matrix-mult m m) res (quotient k 2)))))


(define (fib-fast k)
  (cond [(= k 0) 0]
        [(= k 1) 1]
        [(= k 2) 1]
        [else
         (define fib-empty (make-matrix 1 1 1 0))
         (matrix-a (matrix-expt fib-empty fib-empty (- k 1)))]))

(fib-fast 5)




  
  









  
  





  