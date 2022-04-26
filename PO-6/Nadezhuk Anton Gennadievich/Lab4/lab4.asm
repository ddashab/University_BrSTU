masm 
model use16 small
.486

.data
x dw 4
y dw 2
z dw ?

tmp1 dw ?
tmp2 dw ?

fifteen dw 15
minus_five dw -5
two dw 2
one dw 1
four dw 4

result_msg db "Result: $"

.stack 100h

.code
main proc near
    mov ax, @data
    mov ds, ax
    xor ax, ax
    finit
    fild x
    fisub y
    ficomp minus_five
    fstsw ax
    sahf
    jc met1
    ficomp fifteen
    fstsw ax
    sahf
    jnc met2
    call p3
    jmp exit
    met1: 
        call p1
        jmp exit
    met2:
        call p2
    exit:
        mov ax, 4c00h 
        int 21h
main endp

p1 proc near
    fild x; st(0) = x
    fimul x; st(0) = x*x
    fild y; st(0) = y, st(1) = x*x
    fimul y; st(0) = y*y
    fistp tmp1; tmp1 = st(0) = y*y, st(0) = x*x
    fiadd tmp1; st(0) = x*x + y*y
    fisub one; st(0) = x*x + y*y - 1
    fistp tmp2; tmp2 = st(0) = x*x + y*y - 1
    fild tmp1; st(0) = y*y
    fisub x; st(0) = y*y - x
    fidiv tmp2; st(0) = (y*y - x)/(x*x + y*y - 1)
    fistp z; z = st(0)
    call print
    ret
p1 endp

p2 proc near
    fild y; st(0) = y
    fimul y; st(0) = y*y
    fild x; st(0) = x, st(1) = y*y
    fimul x; st(0) = x*x
    fistp tmp1; tmp1 = st(0) = x*x, st(0) = y*y
    fiadd tmp1; st(0) = y*y + x*x
    fiadd one; st(0) = y*y + x*x + 1
    fistp tmp2; tmp2 = st(0) = y*y + x*x + 1
    fild tmp1; st(0) = x*x
    fiadd y; st(0) = x*x + y
    fiadd y; st(0) = x*x + 2y
    fidiv tmp2; st(0) = (x*x + 2y)/(y*y + x*x + 1)
    fistp z; z = st(0)
    call print
    ret
p2 endp

p3 proc near
    fild x; st(0) = x
    fimul x; st(0) = x*x
    fild y; st(0) = y, st(1) = x*x
    fimul y; st(0) = y*y
    fimul two; st(0) = 2*y*y
    fistp tmp1; tmp1 = st(0) = 2*y*y, st(0) = x*x
    fiadd tmp1; st(0) = x*x + 2*y*y
    fiadd four; st(0) = x*x + 2*y*y
    fistp z; z = st(0)
    call print
    ret
p3 endp

print proc
    mov ah, 9h
    lea dx, result_msg
    int 21h
    
    mov ax, z
    xor cx, cx
    mov bx, 10
    lp1:
        xor dx, dx
        div bx
        add dl, '0'
        push dx
        inc cx
        or ax, ax
        jnz lp1
    lp2:
        pop ax
        int 29h
        loop lp2
    mov ah, 4ch
    int 21h
print endp
end main