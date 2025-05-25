#lang plait

(define-type tree
  (leaf)
  (node [l : tree]
        [elem : 'a]
        [r : tree])
  (node2 [l : tree]
         [elem1 : 'a]
         [mid : tree]
         [elem2 : 'a]
         [r : tree]))

(define (rek x mini maxi)
  (cond [(leaf? x) #t]
        [(node? x) (and (> maxi (node-elem x))
                        (< mini (node-elem x))
                        (rek (node-l x) mini (min (node-elem x) maxi))
                        (rek (node-r x) (max (node-elem x) mini) maxi))]
        [(node2? x) (and (> maxi (node2-elem1 x))
                         (< mini (node2-elem1 x))
                         (> maxi (node2-elem2 x))
                         (< mini (node2-elem2 x))
                         (< (node2-elem1 x) (node2-elem2 x))
                         (rek (node2-l x) mini (min (node2-elem1 x) (min (node2-elem2 x) maxi)))
                         (rek (node2-r x) (max (node2-elem1 x) (max (node2-elem2 x) mini)) maxi)
                         (rek (node2-mid x)
                                   (min (node2-elem1 x) (min (node2-elem2 x) mini))
                                   (max (node2-elem1 x) (max (node2-elem2 x) maxi))))]))

(define (rek2 x lvl)
  (cond [(leaf? x) (pair #t 0)]
        [(node? x) (if (and (fst (rek2 (node-l x) lvl)) (fst (rek2 (node-r x) lvl))
                            (= (snd (rek2 (node-l x) lvl)) (snd (rek2 (node-r x) lvl))))
                       (pair #t (+ (snd (rek2 (node-r x) lvl)) 1)) (pair #f 0))]
        [(node2? x) (if (and (fst (rek2 (node2-l x) lvl))
                             (fst (rek2 (node2-mid x) lvl))
                             (fst (rek2 (node2-r x) lvl))
                            (= (snd (rek2 (node2-l x) lvl)) (snd (rek2 (node2-r x) lvl)))
                            (= (snd (rek2 (node2-r x) lvl)) (snd (rek2 (node2-mid x) lvl))))
                       (pair #t (+ (snd (rek2 (node2-r x) lvl)) 1)) (pair #f 0))]))

(define (2-3tree? x)
  (and (rek x -inf.0 +inf.0) (fst (rek2 x 0))))

(define drzewo (node2
                (node
                     (leaf)
                     6
                     (node
                          (leaf)
                          3
                          (leaf)))
                2
                (leaf)
                3
                (node
                     (leaf)
                     2
                     (leaf))))
(define drzewko (node
                (leaf)
                1
                (leaf)))


