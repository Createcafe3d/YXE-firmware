#ifndef __INTERLOCK_H
#define __INTERLOCK_H

void setup_interlock(void);
uint8_t get_interlock_state(void);
void send_printer_status(void);

#endif
