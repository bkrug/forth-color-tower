/
/ This word is most useful for testing in FORTH interactive terminal
/
: DISPLAYTOWERS ( -- )
  0 4 DO
    CR
    ."    " TOWER1 I + C@ EMIT
    ."            " TOWER2 I + C@ EMIT
    ."            " TOWER3 I + C@ EMIT
    -1
  +LOOP
  CR ." TOWER 1     TOWER 2     TOWER 3"
;