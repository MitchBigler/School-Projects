        .orig x3000

; Main loop
LOOP    LEA R0, PROMPT
        PUTS                ; Output PROMPT

        LEA R2, INPUT       ; Load INPUT ptr to R2

; Input loop
READ    GETC                ; Get char from user
        OUT                 ; Echo char

        ADD R1, R0, #-10    ; Check if char is a newline (x0A)
        BRz ENDINPUT        ; If newline, exit to ENDINPUT

        STR R0, R2, #0      ; Store char in INPUT
        ADD R2, R2, #1      ; Increment INPUT ptr

        BRnzp READ          ; Loop back

ENDINPUT AND R0, R0, #0     ; Clear R0
        STR R0, R2, #0      ; Null-terminate INPUT

; Set INPUT all caps
        AND R1, R1, #0      ; Clear R1
        LEA R1, INPUT       ; Load INPUT pointer into R1

UPLOOP  LDR R0, R1, #0      ; Load current char into R0
        BRz CHECK_INSTRUCTION ; Exit loop if null terminator

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

NEXTCHAR ADD R1, R1, #1     ; Increment INPUT ptr
        BR UPLOOP           ; Loop back

; Data for input and uppper
PROMPT  .STRINGZ "Enter LC-3 instruction ('QUIT' to exit): "
INPUT   .BLKW #8
ACHECK  .FILL #-97
ZCHECK  .FILL #-122

; Check first char
CHECK_INSTRUCTION
        LEA R6, LOOP     ; Store LOOP location in R6 for returning

        LEA R1, INPUT         ; Load ptr to INPUT
        LDR R0, R1, #0        ; Load first character
        BRz INVALID

        ADD R0, R0, #-16      ; -64 to start from 'A'
        ADD R0, R0, #-16       
        ADD R0, R0, #-16       
        ADD R0, R0, #-16

        ADD R0, R0, #-1        ; Check for 'A'
        BRz STATE_A
        ADD R0, R0, #-1        ; Check for 'B'
        BRz STATE_B
        ADD R0, R0, #-8        ; Check for 'J'
        BRz STATE_J
        ADD R0, R0, #-2        ; Check for 'L'
        BRz STATE_L
        ADD R0, R0, #-2        ; Check for 'N'
        BRz STATE_N
        ADD R0, R0, #-4        ; Check for 'R'
        BRz STATE_R
        ADD R0, R0, #-1        ; Check for 'S'
        BRz STATE_S
        ADD R0, R0, #-1        ; Check for 'T'
        BRz STATE_T
        ADD R0, R0, #3         ; Check for 'Q'
        BRz STATE_Q

        BR INVALID            ; invalid input

; State Machine for Each Letter
STATE_A LDR R0, R1, #1        ; Load next char
        LEA R2, NEG_68
        LDR R2, R2, #0

        ADD R3, R0, R2        ; Compare 'D'
        BRz STATE_AD          ; If 'D', move to AD

        ADD R3, R3, #-10      ; Compare 'N'
        BRz STATE_AN          ; If 'N', go to AN

        BR INVALID            ; Else, go to INVALID

STATE_AD
        LDR R0, R1, #2        ; Load next char
        LEA R2, NEG_68
        LDR R2, R2, #0
        ADD R3, R0, R2        ; Compare 'D'
        BRnp INVALID

        ; If 'ADD', check for newline
        JSR CHECK_NL3         ; Check newline      
        LEA R0, OPADD         ; Valid ADD opcode
        PUTS
        JMP R6

STATE_AN
        LDR R0, R1, #2        ; Load next char
        LEA R2, NEG_68
        LDR R2, R2, #0
        ADD R3, R0, R2        ; Compare 'D'
        BRnp INVALID

        ; If 'AND', check for newline
        JSR CHECK_NL3         ; Check newline    
        LEA R0, OPAND         ; Valid AND opcode
        PUTS
        JMP R6

STATE_B
        LDR R0, R1, #1        ; Load next char
        LEA R2, NEG_82
        LDR R2, R2, #0
        ADD R3, R0, R2        ; Compare 'R'
        BRnp INVALID

        ; If 'BR', check for newline
        JSR CHECK_NL2         ; Check newline         
        LEA R0, OPBR          ; Valid BR opcode
        PUTS
        JMP R6

STATE_J LDR R0, R1, #1        ; Load next char
        LEA R2, NEG_77
        LDR R2, R2, #0

        ADD R3, R0, R2        ; Compare 'M'
        BRz STATE_JM          ; If 'M', move to JM

        ADD R3, R3, #-6      ; Compare 'S'
        BRz STATE_JS          ; If 'S', go to JS
        BR INVALID            ; Else, go to INVALID

