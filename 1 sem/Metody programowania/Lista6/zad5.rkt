#lang plait

( define-type ( NNF 'v )
   ( nnf-lit [ polarity : Boolean ] [ var : 'v ])
   ( nnf-conj [ l : ( NNF 'v ) ] [ r : ( NNF 'v ) ])
   ( nnf-disj [ l : ( NNF 'v ) ] [ r : ( NNF 'v ) ]) )

(define (eval-nnf sig x)
  (cond [(nnf-lit? x) (if (some-v ( hash-ref sig (nnf-lit-var x)))
                          (if (nnf-lit-polarity x) #t #f)
                          (if (nnf-lit-polarity x) #f #t))]
        [(nnf-conj? x) (and (eval-nnf sig (nnf-conj-l x)) (eval-nnf sig (nnf-conj-r x)))]
        [else (or (eval-nnf sig (nnf-disj-l x)) (eval-nnf sig (nnf-disj-r x)))]))

(define rachunek (nnf-conj (nnf-lit #t "x") (nnf-lit #f "y")))
(define wartosciowanie (make-hash (list (pair "x" #t) (pair "y" #t))))

(eval-nnf wartosciowanie rachunek)