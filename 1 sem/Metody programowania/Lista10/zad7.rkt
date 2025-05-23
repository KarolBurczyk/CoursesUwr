#lang plait

(define-syntax my-and
  (syntax-rules ()
    [(my-and) #f]
    [(my-and [a : Boolean]) a]
    [(my-and a b ...) (if a (my-and b ...) a)] ))

(define-syntax my-or
  (syntax-rules ()
    [(my-or) #f]
    [(my-or [a : Boolean]) a]
    [(my-or a b ...) (if a a (my-or b ...))]))

(define-syntax my-let
  (syntax-rules ()
    [(my-let () a) a]
    [(my-let ([x1 a1] [x2 a2] ...) body)
     ((lambda (x1 x2 ...) body) a1 a2 ...)]))

(define-syntax my-let*
  (syntax-rules ()
    [(my-let* () a) a]
    [(my-let* ([x1 a1] [x2 a2] ...) body)
     ((lambda (x1) (my-let* ([x2 a2] ...) body)) a1)]))

(my-and #t #t #t #f)
(my-or #f #f #f #t)
(define a 7)
(my-let ([a 10] [b (+ a 10)]) (+ a b))
(my-let* ([a 10] [b (+ a 10)]) (+ a b))





 
     