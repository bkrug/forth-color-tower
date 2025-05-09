INCLUDE DSK2.MALLOC

: FIB ( sequenceLength -- )
  CR
  ( place initial fibianoci numbers on the stack )
  0 1
  ( move the sequence length to the top of the stack, and loop )
  ROT 0 DO
    ( display the second number in stack )
    OVER . CR
    (
      remove second number in stack
      top of the stack remains
      add new item to stack that is the sum of the two old items
    )
    TUCK +
  LOOP
  DROP DROP
;