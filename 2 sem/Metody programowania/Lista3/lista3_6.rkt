#lang racket

(define (empty-set)
  (lambda (x) #f))

(define (singleton a)
  (lambda (x) (equal? a x)))

(define (in a s)
  (s a))

(define (union s t)
  (lambda (x) (or (s x) (t x))))

(define (intersect s t)
  (lambda (x) (and (s x) (t x))))


(define zbior1 (lambda (x) (< x 0)))
(define zbior2 (lambda (x) (> x 0)))
(define suma (intersect zbior1 zbior2))


