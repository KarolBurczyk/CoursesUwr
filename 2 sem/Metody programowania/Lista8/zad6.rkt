#lang plait

(define-type Exp
  (exp-var [x : Symbol])
  (exp-num [x : Number])
  (exp-oper [operator : Symbol][x : Exp][y : Exp])
  (exp-lambda [args : (Listof Symbol)][body : Exp])
  (exp-app [fun : Exp][args : (Listof Exp)])
  (exp-if [condition : Exp][iftrue : Exp][iffalse : Exp])
  (exp-cond [cases : (Listof (Exp * Exp))])
  (exp-let [defs : (Listof (Symbol * Exp))][body : Exp])
)

(define przyklad1 (exp-if (exp-oper '= (exp-num 3) (exp-num 3)) (exp-num 4) (exp-num 9)))

(define przyklad2 (exp-cond (list (pair (exp-oper '= (exp-var 'x) (exp-num 3)) (exp-var 'z))
                                  (pair (exp-oper '= (exp-var 'y) (exp-num 3)) (exp-var 'x)))))
