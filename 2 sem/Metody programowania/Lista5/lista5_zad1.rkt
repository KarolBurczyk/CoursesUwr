#lang plait

(define (proc1 a b) a)

(define (proc2 f g a) (f a (g a)))

(define (proc3 f) (f (lambda (x) (f (lambda (x) x)))))

(define (proc4 f g)
   (lambda (x) (pair (f x)(g x))))

(define (proc5 o a)
  (if (none? (o a))
      '()
      (cons (snd (some-v (o a))) (proc5 o (fst (some-v (o a)))))))


 