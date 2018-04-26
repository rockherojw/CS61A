; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (cdr(car s))
  
)

(define (caddr s)
  (cdr(cdr(car s)))
  
)

(define (sign x)
  (cond
    ((> x 0) 1)
      ((= x 0) 0)
      (else (-1))
    )
)

(define (ordered? s)
  'YOUR-CODE-HERE
  (cond
    ((null? lst) true)
    ((null? (cdr lst)) true)
    ((< (car lst) (cadr lst)) (ordered? (cdr lst)))
    (else false)))


(define (nodots s)
  'YOUR-CODE-HERE
  nil
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) false)
    ((> (car s) v) false)
    ((< (car s) v) (contains? (cdr s) v))
    (else true)))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))
      ((contains? s v) s)
      ((< v (car s)) (cons v s))
      (else (cons (car s) (append (cdr s) v)))))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
    ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
    ((< (car s) (car t)) (intersect (cdr s) t))
    ((> (car s) (car t)) (intersect s (cdr t)))))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          (else (union (add s (car t)) (cdr t)))))

; Tail-Calls in Scheme

(define (exp-recursive b n)
  (if (= n 0)
      1
      (* b (exp-recursive b (- n 1)))))

(define (exp b n)
  ;; Computes b^n.
  ;; b is any number, n must be a non-negative integer.
  "YOUR CODE HERE"
)

(define (filter pred lst)
  'YOUR-CODE-HERE
)