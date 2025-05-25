#lang racket

(define (negatives n)
  (build-list n (lambda (x) (* -1 (+ x 1)))))

(define (reciprocals n)
  (build-list n (lambda (x) (/ 1 (+ x 1)))))

(define (evens n)
  (build-list n (lambda (x) (* 2 x))))

(define (identityM n)
  (build-list n (lambda (y)
    (build-list n (lambda (x) (if (= x y) 1 0))))))

