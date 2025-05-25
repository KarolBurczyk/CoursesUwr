#lang racket

(provide (struct-out column-info)
         (struct-out table)
         (struct-out and-f)
         (struct-out or-f)
         (struct-out not-f)
         (struct-out eq-f)
         (struct-out eq2-f)
         (struct-out lt-f)
         table-insert
         table-project
         table-sort
         table-select
         table-rename
         table-cross-join
         table-natural-join)

(define-struct column-info (name type) #:transparent)

(define-struct table (schema rows) #:transparent)

(define cities
  (table
   (list (column-info 'city    'string)
         (column-info 'country 'string)
         (column-info 'area    'number)
         (column-info 'capital 'boolean))
   (list (list "Wrocław" "Poland"  293 #f)
         (list "Warsaw"  "Poland"  517 #t)
         (list "Poznań"  "Poland"  262 #f)
         (list "Berlin"  "Germany" 892 #t)
         (list "Munich"  "Germany" 310 #f)
         (list "Paris"   "France"  105 #t)
         (list "Rennes"  "France"   50 #f))))

(define countries
  (table
   (list (column-info 'country 'string)
         (column-info 'population 'number))
   (list (list "Poland" 38)
         (list "Germany" 83)
         (list "France" 67)
         (list "Spain" 47))))

(define (empty-table columns) (table columns '()))

; Wstawianie

(define (is-type x y)
  (cond  [(equal? x 'string) (string? y)]
         [(equal? x 'number) (number? y)]
         [(equal? x 'boolean) (boolean? y)]
         [(equal? x 'symbol) (symbol? y)])
  )

(define (insert-pom row tab)
  (cond [(null? row) (if (null? tab) #t #f)]
        [(is-type (column-info-type (car tab)) (car row)) (insert-pom (cdr row) (cdr tab))]
        [else #f])
  )
(define (table-insert row tab)
  (if (insert-pom row (table-schema tab)) (table (table-schema tab)(append (table-rows tab) (list row)))("Niepoprawne typy danych")))

;#TEST INSERT
;( table-rows ( table-insert ( list "Rzeszow" "Poland" 129
;#f ) cities ) )

; Projekcja

(define (table-project-pom3 col kols)
  (cond [(null? kols) #f]
        [(equal? (car kols) (column-info-name col)) #t]
        [else (table-project-pom3 col (cdr kols))])
  )

(define (table-project-pom2 row columns kols)
  (cond [(null? columns) '()]
        [(table-project-pom3 (car columns) kols)
         (cons (car row) (table-project-pom2 (cdr row) (cdr columns) kols))]
        [else (table-project-pom2 (cdr row) (cdr columns) kols)])
  )

(define (table-project-pom1 rows columns kols)
  (cond [(null? rows) '()]
        [else (cons (table-project-pom2 (car rows) columns kols)
                    (table-project-pom1 (cdr rows) columns kols))])
  )

(define (table-project cols tab)
  (table-project-pom1 (table-rows tab) (table-schema tab) cols)
  )

;#TEST TABLE_PROJECT
;( table-project '( city country ) cities )

; Zmiana nazwy

(define (table-rename-pom col ncol cols)
  (cond [(null? cols) '()]
        [(equal? (column-info-name (car cols)) col)
         (cons (column-info ncol (column-info-type (car cols)))
               (cdr cols))]
        [else (table-rename-pom col ncol (cdr cols))]))

(define (table-rename col ncol tab)
  (table (table-rename-pom col ncol (table-schema tab)) (table-rows tab))
  )

;#TEST TABLE_RENAME
;( table-rename 'city 'name cities )

; Sortowanie

(define (compare-pom1 elem1 elem2 col)
  (cond  [(equal? (column-info-type col) 'string)
          (cond [(string<? elem1 elem2) "<"]
                [(string>? elem1 elem2) ">"]
                [else "="])]
         [(equal? (column-info-type col) 'number)
          (cond [(< elem1 elem2) "<"]
                [(> elem1 elem2) ">"]
                [else "="])]
         [(equal? (column-info-type col) 'boolean)
          (cond [(equal? elem1 elem2) "="]
                [(and (equal? elem1 #t)(equal? elem2 #f)) ">"]
                [else "<"])]
         [(equal? (column-info-type col) 'symbol)
          (cond [(< (symbol->string elem1) (symbol->string elem2)) "<"]
                [(> (symbol->string elem1) (symbol->string elem2)) ">"]
                [else "="])])
  )

(define (compare-pom elem1 elem2 col schema)
  (cond [(null? schema) "="]
        [(equal? col (column-info-name (car schema))) (compare-pom1 (car elem1)(car elem2)(car schema))]
        [else (compare-pom (cdr elem1) (cdr elem2) col (cdr schema))])
  )

(define (compare elem1 elem2 cols schema)
  (cond [(null? cols) #t]
        [else
         (let ([answer (compare-pom elem1 elem2 (car cols) schema)])
          (cond [(equal? answer "=") (compare elem1 elem2 (cdr cols) schema)]
                [(equal? answer "<") #t]
                [(equal? answer ">") #f])
           )])
  )

(define (table-sort-pom1 cols elem tab schema)
  (cond [(null? tab) elem]
        [(compare elem (car tab) cols schema) (table-sort-pom1 cols elem (cdr tab) schema)]
        [else (table-sort-pom1 cols (car tab) (cdr tab) schema)])
  )

(define (table-sort-pom cols tab schema)
  (cond [(null? tab) '()]
        [else (let ([answer (table-sort-pom1 cols (car tab) (cdr tab) schema)])
                (cons answer
                    (table-sort-pom cols (remove answer tab) schema)))]) 
  )

(define (table-sort cols tab)
  (table (table-schema tab) (table-sort-pom cols (table-rows tab)(table-schema tab)))
  )

;#TEST TABLE_SORT
;( table-rows ( table-sort '( country city ) cities ) )

; Selekcja

(define-struct and-f (l r))
(define-struct or-f (l r))
(define-struct not-f (e))
(define-struct eq-f (name val))
(define-struct eq2-f (name name2))
(define-struct lt-f (name val))

;Dwie funkcje do eq-f
(define (table-select-eqf1 col val elem schema)
  (cond [(null? schema) '()]
        [(equal? (column-info-name (car schema)) col) (if (equal? (car elem) val) #t #f)]
        [else (table-select-eqf1 col val (cdr elem) (cdr schema))])
  )

(define (table-select-eqf col val tab schema)
  (cond [(null? tab) '()]
        [(table-select-eqf1 col val (car tab) schema)
                    (cons (car tab)
                          (table-select-eqf col val (cdr tab) schema))]
        [else (table-select-eqf col val (cdr tab) schema)]) 
  )

;Dwie funkcje do eq-f-2
(define (table-select-eqf2-2 col elem schema)
  (cond [(null? schema) '()]
        [(equal? (column-info-name (car schema)) col) (car elem)]
        [else (table-select-eqf2-2 col (cdr elem) (cdr schema))])
  )

(define (table-select-eqf1-2 col1 col2 elem schema)
  (cond [(null? schema) '()]
        [(equal? (column-info-name (car schema)) col1)
         (if (equal? (car elem) (table-select-eqf2-2 col2 (cdr elem) (cdr schema))) #t #f)]
        [else (table-select-eqf1-2 col1 col2 (cdr elem) (cdr schema))])
  )

(define (table-select-eqf-2 col1 col2 tab schema)
  (cond [(null? tab) '()]
        [(table-select-eqf1-2 col1 col2 (car tab) schema)
                    (cons (car tab)
                          (table-select-eqf-2 col1 col2 (cdr tab) schema))]
        [else (table-select-eqf-2 col1 col2 (cdr tab) schema)]) 
  )

;Funkcje do częci wspólnej dwóch tablic
(define (table-common-part-pom row tab)
  (cond [(null? tab) #f]
        [(equal? (car tab) row) #t]
        [else (table-common-part-pom row (cdr tab))])
  )

(define (table-common-part tab1 tab2)
  (cond [(null? tab1) '()]
        [(table-common-part-pom (car tab1) tab2)
         (cons (car tab1) (table-common-part (cdr tab1) tab2))]
        [else (table-common-part (cdr tab1) tab2)])
  )

;Trzy funkcje do lt-f
(define (table-select-ltf2 elem val)
  (cond [(and (string? elem)(string<? elem val)) #t]
        [(and (number? elem)(< elem val)) #t]
        [(and (symbol? elem)(string<? (symbol->string elem)(symbol->string val))) #t]
        [(and (boolean? elem)(equal? elem #f)(equal? val #t)) #t]
        [else #f])
  )

(define (table-select-ltf1 col val elem schema)
  (cond [(null? schema) '()]
        [(equal? (column-info-name (car schema)) col) (table-select-ltf2 (car elem) val)]
        [else (table-select-ltf1 col val (cdr elem) (cdr schema))])
  )

(define (table-select-ltf col val tab schema)
  (cond [(null? tab) '()]
        [(table-select-ltf1 col val (car tab) schema)
                    (cons (car tab)
                          (table-select-ltf col val (cdr tab) schema))]
        [else (table-select-ltf col val (cdr tab) schema)]) 
  )

(define (table-select form tab)
  (cond [(not-f? form) (table (table-schema tab)
                              (remove* (table-rows (table-select (not-f-e form) tab))(table-rows tab)))]
        [(and-f? form) (table (table-schema tab)
                               (table-common-part (table-rows (table-select (and-f-l form) tab))
                              (table-rows (table-select (and-f-r form) tab))))]
        [(or-f? form) (table (table-schema tab)
                              (remove-duplicates (append (table-rows (table-select (or-f-l form) tab))
                              (table-rows (table-select (or-f-r form) tab)))))]
        [(eq-f? form)(table (table-schema tab)
                            (table-select-eqf (eq-f-name form) (eq-f-val form)
                                              (table-rows tab) (table-schema tab)))]
        [(eq2-f? form)(table (table-schema tab)
                            (table-select-eqf-2 (eq2-f-name form) (eq2-f-name2 form)
                                              (table-rows tab) (table-schema tab)))]
        [(lt-f? form)(table (table-schema tab)
                            (table-select-ltf (lt-f-name form) (lt-f-val form)
                                              (table-rows tab) (table-schema tab)))]
        )
  )

;#TEST TABLE-ROWS
;( table-rows ( table-select ( and-f ( eq-f 'capital #t ) ( not-f ( lt-f 'area 300) ) ) cities ) )


; Złączenie kartezjańskie

(define (table-cross-join-pom2 row tab2)
  (cond [(null? tab2) '()]
        [else (cons (append row (car tab2)) (table-cross-join-pom2 row (cdr tab2)))])
  )

(define (table-cross-join-pom1 tab1 tab2)
  (cond [(null? tab1) '()]
        [else (append (table-cross-join-pom2 (car tab1) tab2) (table-cross-join-pom1 (cdr tab1) tab2))])
  )

(define (table-cross-join tab1 tab2)
  (table (append (table-schema tab1)(table-schema tab2))
         (table-cross-join-pom1 (table-rows tab1) (table-rows tab2)))
  )

;#TEST TABLE-CROSS-JOIN
;( table-cross-join cities
;( table-rename 'country 'country2 countries ) )

; Złączenie

(define (table-natural-join tab1 tab2)
  tab1
  )

