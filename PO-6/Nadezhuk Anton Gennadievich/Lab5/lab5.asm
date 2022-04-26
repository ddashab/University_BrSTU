masm 
model use16 small
.486

.data
x dd 4.5
y dd 2.5
z dd ?

tmp1 dd ?
tmp2 dd ?

fifteen dd 15.0
minus_five dd -5.0
two dd 2.0
one dd 1.0
four dd 4.0

result_msg db "Result: $"

.stack 100h

.code
main proc near
    mov ax, @data
    mov ds, ax
    xor ax, ax
    finit
    fld x
    fsub y
    fcomp minus_five
    fstsw ax
    sahf
    jc met1
    fcomp fifteen
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
    fld x; st(0) = x
    fmul x; st(0) = x*x
    fld y; st(0) = y, st(1) = x*x
    fmul y; st(0) = y*y
    fstp tmp1; tmp1 = st(0) = y*y, st(0) = x*x
    fadd tmp1; st(0) = x*x + y*y
    fsub one; st(0) = x*x + y*y - 1
    fstp tmp2; tmp2 = st(0) = x*x + y*y - 1
    fld tmp1; st(0) = y*y
    fsub x; st(0) = y*y - x
    fdiv tmp2; st(0) = (y*y - x)/(x*x + y*y - 1)
    fstp z; z = st(0)
    ret
p1 endp

p2 proc near
    fld y; st(0) = y
    fmul y; st(0) = y*y
    fld x; st(0) = x, st(1) = y*y
    fmul x; st(0) = x*x
    fstp tmp1; tmp1 = st(0) = x*x, st(0) = y*y
    fadd tmp1; st(0) = y*y + x*x
    fadd one; st(0) = y*y + x*x + 1
    fstp tmp2; tmp2 = st(0) = y*y + x*x + 1
    fld tmp1; st(0) = x*x
    fadd y; st(0) = x*x + y
    fadd y; st(0) = x*x + 2y
    fdiv tmp2; st(0) = (x*x + 2y)/(y*y + x*x + 1)
    fstp z; z = st(0)
    ret
p2 endp

p3 proc near
    fld x; st(0) = x
    fmul x; st(0) = x*x
    fld y; st(0) = y, st(1) = x*x
    fmul y; st(0) = y*y
    fmul two; st(0) = 2*y*y
    fstp tmp1; tmp1 = st(0) = 2*y*y, st(0) = x*x
    fadd tmp1; st(0) = x*x + 2*y*y
    fadd four; st(0) = x*x + 2*y*y
    fstp z; z = st(0)
    ret
p3 endp
end main