#lang plait

(define-type-alias Value Number)

(define (run [s : S-Exp]) : Value
  (numV-n (eval (parse s) mt-env)))

;; abstract syntax -------------------------------

(define-type Op
  (add) (sub) (mul) (leq))

(define-type Exp
  (numE [n : Value])
  (varE [x : Symbol])
  (opE [l : Exp] [op : Op] [r : Exp])
  (ifE [b : Exp] [l : Exp] [r : Exp])
  (letE [x : Symbol] [e1 : Exp] [e2 : Exp])
  (appE [name : Symbol] [e : (Listof Exp)]))

(define-type Prog
  (progE [d : (Listof Def)] [e : Exp]))

(define-type Def
  (defE [name : Symbol] [args : (Listof Symbol)] [e : Exp]))

;; parse ----------------------------------------

(define (parse-Exp [s : S-Exp])
  (cond
    [(s-exp-match? `NUMBER s)
     (numE (s-exp->number s))]
    [(s-exp-match? `{ANY SYMBOL ANY} s)
     (opE (parse-Exp (first (s-exp->list s)))
          (parse-op (s-exp->symbol (second (s-exp->list s))))
          (parse-Exp (third (s-exp->list s))))]
    [(s-exp-match? `{ifz ANY then ANY else ANY} s)
     (ifE (parse-Exp (second (s-exp->list s)))
          (parse-Exp (fourth (s-exp->list s)))
          (parse-Exp (fourth (rest (rest (s-exp->list s))))))]
    [(s-exp-match? `{let SYMBOL ANY ANY} s)
     (letE (s-exp->symbol (second (s-exp->list s)))
           (parse-Exp (third (s-exp->list s)))
           (parse-Exp (fourth (s-exp->list s))))]
    [(s-exp-match? `SYMBOL s)
     (varE (s-exp->symbol s))]
    [(s-exp-match? `{SYMBOL {ANY ...}} s)
     (appE (s-exp->symbol (first (s-exp->list s)))
           (map parse-Exp (s-exp->list (second (s-exp->list s)))))]
    [else (error 'parse "invalid input")]))

(define (parse-Def [s : S-Exp])
  (cond
    [(s-exp-match? `{fun SYMBOL ANY = ANY} s)
     (defE (s-exp->symbol (second (s-exp->list s)))
       (map s-exp->symbol (s-exp->list (third (s-exp->list s))))
       (parse-Exp (fourth (rest (s-exp->list s)))))]
    [else (error 'parse "invalid input")]))

(define (parse [s : S-Exp])
  (cond
    [(s-exp-match? `{define ANY for ANY} s)
     (progE (map parse-Def (s-exp->list (second (s-exp->list s))))
            (parse-Exp (fourth (s-exp->list s))))]
    [else (error 'parse "invalid input")]))

(define (parse-op [op : Symbol]) : Op
  (cond
    [(eq? op '+) (add)]
    [(eq? op '-) (sub)]
    [(eq? op '*) (mul)]
    [(eq? op '<=) (leq)]
    [else (error 'parse "unknown operator")]))

;; eval --------------------------------------


;; environments

(define-type Storable
  (valS [v : Val])
  (undefS))

(define-type Binding
  (bind [name : Symbol]
        [ref : (Boxof Storable)]))

(define-type-alias Env (Listof Binding))

(define mt-env empty)

(define (extend-env-undef [env : Env] [x : Symbol]) : Env
  (cons (bind x (box (undefS))) env))

(define (extend-env [env : Env] [x : Symbol] [v : Val]) : Env
  (cons (bind x (box (valS v))) env))

(define (find-var [env : Env] [x : Symbol]) : (Boxof Storable)
  (type-case (Listof Binding) env
    [empty (error 'lookup "unbound variable")]
    [(cons b rst-env) (cond
                        [(eq? x (bind-name b))
                         (bind-ref b)]
                        [else
                         (find-var rst-env x)])]))
  
(define (lookup-env [x : Symbol] [env : Env]) : Val
  (type-case Storable (unbox (find-var env x))
    [(valS v) v]
    [(undefS) (error 'lookup-env "undefined variable")]))
   
(define (update-env! [env : Env] [x : Symbol] [v : Val]) : Void
  (set-box! (find-var env x) (valS v)))


;; primitive operations

(define (op-num-num->proc [f : (Value Value -> Value)]) : (Val Val -> Val)
  (λ (v1 v2)
    (type-case Val v1
      [(numV n1)
       (type-case Val v2
         [(numV n2)
          (numV (f n1 n2))]
         [else
          (error 'eval "type error")])]
      [else
       (error 'eval "type error")])))

(define (op-num-bool->proc [f : (Value Value -> Boolean)]) : (Val Val -> Val)
  (λ (v1 v2)
    (type-case Val v1
      [(numV n1)
       (type-case Val v2
         [(numV n2)
          (if (f n1 n2) (numV 0) (numV 1))]
         [else
          (error 'eval "type error")])]
      [else
       (error 'eval "type error")])))

(define (op->proc [op : Op]) : (Val Val -> Val)
  (type-case Op op
    [(add) (op-num-num->proc +)]
    [(sub) (op-num-num->proc -)]
    [(mul) (op-num-num->proc *)]
    [(leq) (op-num-bool->proc <=)]))

;; evaluation function (eval/apply)

(define-type Val
  (numV [n : Value])
  (funV [name : (Listof Symbol)] [f : Exp] [env : Env]))

(define (eval [p : Prog] [env : Env])
  (type-case Prog p
    [(progE d e)
     (eval-Exp e (eval-Def d (eval-unDef d env)))]))

(define (eval-unDef d env)
  (cond [(empty? d) env]
        [else (type-case Def (first d)
           [(defE name args e) (eval-unDef (rest d) (extend-env-undef (eval-args args env) name))])]))

(define (eval-args args env)
  (cond [(empty? args) env]
        [else (eval-args (rest args) (extend-env-undef env (first args)))]))

(define (eval-Def d env)
  (cond [(empty? d) env]
        [else (type-case Def (first d)
           [(defE name args e) (begin
                                 (update-env! env name (funV args e env))
                                 (eval-Def (rest d) env))])]))

(define (eval-Exp [e : Exp] [env : Env]) : Val
  (type-case Exp e
    [(numE n) (numV n)]
    [(opE l o r) ((op->proc o) (eval-Exp l env) (eval-Exp r env))]
    [(ifE b l r)
     (let ([v (eval-Exp b env)])
       (type-case Val v 
         [(numV x) (cond [(= x 0) (eval-Exp l env)]
                         [else (eval-Exp r env)])]
         [else (error 'eval-Exp "type error")]))]
    [(varE x)
     (lookup-env x env)]
    [(letE x e1 e2)
     (let ([v1 (eval-Exp e1 env)])
       (eval-Exp e2 (extend-env env x v1)))]
    [(appE name e)
     (apply (lookup-env name env) e env)]))

(define (apply [v1 : Val] [e : (Listof Exp)] [env : Env]) : Val
  (type-case Val v1
    [(funV s f env2)
     (eval-Exp f (apply-Def s e env))]
    [else (error 'apply "not a function")]))

(define (apply-Def s e env)
  (cond [(empty? s) env]
        [else (begin
                (update-env! env (first s) (eval-Exp (first e) env))
                (apply-Def (rest s) (rest e) env))]))




