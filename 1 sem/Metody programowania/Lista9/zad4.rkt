#lang racket

(define (pom2 txt)
  (cond [(equal? "A" txt) "._"]
        [(equal? "B" txt) "_..."]
        [(equal? "C" txt) "_._."]
        [(equal? "D" txt) "_.."]
        [(equal? "E" txt) "."]
        [(equal? "F" txt) ".._."]
        [(equal? "G" txt) "__."]
        [(equal? "H" txt) "...."]
        [(equal? "I" txt) ".."]
        [(equal? "J" txt) ".___"]
        [(equal? "K" txt) "_._"]
        [(equal? "L" txt) "._.."]
        [(equal? "M" txt) "__"]
        [(equal? "N" txt) "_."]
        [(equal? "O" txt) "___"]
        [(equal? "P" txt) ".__."]
        [(equal? "R" txt) "._."]
        [(equal? "S" txt) "..."]
        [(equal? "T" txt) "_"]
        [(equal? "U" txt) ".._"]
        [(equal? "W" txt) ".__"]
        [(equal? "X" txt) "_.._"]
        [(equal? "Y" txt) "_.__"]
        [(equal? "Z" txt) "__.."]
        [(equal? "1" txt) ".____"]
        [(equal? "2" txt) "..___"]
        [(equal? "3" txt) "...__"]
        [(equal? "4" txt) "...._"]
        [(equal? "5" txt) "....."]
        [(equal? "6" txt) "_...."]
        [(equal? "7" txt) "__..."]
        [(equal? "8" txt) "___.."]
        [(equal? "9" txt) "____."]
        [(equal? "0" txt) "_____"]
        [else ""]))

(define (pom lst)
  (cond [(null? (cdr lst)) (pom2 (string (car lst)))]
        [else (string-append (string-append (pom2 (string (car lst)))) " "  (pom (cdr lst)))])
  )

(define (morse-code kod)
  (pom (string->list kod))
  )

(morse-code "METODY PROGRAMOWANIA")

