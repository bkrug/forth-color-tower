\ VDP memory manager words     Sept 15 2019
 
\ VARIABLE VP  \ moved to kernel
 
HEX 1000 VP !  \ "VDP pointer" start of free VDP RAM
 
: VHERE   ( -- addr) VP @ ;   \ FETCH the value in VDP pointer
: VALLOT  ( n -- )   VP +! ;  \ add n to the value in VDP pointer
: VC,     ( n -- )   VHERE VC!  1 VALLOT ;
: V,      ( n -- )   VHERE V!   2 VALLOT ;
: VCOUNT  ( vdp$adr -- vdpadr len ) DUP 1+ SWAP VC@ ;
: VCREATE ( <text> -- ) VHERE CONSTANT ;
 
 
