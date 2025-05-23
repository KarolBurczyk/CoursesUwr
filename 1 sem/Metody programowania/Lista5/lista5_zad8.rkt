#lang plait

( define-type Prop
( var [ v : String ])
( conj [ l : Prop ] [ r : Prop ])
( disj [ l : Prop ] [ r : Prop ])
( neg [ f : Prop ]) )

(define rachunek
  (conj (neg (var "x")) (var "y")))

(define wartosciowanie (make-hash (list (pair "x" #t)
                              (pair "y" #t))))

(define (rek zdanie wartosciowanie)
  (cond [(neg? zdanie) (not(rek (neg-f zdanie) wartosciowanie))]
        [(conj? zdanie) (and (rek (conj-l zdanie) wartosciowanie)
                                (rek (conj-r zdanie) wartosciowanie))]
        [(disj? zdanie) (or (rek (disj-l zdanie) wartosciowanie)
                                (rek (disj-r zdanie) wartosciowanie))]
        [else (some-v (hash-ref wartosciowanie (var-v zdanie)))]))

(rek rachunek wartosciowanie)


  
  
  

