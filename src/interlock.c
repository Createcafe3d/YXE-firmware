#include "stm32f0xx_conf.h"
#include "stm32f0xx_tim.h"
#include "stm32f0xx_gpio.h"
#include "stm32f0xx_exti.h"

#include "interlock.h"
#include "hwaccess.h"
#include "led_override.h"

#include "serialio.h"
#include "messages.pb.h"
#include "pb_encode.h"


extern bool g_laser_gating;

void setup_interlock(void){

  //Initialize GPIO's PF0 && PF1 (INPUTS)
  GPIO_InitTypeDef gp;
  RCC_AHBPeriphClockCmd(RCC_AHBPeriph_GPIOF, ENABLE);

  gp.GPIO_Pin = GPIO_Pin_0 | GPIO_Pin_1;
  gp.GPIO_Mode = GPIO_Mode_IN;
  gp.GPIO_Speed = GPIO_Speed_2MHz;
  gp.GPIO_OType = GPIO_OType_PP;
  gp.GPIO_PuPd = GPIO_PuPd_DOWN;
  GPIO_Init(GPIOF, &gp);
}

uint8_t get_interlock_state(void){
    uint8_t switch_a=0;
    uint8_t switch_b=1;
	uint8_t switches;
	
    switch_a = GPIO_ReadInputDataBit(GPIOF, GPIO_Pin_0);
    switch_b = GPIO_ReadInputDataBit(GPIOF, GPIO_Pin_1);
	switches = (switch_a << 1) + switch_b;
	switch(switches){
	case 0b00:
		 play_blink_four();
		 break; 
	case 0b01:
		 play_blink_right();
		 break; 
	case 0b10: 
		 play_blink_left();
		 break; 
	case 0b11:
		break;
	}


    return (switch_a & switch_b);

}

void send_printer_status() {
  uint8_t out[16];
  uint8_t type;
  pb_ostream_t stream = pb_ostream_from_buffer(out, sizeof(out));
  bool status;
  PrinterStatus record;

  type = PRINTER_STATUS;
  pb_write(&stream, &type, 1);

  record.cardInserted = 1;
  record.keyInserted = get_interlock_state();
  record.overrideSwitch = get_interlock_state();
  record.laserOn = g_laser_gating;
  record.laserPowerFeedback = 42;
  status = pb_encode(&stream, PrinterStatus_fields, &record);
  if (status) {
    serialio_write(out, stream.bytes_written);
  }
}
