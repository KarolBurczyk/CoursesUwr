#lang plait

(define-type Op
  (op-add) (op-mul) (op-sub) (op-div) (op-pow))

(define-type Op-un
  (op-fuc) (op-min))

(define-type Exp
  (exp-number [n : Number])
  (exp-op [op : Op] [e1 : Exp] [e2 : Exp])
  (exp-op-un [op : Op-un] [e : Exp]))

(define (parse-Op s)
  (let ([sym (s-exp->symbol s)])
  (cond
    [(equal? sym '+) (op-add)]
    [(equal? sym '-) (op-sub)]
    [(equal? sym '*) (op-mul)]
    [(equal? sym '/) (op-div)]
    [(equal? sym '^) (op-pow)])))

(define (parse-Op-un s)
  (let ([sym (s-exp->symbol s)])
  (cond [(equal? sym '!) (op-fuc)]
        [(equal? sym '-) (op-min)])))

(define (length x suma)
  (if (empty? x)
      suma
      (length (rest x) (+ suma 1)))
  )

(define (parse-Exp s)
  (cond
    [(s-exp-number? s) (exp-number (s-exp->number s))]
    [(s-exp-list? s)
     (if (= (length (s-exp->list s) 0) 3)
         (let ([xs (s-exp->list s)])
           (exp-op (parse-Op  (first  xs))
                   (parse-Exp (second xs))
                   (parse-Exp (third  xs))))
         (let ([xs (s-exp->list s)])
           (exp-op-un (parse-Op-un  (first  xs))
                      (parse-Exp (second xs)))))]))

; ==============================================

(define (potega a b res)
  (if (= b 0)
      res
      (potega a (- b 1) (* res a))))

(define (silnia x res)
  (if (>= x 1)
      (silnia (- x 1) (* res x))
      res)
  )

(define (eval-op op)
  (type-case Op op
    [(op-add) +]
    [(op-sub) -]
    [(op-mul) *]
    [(op-div) /]
    [(op-pow) (lambda  (x y) (potega x y 1))]))

(define (eval-op-un op)
  (type-case Op-un op
    [(op-fuc) (lambda (x) (silnia x 1))]
    [(op-min) (lambda (x) (* -1 x))]))

(define (eval e)
  (type-case Exp e
    [(exp-number n)    n]
    [(exp-op op e1 e2)
     ((eval-op op) (eval e1) (eval e2))]
    [(exp-op-un op e)
     ((eval-op-un op) (eval e))]))