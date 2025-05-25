#lang plait

( define-type ( NNF 'v )
   ( nnf-lit [ polarity : Boolean ] [ var : 'v ])
   ( nnf-conj [ l : ( NNF 'v ) ] [ r : ( NNF 'v ) ])
   ( nnf-disj [ l : ( NNF 'v ) ] [ r : ( NNF 'v ) ]) )

(define (neg-nnf x)
  (cond [(nnf-lit? x) (if (nnf-lit-polarity x) (nnf-lit #f (nnf-lit-var x)) (nnf-lit #t (nnf-lit-var x)))]
        [(nnf-conj? x) (nnf-disj (neg-nnf (nnf-conj-l x))(neg-nnf (nnf-conj-r x)))]
        [(nnf-disj? x) (nnf-conj (neg-nnf (nnf-disj-l x))(neg-nnf (nnf-disj-r x)))]))

(define rachunek (nnf-conj (nnf-lit #t "x") (nnf-lit #f "y")))
rachunek
(neg-nnf rachunek)
