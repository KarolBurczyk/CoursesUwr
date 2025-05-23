#lang racket
;
;(define (my-foldr f xs ys)
;  (if (or (null? xs) (null? ys))
;      x
;      (f (car xs) (my-foldr f x (cdr xs)))))

;(foldr (lambda (v l) (cons (add1 v) l)) '() '(1 2 3 4))

(define (my-foldr2 f ys xs acc)
  (if (or (null? xs) (null? ys))
      acc
      (f (car xs) (car ys) (my-foldr2 f (rest ys) (cdr xs) acc))))

;(define (my-foldr f x xs)
;  (if (null? xs)
;      x
;      (f (car xs) (my-foldr f x (cdr xs)))))

;(my-foldr-orig + '(5 6 7 8) '(1 2 3 4) 0)

;(my-foldr (lambda (x acc) (cons (cons (car x) (car acc)) (cons (cdr x) (cdr acc)))) (cons empty empty) '(('a . 1)('b . 2)))

#;(reverse (car (foldl (lambda (x acc) (if (cdr acc)
                           (cons (cons x (car acc)) (not (cdr acc)))
                           (cons (car acc) (not (cdr acc)))))
       (cons empty  #f) (list 1 2 3 4 5 6 7 8))))



; =======================================================
; Lista 15

(define (my-foldr f x xs)
  (if (null? xs)
      x
      (f (car xs) (my-foldr f x (cdr xs)))))

(define (my-foldl f x xs)
  (define (it xs acc)
    (if (null? xs)
        acc
        (it (cdr xs) (f (car xs) acc))))
  (it xs x))

(define (my-append xs ys)
  (if (null? xs)
      ys
      (cons (car xs) (my-append (cdr xs) ys))))

(define-struct leaf () #:transparent)
(define-struct node (l val r) #:transparent)

(define (tree? x)
  (cond [(leaf? x) #t]
        [(node? x) (and (tree? (node-l x))
                        (tree? (node-r x)))]
        [else #f]))

(define tree (node
              (node
               (leaf)
               9
               (leaf))
              1
              (node
               (leaf)
               2
               (leaf))))

;(tree? tree)

;======================================

;indukcja dowodziki

;1. (length (append xs ys)) = (+ (length xs) (length ys))

;Podstawa. dla xs = empty
;L = (length (append empty ys)) = (length ys)
;P = (+ (length empty) (length ys)) = (+ 0 (length ys)) = (length ys) = L

;Krok Ind. przy zał., że (length (append xs ys)) = (+ (length xs) (length ys)) jest prawdą, chcemy pokazać, że
;zachodzi (length (append (cons x xs) ys)) = (+ (length (cons x xs)) (length ys))
;zatem
;L = (length (append (cons x xs) ys))= (length (cons x (append xs ys))) = (+ 1 (length (append xs ys)))
;P = (+ (length (cons x xs)) (length ys)) = (+ (+ 1 (length xs)) (length ys)) = z przemienności dodawania =
;(+ 1 (+ (length xs) (length ys)))
;zatem skoro zachodzi (length (append xs ys)) = (+ (length xs) (length ys)), to powiększenie obydwu stron
;o 1 również zachodzi

;2. (filter p (map f xs)) = (map f (filter (lambda (x) (p (f x))) xs))

;Podstawa. dla xs = empty
;L = (filter p (map f xs)) = (filter p (map f empty)) = (filter p empty) = empty
;P = (map f (filter (lambda (x) (p (f x))) xs)) = (map f (filter (lambda (x) (p (f x))) empty)) =
;(map f empty) = empty = L

;Krok. przy zał, że (filter p (map f xs)) = (map f (filter (lambda (x) (p (f x))) xs)) jest prawdziwe, chcemy
;pokazać, że (filter p (map f (cons x xs))) = (map f (filter (lambda (x) (p (f x))) (cons x xs))) również
;zachodzi, zatem
;L = (filter p (map f (cons x xs))) = (filter p (cons (f x) (map f xs))) =
;(cons (if (p (f x)) (f x) null) (filter p (map f xs))
;P = (map f (filter (lambda (x) (p (f x))) (cons x xs))) =
;(map f (cons (if (p (f x)) x null) (filter (lambda (x) (p (f x))) xs))) =
;(cons (if (p (f x)) (f x) null) (map f (filter (lambda (x) (p (f x)) xs))))
;a zakładaliśmy, że cdr naszych consów jest równy, więc skoro car jest równy to zachodzi L = P,
;co należało udowodnić

;3. (foldr + 0 ns) = (foldr + 0 ns), gdzie ns jest listą liczb całkowitych

;Podstawa. da ns = empty
;L = (foldr + 0 empty) = 0
;P = (foldl + 0 empty) = 0 = L

;Krok. zakładamy, że zachodzi (foldr + 0 ns) = (foldl + 0 ns) i chcemy udowodnić
;(foldr + 0 (cons n ns)) = (foldr + 0 (cons n ns))
;L = (foldr + 0 (cons n ns)) = (+ n (foldr + 0 ns)) 
;P = (foldl + 0 (cons n ns)) = (foldl + (+ 0 n) ns) = (+ n (foldl + 0 ns)) = (+ n (foldr  + 0 ns)) = L
;co należało dowieść


;=======================================

;kontrakty parametryczne

;1: (parametric->/c [a b] (-> (-> a b) a b))
(define (apply f n)
  (parametric->/c [a b] (-> (-> a b) a b))
   (f n))
;(apply number->string 9)

;2: (parametric->/c [a b c] (-> (-> a b c) (-> (cons/c a b) c)))
(define (fun2 f)
  (parametric->/c [a b c] (-> (-> a b c) (-> (cons/c a b) c)))
  (lambda (x) (f (car x) (cdr x))))
;((fun2 +) (cons 9 2))

;3: (parametric->/c [a b] (-> (listof (-> a b)) (listof a) (listof b))
(define (fun3 fun ns)
  (parametric->/c [a b] (-> (listof (-> a b)) (listof a) (listof b)))
  (cond [(or (empty? ns) (empty? fun)) null]
        [else (cons ((car fun) (car ns)) (fun3 (cdr fun) (cdr ns)))]))

;(fun3 (list (lambda (x) (* x x)) (lambda (x) (+ x x ))) (list 5 3))

;4: (parametric->/c [a b] (-> (-> b (or/c false/c (cons/c a b))) b (listof a)))
(define (fun4 f b)
  (parametric->/c [a b] (-> (-> b (or/c false/c (cons/c a b))) b (listof a)))
  (if (not (f b))
      empty
      (list (car (f b)))))

;5: (parametric->/c [a] (-> (-> a boolean?) (listof a) (cons/c (listof a) (listof a))))
(define (fun5 f lst)
  (parametric->/c [a] (-> (-> a boolean?) (listof a) (cons/c (listof a) (listof a))))
  (cons (filter (lambda (x) (f x)) lst)
        (filter (lambda (x) (not (f x))) lst)))

;6: (parametric->/c [a b] (-> (-> a b) (listof a) (-> b (listof a))))
(define (fun6 f lst)
  (parametric->/c [a b] (-> (-> a b) (listof a) (-> b (listof a))))
  (define (pom lstB lstA b)
    (cond [(empty? lstB) empty]
          [(= (car lstB) b) lstA]
          [else (pom (cdr lstB) (cdr lstA) b)]))
  (lambda (x) (pom (map f lst) lst x)))

;((fun6 (lambda (x) (* x x)) (list 1 2 3 4 5 6 7 8 9)) 49)

;===============================================

;(foldr (lambda (x y acc) (cons (+ x y) acc)) '() (list 1 2 3) (list 2 3 4))