STATE_JM
        LDR R0, R1, #2        ; Load next char
        LEA R2, NEG_80
        LDR R2, R2, #0
        ADD R3, R0, R2        ; Compare 'P'
        BRnp INVALID

        ; If 'JMP', check for newline
        JSR CHECK_NL3         ; Check newline   
        LEA R0, OPJMP         ; Valid JMP opcode
        PUTS
        JMP R6

STATE_JS
        LDR R0, R1, #2        ; Load next char
        LEA R2, NEG_82
        LDR R2, R2, #0
        ADD R3, R0, R2        ; Compare 'R'
        BRnp INVALID

        ; If 'JSR', check for R or newline
        LDR R0, R1, #3        ; Load next char
        ADD R3, R0, #0        ; Compare nl
        BRz VALID_JSR

        ADD R3, R0, R2        ; Compare 'R'
        BRnp INVALID
        JSR CHECK_NL4

VALID_JSR 
        LEA R0, OPJSR         ; Valid JSR opcode
        PUTS
        JMP R6

STATE_L LDR R0, R1, #1        ; Load next char
        LEA R2, NEG_68
        LDR R2, R2, #0

        ADD R3, R0, R2        ; Compare 'D'
        BRz STATE_LD          ; If 'D', move to LD

        ADD R3, R3, #-1       ; Compare 'E'
        BRz STATE_LE          ; If 'E', go to LE
        BR INVALID            ; Else, go to INVALID

STATE_LD
        LDR R0, R1, #2        ; Load next char
        LEA R2, NEG_73
        LDR R2, R2, #0
        ADD R3, R0, R2        ; Compare 'I'
        BRz STATE_LDI
        ADD R3, R3, #-9
        BRz STATE_LDR
        JSR CHECK_NL2
        LEA R0, OPLD          ; Valid LDI opcode
        PUTS
        JMP R6

STATE_LDI
        JSR CHECK_NL3
        LEA R0, OPLDI         ; Valid LDI opcode
        PUTS
        JMP R6

STATE_LDR
        JSR CHECK_NL3
        LEA R0, OPLDR         ; Valid LDR opcode
        PUTS
        JMP R6

STATE_LE
        LDR R0, R1, #2        ; Load next char
        LEA R2, NEG_65
        LDR R2, R2, #0
        ADD R3, R0, R2        ; Compare 'A'
        BRnp INVALID

        ; If 'LEA', check for newline
        JSR CHECK_NL3         ; Check newline    
        LEA R0, OPLEA         ; Valid LEA opcode
        PUTS
        JMP R6

STATE_N LDR R0, R1, #1        ; Load next char
        LEA R2, NEG_79
        LDR R2, R2, #0
        ADD R3, R0, R2        ; Compare 'O'
        BRnp INVALID          ; Else, go to INVALID

        LDR R0, R1, #2        ; Load next char
        ADD R2, R2, #-5
        ADD R3, R0, R2        ; Compare 'T'
        BRnp INVALID          ; Else, go to INVALID

        ; If 'NOT', check for newline
        JSR CHECK_NL3         ; Check newline    
        LEA R0, OPNOT         ; Valid NOT opcode
        PUTS
        JMP R6

STATE_R LDR R0, R1, #1        ; Load next char
        LEA R2, NEG_69
        LDR R2, R2, #0

        ADD R3, R0, R2        ; Compare 'E'
        BRz STATE_RE          ; If 'E', move to RE

        ADD R3, R3, #-15      ; Compare 'R'
        BRz STATE_RT          ; If 'R', go to RT

        BR INVALID            ; Else, go to INVALID

STATE_RE
        LDR R0, R1, #2        ; Load next char
        LEA R2, NEG_84
        LDR R2, R2, #0
        ADD R3, R0, R2        ; Compare 'T'
        BRnp INVALID

        ; If 'RET', check for newline
        JSR CHECK_NL3         ; Check newline      
        LEA R0, OPRET         ; Valid RET opcode
        PUTS
        JMP R6

STATE_RT
        LDR R0, R1, #2        ; Load next char
        LEA R2, NEG_73
        LDR R2, R2, #0
        ADD R3, R0, R2        ; Compare 'I'
        BRnp INVALID

        ; If 'RTI', check for newline
        JSR CHECK_NL3         ; Check newline    
        LEA R0, OPRTI         ; Valid RTI opcode
        PUTS
        JMP R6

