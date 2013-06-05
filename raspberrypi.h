#ifndef _RASPBERRYPI_H
#define _RASPBERRYPI_H

#include <bcm2835.h>
#include <stdint.h>
#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <sys/mman.h>

#define PSTR(s) s
#define sei()
#define cli()
#define ISR(m) void ##m(void)
#define pgm_read_byte_near(s) *s

/* Xenomai */
#include <native/task.h>
#include <native/timer.h>

#include  <rtdk.h>
#endif


