.data
var1: .word 30
var2: .word 40
.text
main:
      lw $t0,var1($zero)
      lw $t1,var2($zero)
      slt $t2,$t0,$t1