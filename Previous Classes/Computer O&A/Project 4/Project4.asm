        .orig x3000

; Main loop
LOOP    LEA R0, PROMPT
        PUTS                ; Output PROMPT

        LEA R2, INPUT       ; Load INPUT pointer to R2

; Input loop
READ    GETC                ; Get char from user
        OUT                 ; Echo char

        ADD R1, R0, #-10    ; Check if char is a newline (x0A)
        BRz ENDINPUT        ; If newline, exit to ENDINPUT

        STR R0, R2, #0      ; Store char in INPUT
        ADD R2, R2, #1      ; Increment INPUT pointer

        BRnzp READ          ; Loop back

ENDINPUT AND R0, R0, #0     ; Clear R0
        STR R0, R2, #0      ; Null-terminate INPUT

; Set INPUT all caps
        AND R1, R1, #0      ; Clear R1
        LEA R1, INPUT       ; Load INPUT pointer into R1

UPLOOP  LDR R0, R1, #0      ; Load current char into R0
        BRz UPEND           ; Exit loop if null terminator

        LEA R2, ACHECK      ; Load ACHECK to R2
        LDR R2, R2, #0      
        ADD R2, R0, R2      ; Skip if char >= 'a'
        BRn NEXTCHAR

        LEA R2, ZCHECK      ; Load ZCHECK to R2
        LDR R2, R2, #0      
        ADD R2, R0, R2      ; Skip if char >= 'z'
        BRp NEXTCHAR

        ADD R0, R0, #-16    ; Set to uppercase
        ADD R0, R0, #-16
        STR R0, R1, #0      ; Store upper char in INPUT

NEXTCHAR ADD R1, R1, #1     ; Increment INPUT pointer
        BR UPLOOP           ; Loop back

; Check if INPUT == quit
UPEND   LEA R3, INPUT       ; Load INPUT as STR1
        LEA R4, QUIT        ; Load QUIT as STR2
        JSR STRCOMP         ; Compare strings

        ADD R2, R2, #0      ; Check if R2 == 1 (same)
        BRnz PASS            ; END if INPUT == quit

        LEA R0, QPROMPT     ; Output quit prompt
        PUTS                
        BR DONE

; Check AABC
PASS    LEA R3, INPUT       ; Load INPUT as STR1
        LEA R4, AABC        ; Load AABC as STR2
        JSR STRCOMP         ; Compare strings

        ADD R2, R2, #0      ; Check if R2 == 1 (same)
        BRp OUTSCM

; Check AAPL
        LEA R3, INPUT       ; Load INPUT as STR1
        LEA R4, AAPL        ; Load AAPL as STR2
        JSR STRCOMP         ; Compare strings

        ADD R2, R2, #0      ; Check if R2 == 1 (same)
        BRp OUTNNM

; Check MSBF
        LEA R3, INPUT       ; Load INPUT as STR1
        LEA R4, MSBF        ; Load MSBF as STR2
        JSR STRCOMP         ; Compare strings

        ADD R2, R2, #0      ; Check if R2 == 1 (same)
        BRp OUTSCM

; Check MSFT
        LEA R3, INPUT       ; Load INPUT as STR1
        LEA R4, MSFT        ; Load MSFT as STR2
        JSR STRCOMP         ; Compare strings

        ADD R2, R2, #0      ; Check if R2 == 1 (same)
        BRp OUTNNM

; Check TESI
        LEA R3, INPUT       ; Load INPUT as STR1
        LEA R4, TESI        ; Load TESI as STR2
        JSR STRCOMP         ; Compare strings

        ADD R2, R2, #0      ; Check if R2 == 1 (same)
        BRp OUTSCM

; Check TESS
        LEA R3, INPUT       ; Load INPUT as STR1
        LEA R4, TESS        ; Load TESS as STR2
        JSR STRCOMP         ; Compare strings

        ADD R2, R2, #0      ; Check if R2 == 1 (same)
        BRp OUTNNM

; Invalid input
        LEA R0, INVAL       ; Output INVAL message
        PUTS
        BR LOOP             ; Restart main LOOP

OUTSCM  LEA R0, SCM
        PUTS
        BR LOOP

OUTNNM  LEA R0, NNM
        PUTS
        BR LOOP


DONE    HALT

; String compare function (Use R3, R4 as STR pointers, R2 result (0: Same, -1: Different))
STRCOMP AND R2, R2, #0      ; Clear R2 to store result
        AND R1, R1, #0      ; Clear R1 to check difference

NEXT    LDR R5, R3, #0      ; Load STR1 char into R5
        BRz LAST            ; Go to LAST if 0
        LDR R6, R4, #0      ; Load STR2 char into R6
        NOT R6, R6          ; Get inverse of R6
        ADD R6, R6, #1      ; Add 1 to R6 to have 2's comp negative

        ADD R1, R5, R6      ; Add STR1 char + -STR2 char into R7

        BRnp DIFF           ; If STR1 char != STR2 char, go to DIFF
        ADD R3, R3, #1      ; Else Increment both STR pointers
        ADD R4, R4, #1

        BR NEXT             ; Loop to NEXT char

LAST    LDR R6, R4, #0      ; Load STR2 last char
        BRnp DIFF           ; If not zero, they are different
        ADD R2, R2, #1
        BR RESULT

DIFF    ADD R2, R2, #-1

RESULT  RET                 ; Return
        

; Data
PROMPT  .STRINGZ "Please enter a stock symbol, (quit to exit): "
QPROMPT .STRINGZ "Thanks. See you soon.\n"
INVAL   .STRINGZ "Input not valid.\n"
NL      .STRINGZ "\n"

ACHECK  .FILL #-97
ZCHECK  .FILL #-122

INPUT   .BLKW #6

QUIT    .STRINGZ "QUIT"

AABC    .STRINGZ "AABC"
AAPL    .STRINGZ "AAPL"
MSBF    .STRINGZ "MSBF"
MSFT    .STRINGZ "MSFT"
TESI    .STRINGZ "TESI"
TESS    .STRINGZ "TESS"

SCM     .STRINGZ "SCM\n"
NNM     .STRINGZ "NNM\n"

        .END