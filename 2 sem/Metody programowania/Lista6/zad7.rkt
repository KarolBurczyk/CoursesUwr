#lang plait

( define-type ( Formula 'v )
   ( var [ var : 'v ])
   ( neg [ f : ( Formula 'v ) ])
   ( conj [ l : ( Formula 'v ) ] [ r : ( Formula 'v ) ])
   ( disj [ l : ( Formula 'v ) ] [ r : ( Formula 'v ) ]) )

(define (eval-formula sig x)
  (cond [(var?  x)(sig (var-var x))]
        [(neg?  x)(not (eval-formula sig (neg-f φ)))]
        [(conj? x)(and
                   (eval-formula sig (conj-l x))
                   (eval-formula sig (conj-r x)))]
        [(disj? x)(or
                   (eval-formula sig (disj-l x))
                   (eval-formula sig (disj-r x)))]))