STATE_S LDR R0, R1, #1        ; Load next char
        LEA R2, NEG_84
        LDR R2, R2, #0

        ADD R3, R0, R2        ; Compare 'T'
        BRnp INVALID          ; If not 'T', invalid

        LDR R0, R1, #2        ; Load next char
        ADD R2, R2, #2
        ADD R3, R0, R2        ; Compare 'R'
        BRz STATE_STR

        ADD R3, R3, #9        ; Compare 'I'
        BRz STATE_STI

        JSR CHECK_NL2
        LEA R0, OPST         ; Valid ST opcode
        PUTS
        JMP R6

STATE_STR
        JSR CHECK_NL3
        LEA R0, OPSTR         ; Valid STR opcode
        PUTS
        JMP R6

STATE_STI
        JSR CHECK_NL3
        LEA R0, OPSTI         ; Valid STI opcode
        PUTS
        JMP R6

STATE_T LDR R0, R1, #1        ; Load next char
        LEA R2, NEG_82
        LDR R2, R2, #0
        ADD R3, R0, R2        ; Compare 'R'
        BRnp INVALID          ; Else, go to INVALID

        LDR R0, R1, #2        ; Load next char
        ADD R2, R2, #15
        ADD R2, R2, #2
        ADD R3, R0, R2        ; Compare 'A'
        BRnp INVALID          ; Else, go to INVALID

        LDR R0, R1, #3        ; Load next char
        ADD R2, R2, #-15
        ADD R3, R0, R2        ; Compare 'P'
        BRnp INVALID          ; Else, go to INVALID

        ; If 'TRAP', check for newline
        JSR CHECK_NL4         ; Check newline    
        LEA R0, OPTRAP        ; Valid NOT opcode
        PUTS
        JMP R6

STATE_Q LDR R0, R1, #1        ; Load next char
        LEA R2, NEG_85
        LDR R2, R2, #0
        ADD R3, R0, R2        ; Compare 'U'
        BRnp INVALID          ; Else, go to INVALID

        LDR R0, R1, #2        ; Load next char
        ADD R2, R2, #12
        ADD R3, R0, R2        ; Compare 'I'
        BRnp INVALID          ; Else, go to INVALID

        LDR R0, R1, #3        ; Load next char
        ADD R2, R2, #-11
        ADD R3, R0, R2        ; Compare 'T'
        BRnp INVALID          ; Else, go to INVALID

        ; If 'QUIT', check for newline
        JSR CHECK_NL4         ; Check newline    
        LEA R0, QUIT          ; QUIT entered
        PUTS

        HALT


; Constant nums < -16
NEG_65  .FILL #-65
NEG_68  .FILL #-68
NEG_69  .FILL #-69
NEG_73  .FILL #-73
NEG_77  .FILL #-77
NEG_79  .FILL #-79
NEG_80  .FILL #-80
NEG_82  .FILL #-82
NEG_84  .FILL #-84
NEG_85  .FILL #-85

INVALID    LEA R0, INVAL
           PUTS
           JMP R6

; Data
QUIT  .STRINGZ "Goodbye.\n"
INVAL .STRINGZ "Invalid instruction.\n"

; Opcodes
OPADD   .STRINGZ "0001\n"
OPAND   .STRINGZ "0101\n"
OPBR    .STRINGZ "0000\n"
OPJMP   .STRINGZ "1100\n"
OPJSR   .STRINGZ "0100\n"
OPLD    .STRINGZ "0010\n"
OPLDI   .STRINGZ "1010\n"
OPLDR   .STRINGZ "0110\n"
OPLEA   .STRINGZ "1110\n"
OPNOT   .STRINGZ "1001\n"
OPRET   .STRINGZ "1100\n"
OPRTI   .STRINGZ "1000\n"
OPST    .STRINGZ "0011\n"
OPSTI   .STRINGZ "1011\n"
OPSTR   .STRINGZ "0111\n"
OPTRAP  .STRINGZ "1111\n"

CHECK_NL4
        LDR R0, R1, #4        ; Load next char
        ADD R0, R0, #0        ; Compare with newline
        BRnp INVALID
        RET

CHECK_NL3
        LDR R0, R1, #3        ; Load next char
        ADD R0, R0, #0        ; Compare with newline
        BRnp INVALID
        RET

CHECK_NL2
        LDR R0, R1, #2        ; Load next char
        ADD R0, R0, #0        ; Compare with newline
        BRnp INVALID
        RET

        .END