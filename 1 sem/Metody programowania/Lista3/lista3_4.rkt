#lang racket

(define (inc x)
  (+ x 1))

(define (square x)
  (* x x))

(define (my-compose fun1 fun2)
  (define (function x)
    (fun1 (fun2 x)))
  function)

((my-compose square inc) 5)
((my-compose inc square) 5)