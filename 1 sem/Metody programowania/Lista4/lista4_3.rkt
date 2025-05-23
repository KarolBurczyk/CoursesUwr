#lang racket

(define-struct leaf () #:transparent)
(define-struct node (l elem r) #:transparent)

( define tree
   ( node
     ( node ( leaf ) 2 ( leaf ) )
     5
     ( node ( node ( leaf ) 6 ( leaf ) )
            8
            ( node ( leaf ) 9 ( leaf ) ) ) ) )


(define (bst? t)
  (define (rek t mini maxi)
    (if (< (node-elem t) maxi)
        (define maxi (node-elem t)))
    (if (> (node-elem t) mini)
        (define mini (node-elem t)))
    (cond [(leaf? t) #t]
          [((node-elem (node-r t)) < (mini)) #f]
          [((node-elem (node-l t)) > (maxi) #f)]
          [(and (rek t-l) (rek t-r)) #t]
          [else #f]))
 
  