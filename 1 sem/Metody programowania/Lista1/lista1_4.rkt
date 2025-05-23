#lang racket
(require rackunit)
(define (procedura x y z)
    (if (> x y)
        (if (> y z)
            (+ (* x x) (* y y))
            (+ (* x x) (* z z)))
        (if (> x z)
            (+ (* y y) (* x x))
            (+ (* y y) (* z z)))))

(check-equal? (procedura 1 2 3) 12)
(check-equal? (procedura 1 4 3) 25)
