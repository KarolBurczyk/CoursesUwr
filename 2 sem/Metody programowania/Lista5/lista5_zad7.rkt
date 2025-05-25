#lang plait
( define-type Prop
( var [ v : String ])
( conj [ l : Prop ] [ r : Prop ])
( disj [ l : Prop ] [ r : Prop ])
( neg [ f : Prop ]) )

(define rachunek
  (conj (neg (var "x")) (var "x")))

(define (rek zdanie)
  (cond [(neg? zdanie) (rek (neg-f zdanie))]
        [(conj? zdanie) (append (rek(conj-l zdanie))
                                (rek(conj-r zdanie)))]
        [(disj? zdanie) (append (rek(disj-l zdanie))
                                (rek(disj-r zdanie)))]
        [else (list (var-v zdanie))]))
(define (remove-duplicates x)
    (cond [(empty? x) '()]
          [(member (first x) (rest x))
           (remove-duplicates (rest x))]
          [else (cons (first x)
                 (remove-duplicates (rest x)))]))
(define (free-vars zdanie)
  (remove-duplicates (rek zdanie)))

(free-vars rachunek)
  
  
  

