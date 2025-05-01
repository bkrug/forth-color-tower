: FIB ( sequenceLength -- )
  0 1
  CR
  ROT 0 DO
    ( display the second number from top of stack )
    OVER . CR
    ( remove second number from top of stack )
    ( add new item to stack that is the some of the two old items )
    TUCK +
  LOOP
  DROP DROP
;