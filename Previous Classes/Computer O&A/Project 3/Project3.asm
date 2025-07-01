        .orig x3000

; User input loop
LOOP    LEA R0, PROMPT
        PUTS                ; Output prompt
        GETC                ; Get char from user
        OUT                 ; Echo char

        AND R3, R3, #0      ; Clear R3
        ADD R3, R0, #0      ; Copy input to R3

        LEA R0, NL
        PUTS                ; Output newline

; Convert ASCII Code to Numerical Value
        ADD R3, R3, #-16    ; Subtract 48 from ASCII code to
        ADD R3, R3, #-16    ; get the numerical equivalence
        ADD R3, R3, #-16    ; To ensure R3 is the numerical equivalent of the char

; Check if input is valid (0-6)
        AND R4, R4, #0      ; Clear R4
        ADD R4, R3, #-6     ; Check if R3 is between 0 and 6
        BRp BAD            ; If R3 > 6, go to BAD
        ADD R4, R3, #0
        BRn BAD            ; If R3 < 0, go to BAD

; Calculate offset
        AND R4, R4, #0      ; Clear R4
        AND R5, R5, #0      ; Clear R5
        ADD R5, R5, #10     ; 10 loops counter

MULT    ADD R5, R5, #0      ; ADD R3 to R4 10 times
        BRz PRINT           ; Jump to PRINT if done
        ADD R4, R4, R3
        ADD R5, R5, #-1
        BRnzp MULT


; Print WKDAY of input       
PRINT   LEA R0, WKDAY
        ADD R0, R0, R4      ; Add offset
        PUTS                ; Output the corresponding WKDAY
        LEA R0, NL
        PUTS                ; Output newline
        BRnzp LOOP          ; Loop again

BAD     LEA R0, INVALID
        PUTS                ; Output error

DONE    HALT                ; Done with the program

; Data
PROMPT  .STRINGZ "Please enter a number:"
NL      .STRINGZ "\n"
INVALID .STRINGZ "Enter a number between 0 and 6 inclusively"

WKDAY   .STRINGZ "SUNDAY   "
        .STRINGZ "MONDAY   "
        .STRINGZ "TUESDAY  "
        .STRINGZ "WEDNESDAY"
        .STRINGZ "THURSDAY "
        .STRINGZ "FRIDAY   "
        .STRINGZ "SATURDAY "

        .END
