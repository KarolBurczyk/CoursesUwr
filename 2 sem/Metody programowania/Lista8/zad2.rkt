#lang racket

(define (mreverse-pom tab1 tab2)
  (if (null? tab1)
        tab2
        (let ([x (mcdr tab1)])
          (set-mcdr! tab1 tab2)
          (mreverse-pom x tab1)))
  )

(define (mreverse! tab)
  (mreverse-pom tab '()))

(define przyklad (mcons 9 (mcons 8 (mcons 7 '()))))

(mreverse! przyklad)