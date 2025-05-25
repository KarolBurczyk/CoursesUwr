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

(define (fold-tree t f acc)
  (cond [(leaf? t) acc]
        [else (f (fold-tree (node-l t) f acc) (node-elem t)
     (fold-tree (node-r t) f acc))]))

(define (tree-sum t)
  (fold-tree t + 0))

(define (tree-flip t)
  (fold-tree t (lambda (x y z)
                 (node z y x))(leaf) ))

(define (tree-height t)
  (fold-tree t (lambda (x y z)
                 (+ (max x z) 1)) 0))

(define (tree-span t)
  (fold-tree t (lambda (x y z)
                 (cons (min y (car x) (car z))
                       (max y (cdr x) (cdr z) ))) (cons +inf.0 -inf.0)))

(define (tree-flatten t)
  (fold-tree t (lambda (x y z)
                 (append x (cons y z))) (list)))

(tree-flip tree) 
(tree-sum tree) 
(tree-height tree) 
(tree-span tree) 
(tree-flatten tree) 



