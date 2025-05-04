: DISPLAYTOWERS
  CR ." TOWER 1     TOWER 2     TOWER 3"
  0 4 DO
    CR
    TOWER1 I + C@ .
    TOWER2 I + C@ .
    TOWER3 I + C@ .
    -1
  +LOOP
;