#lang racket

(define (pom2 txt)
  (cond [(equal? "._" txt) "A"]
        [(equal? "_..." txt) "B"]
        [(equal? "_._." txt) "C"]
        [(equal? "_.." txt) "D"]
        [(equal? "." txt) "E"]
        [(equal? ".._." txt) "F"]
        [(equal? "__." txt) "G"]
        [(equal? "...." txt) "H"]
        [(equal? ".." txt) "I"]
        [(equal? ".___" txt) "J"]
        [(equal? "_._" txt) "K"]
        [(equal? "._.." txt) "L"]
        [(equal? "__" txt) "M"]
        [(equal? "_." txt) "N"]
        [(equal? "___" txt) "O"]
        [(equal? ".__." txt) "P"]
        [(equal? "._." txt) "R"]
        [(equal? "..." txt) "S"]
        [(equal? "_" txt) "T"]
        [(equal? ".._" txt) "U"]
        [(equal? ".__" txt) "W"]
        [(equal? "_.._" txt) "X"]
        [(equal? "_.__" txt) "Y"]
        [(equal? "__.." txt) "Z"]
        [(equal? ".____" txt) "1"]
        [(equal? "..___" txt) "2"]
        [(equal? "...__" txt) "3"]
        [(equal? "...._" txt) "4"]
        [(equal? "....." txt) "5"]
        [(equal? "_...." txt) "6"]
        [(equal? "__..." txt) "7"]
        [(equal? "___.." txt) "8"]
        [(equal? "____." txt) "9"]
        [(equal? "_____" txt) "0"]
        [else "ERROR"]))

(define (pom lst letter)
  (cond [(null? lst) (pom2 letter)]
        [(equal? (car lst) #\space) (if (equal? (car (cdr lst)) #\space) (string-append (string-append (pom2 letter) " ") (pom (cdr (cdr lst)) "")) (string-append (pom2 letter) (pom (cdr lst) "")))]
        [else (pom (cdr lst) (string-append letter (string (car lst))))])
  )

(define (morse-decode kod)
  (pom (string->list kod) "")
  )

(morse-decode "__ .__.  ..___ _____ ..___ ..___")

