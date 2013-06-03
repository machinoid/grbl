#ifndef _RASPBERRYPI_H
#define _RASPBERRYPI_H

#include <bcm2835.h>
#include <stdint.h>
#define PSTR(s) s
#define sei()
#define cli()
#define ISR(m) void ##m(void)
#endif

