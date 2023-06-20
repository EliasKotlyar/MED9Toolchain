#include "autogenerated.h"

uint32_t GET_LDRXN_ADR(void) __attribute__((section(".code"))) ;
uint32_t GET_LDRXN_ADR (void)
{
    uint8_t cruise_enabled = READ_RAM_BYTE(VAR_BFGREN);
    if(cruise_enabled == 1){
        return TABLE_LDRXN1;
    }else{
        return TABLE_LDRXN2;
    }
}