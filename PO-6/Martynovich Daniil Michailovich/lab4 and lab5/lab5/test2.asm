masm
model use16 small
.486
.stack 100h
.data 
x dd 4.5
y dd 2.5
a dd ?
b dd ? 
c dd ?
z dd ?
three dd 3
four  dd 4
two dd 2
seven dd 7
five dd -5
.code 
main proc
mov ax,@data 
mov ds,ax 
finit
fld x ;add x to st(0)
fadd y ;st(0)=x+y
fcomp seven ;compare st(0) c 7
fstsw ax 
sahf ;swr->ax-> 
jnc met1 ;if x+y>7 start met1
fcomp five
fstsw ax 
sahf ;swr->ax->
jc met2 ;if x+y<-5 start met2
fcomp five
fstsw ax 
sahf ;swr->ax->
jc met3 
jmp exit
met1: call p1 ;call p1 if x+7>7
jmp exit
met2: call p2 ;call p2 if a+b=5
jmp exit
met3: call p3 ;call p3 
exit:
mov ah,39h 
lea dx,z
int 21h 
mov ax,4c00h
int 21h
main endp
p1 proc ;p1 proc x+y>7
fld x ;st(0)=x
fmul three ;st(0)=x*3
fst a ;a=x*3
fld y ;st(0)=y
fmul four ; st(0)=y*4
fadd three ;st(0)=y*4+3
fadd a ; st(0)=y*4+3+ad
fst z
ret 
p1 endp
p2 proc ;p2 proc a+b>5
fld y; st(0)=y
fmul y
fadd four ;st(0)=y^2+4
fst c ;c=y^2+4

fld x ;st(0)=x
fmul two
fmul x ;st(0)=2x^2
fst a

fld y ;st(0)=y
fmul three ;st(0)=3*y
fsub a ; st(0)=3y-2x^2
fdiv c ;st(0)=3y-2x^2/y^2+4
fst z
ret 
p2 endp
p3 proc ;p3 proc a+b=5
fld y ;st(0)=y
fmul y
fmul four
fst a ;a=4y^2

fld x
fmul x
fmul three
fsub a
fsub three
fst z
ret 
p3 endp
end main