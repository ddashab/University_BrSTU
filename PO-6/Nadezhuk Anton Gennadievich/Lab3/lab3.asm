masm
model small

remove_words macro string, character
    xor si, si
    xor di, di
    check: 
    cmp string[si], character
        jne copy
        skip:
            inc si
            cmp string[si], "$"
            je end_check
            cmp string[si], separator
            jne skip
        inc si
        jmp check
        copy: 
            mov bl, string[si]
            mov result[di], bl
            inc si
            inc di
            cmp string[si], "$"
            je end_check
            cmp string[si], separator
            jne copy
        
        inc si
        inc di
        jmp check

    end_check: 
    mov result[di], "$"
    endm
      
print macro string
    mov ah, 9h
    lea dx, string
    int 21h
    endm

.data
str_msg db "String: ", "$"
res_msg db 10, 13, "Result: ", "$"
string db "hello my name is anton how are you", "$"
character equ "a"
separator equ " "
lenght equ 34
result db lenght dup(?)

.stack 256h

.code
main proc near
    mov ax, @data
    mov ds, ax
    xor ax, ax
    print str_msg
    print string
    remove_words string, character
    print res_msg
    print result
    mov ax, 4c00h
    int 21h
main endp
end main