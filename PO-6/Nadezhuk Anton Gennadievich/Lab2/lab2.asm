masm
model small

.data
first_msg db "Please enter your text: ", "$"
second_msg db 10, 13, "Result: ", "$"
max_len equ 100
text db max_len dup(?)
temp_text db max_len dup(?)
lenght dw 0
distance db ?

.stack 256h

.code
main proc near
    mov ax, @data
    mov ds, ax
    xor ax, ax
    call input
    call check
    mov ax, 4c00h
    int 21h
main endp

input proc near
    mov ah, 9h
    lea dx, first_msg
    int 21h
    
    lea si, text
    mov cx, max_len
    start_input:
        mov ah, 01h
        int 21h
        cmp al, 2eh
        jz end_text
        mov [si], al
        inc lenght
        inc si
        loop start_input
    end_text:
        inc si
        mov [si], "$"
        
    mov ah, 9h
    lea dx, second_msg
    int 21h
    ret
input endp

check proc near
    lea si, text
    mov cx, lenght
    start_check:
        cmp [si], 48
        jb next_check
        cmp [si], 57
        ja next_check
        cmp [si+1], 97
        jb call_p2
        cmp [si+1], 122
        ja call_p2
        next_check: 
            inc si
            loop start_check
        call p1
        jmp end_check
        call_p2: call p2
    end_check: ret
check endp

p1 proc near
    lea si, text
    mov cx, lenght
    start_p1:
        mov al, [si] 
        cmp al, 65
        jb next_p1
        cmp al, 90
        ja next_p1
        mov distance, al
        sub distance, 65
        mov bl, distance
        mov al, 90
        sub al, bl
        mov [si], al
        next_p1:
            inc si
            loop start_p1
    
    mov ah, 9h
    lea dx, text
    int 21h
    ret
p1 endp

p2 proc near
    lea si, text
    lea di, temp_text
    mov cx, lenght
    start_p2:
        mov al, [si]
        mov [di], al
        next_p2: 
            inc si
            dec cx
            cmp [si], al
            jz next_p2
        inc di
        cmp cx, 0
        jnz start_p2
    inc di
    mov [di], "$"
    
    mov ah, 9h
    lea dx, temp_text
    int 21h
    ret
p2 endp

end main 
 