masm
model use16 small
.486
.stack 100h
.data
x dw 7
y dw 3
a dw ?
b dw ? 
c dw ?
z dw ?
three dw 3
four  dw 4
two dw 2
seven dw 7
five dw -5
.code 
main proc
mov ax,@data 
mov ds,ax 
finit
fild x ;add x to st(0)
fiadd y ;st(0)=x+y
ficomp seven ;compare st(0) c 7
fstsw ax 
sahf ;swr->ax-> 
jnc met1 ;if x+y>7 start met1
ficomp five
fstsw ax 
sahf ;swr->ax->
jc met2 ;if x+y<-5 start met2
call p3 
jmp exit
met1: call p1 ;call p1 if x+7>7
jmp exit
met2: call p2 ;call p2 if x+y<-5
exit:
call OutInt 
main endp
p1 proc ;p1 proc x+y>7
fild x ;st(0)=x
fimul three ;st(0)=x*3
fist a ;a=x*3
fild y ;st(0)=y
fimul four ; st(0)=y*4
fiadd three ;st(0)=y*4+3
fiadd a ; st(0)=y*4+3+ad
fist z
ret 
p1 endp
p2 proc ;p2 proc a+b>5
fild y; st(0)=y
fimul y
fiadd four ;st(0)=y^2+4
fist c ;c=y^2+4

fild x ;st(0)=x
fimul two
fimul x ;st(0)=2x^2
fist a

fild y ;st(0)=y
fimul three ;st(0)=3*y
fisub a ; st(0)=3y-2x^2
fidiv c ;st(0)=3y-2x^2/y^2+4
fist z
ret 
p2 endp
p3 proc ;p3 proc a+b=5
fild y ;st(0)=y
fimul y
fimul four
fist a ;a=4y^2

fild x
fimul x
fimul three
fisub a
fisub three
fist z
ret 
p3 endp
OutInt proc
 mov   ax,z
   xor   cx,cx
   mov   bx,10

lp1:
   xor   dx,dx
   div   bx
   add   dl,'0'
   push  dx
   inc   cx
   or    ax,ax
   jnz   lp1

lp2:
   pop   ax
   int   29h
   loop  lp2

   mov   ah,4ch
   int   21h
OutInt endp
end main