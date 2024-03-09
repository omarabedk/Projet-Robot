/**
  ******************************************************************************
  * @file    main.c
  * @author  Ac6
  * @version V1.0
  * @date    01-December-2013
  * @brief   Default main function.
  ******************************************************************************
*/


#include "stm32f4xx.h"
#include "stm32f4xx_nucleo.h"

#include "drv_uart.h"
#include "dynamixel.h"

#define DYN_ID 1

extern TIM_HandleTypeDef    TimHandle_period;

extern uint8_t rec_buf2[NB_CAR_TO_RECEIVE+1];	 // defined in drv_uart.c
extern uint8_t rec_buf1[NB_CAR_TO_RECEIVE+1];

int main(void)
{

	//int val = 5;
	int j;
	int x=30;

	HAL_Init();	// passage par stm32f4xx_hal_msp.c : configuration des broches
	SystemClock_Config();

    uart1_Init();			// ZIGBEE
    uart2_Init();           // CABLE
    uart6_Init();           // DYNAMIXEL
    //tickTimer_Init(3000);	// 3000 ms
	//i2c1_Init();			// Modifier stm32f4xx_hal_msp.c pour configurer les broches
	//spi1Init();			// Modifier stm32f4xx_hal_msp.c pour configurer les broches
	   HAL_Delay(500);

	    //------------------------------------------------------------
	    //  TEST LIAISON SERIE
	    // ouvrir gtkterm ou minicom / /dev/ttyCAM0 baudrate : 115200-8-N-1


		dxl_LED(1, LED_ON);
		HAL_Delay(2000);
		dxl_LED(1, LED_OFF);

		HAL_Delay(1000);
		dxl_LED(2, LED_ON);
		HAL_Delay(2000);
		dxl_LED(2, LED_OFF);
		//dxl_LED(DYN_ID2, LED_OFF);

		/*  uint32_t position = dxl_getPresentPosition(DYN_ID);
		 uint32_t baudrate = dxl_getBaudRate(DYN_ID);
		 uint8_t firmware_version = dxl_getFirmwareVersion(DYN_ID);
		 uint8_t model_number = dxl_getModelNumber(DYN_ID);
		 */

		//moteur 1
		dxl_setOperatingMode(1, 3);
		dxl_setOperatingMode(2, 3);
		dxl_setGoalPosition(1, 1000);
		dxl_setGoalPosition(2, -1000);
		HAL_Delay(2000);
		dxl_setGoalPosition(1, 0);
		dxl_setGoalPosition(2, 0);
		HAL_Delay(2000);
		dxl_torque(1, TORQUE_OFF);
		dxl_torque(2, TORQUE_OFF);


		dxl_setOperatingMode(1, VELOCITY_MODE);
		dxl_setOperatingMode(2, VELOCITY_MODE);

		term_printf("Hello!");


while(1){
	//mode auto
		while(rec_buf2[0]=='w' || rec_buf1[0] == 'w'){
			j= HAL_GPIO_ReadPin(GPIOA, GPIO_PIN_0);
							while(j==1) {
								dxl_torque(1, TORQUE_ON);
								dxl_torque(2, TORQUE_ON);
								dxl_setGoalVelocity(1, -110);
								dxl_setGoalVelocity(2, 110);
								j= HAL_GPIO_ReadPin(GPIOA, GPIO_PIN_0);

								}
							dxl_torque(1, TORQUE_OFF);
							dxl_torque(2, TORQUE_OFF);
							while(j==0) {
								dxl_torque(1, TORQUE_ON);
								dxl_torque(2, TORQUE_ON);
								dxl_setGoalVelocity(1, 100+x);
								dxl_setGoalVelocity(2, 0+x);
								j= HAL_GPIO_ReadPin(GPIOA, GPIO_PIN_0);
								}
								dxl_torque(1, TORQUE_OFF);
								dxl_torque(2, TORQUE_OFF);

							}



	    	if(rec_buf1[0]=='r' || rec_buf2[0] == 'r')
	    	{
	    		//term_printf("hello world \n\r");
	    	//arriere
	    		dxl_setOperatingMode(1, VELOCITY_MODE);
	    		dxl_setOperatingMode(2, VELOCITY_MODE);
	       	    dxl_torque(1, TORQUE_ON);
	       	    dxl_torque(2, TORQUE_ON);
	       	    dxl_setGoalVelocity(1, 140);
	       	    dxl_setGoalVelocity(2, -140);
	    	}

	    	//arriere rapide
	    	else if(rec_buf1[0]=='c' || rec_buf2[0] == 'c')
	       {
	    		dxl_setOperatingMode(1, VELOCITY_MODE);
	    		dxl_setOperatingMode(2, VELOCITY_MODE);
	    		dxl_torque(1, TORQUE_ON);
	    		dxl_torque(2, TORQUE_ON);
	    		dxl_setGoalVelocity(1, 200);
	    		dxl_setGoalVelocity(2, -200);
	    	}

	    	else if(rec_buf1[0]=='s')
	    	{
	    	 dxl_torque(1, TORQUE_OFF);
	    		    dxl_torque(2, TORQUE_OFF);
	    	}

	       	 //avant
	    	else if(rec_buf1[0]=='b' || rec_buf2[0] == 'b')
	    	{
	       	 dxl_setOperatingMode(1, VELOCITY_MODE);
	       	 dxl_torque(1, TORQUE_ON);
	       	 dxl_setGoalVelocity(1, -140);

	       	 dxl_setOperatingMode(2, VELOCITY_MODE);
	       	 dxl_torque(2, TORQUE_ON);
	       	 dxl_setGoalVelocity(2, 140);
	    	}

	    	//avant rapide
	    	else if(rec_buf1[0]=='l' || rec_buf2[0] == 'l')
	    	{
	    		dxl_setOperatingMode(1, VELOCITY_MODE);
	    		dxl_torque(1, TORQUE_ON);
	    		dxl_setGoalVelocity(1, -200);

	        	dxl_setOperatingMode(2, VELOCITY_MODE);
	    		dxl_torque(2, TORQUE_ON);
	    		dxl_setGoalVelocity(2, 200);
	    	}


	       	 //gauche arrière
	    	else if(rec_buf1[0]=='a' || rec_buf2[0] == 'a')
	    	{
	       	 	dxl_setOperatingMode(1, VELOCITY_MODE);
	       	 	 dxl_torque(1, TORQUE_ON);
	       	 	 dxl_setGoalVelocity(1, 140);

	       	 	 dxl_setOperatingMode(2, VELOCITY_MODE);
	       	 	  dxl_torque(2, TORQUE_ON);
	       	 	   dxl_setGoalVelocity(2, -30);
	    	}

	       	 //gauche avant
	    	else if(rec_buf1[0]=='t' || rec_buf2[0] == 't')
	    	{
	       	 	dxl_setOperatingMode(1, VELOCITY_MODE);
	       	 	 dxl_torque(1, TORQUE_ON);
	       	 	 dxl_setGoalVelocity(1, -140);

	       	 	 dxl_setOperatingMode(2, VELOCITY_MODE);
	       	 	  dxl_torque(2, TORQUE_ON);
	       	 	   dxl_setGoalVelocity(2, 30);
	    	}

	       	 	   //droite avant
	    	else if(rec_buf1[0]=='d' || rec_buf2[0] == 'd')
	    	{
		       	 	dxl_setOperatingMode(1, VELOCITY_MODE);
		       	 	 dxl_torque(1, TORQUE_ON);
		       	 	 dxl_setGoalVelocity(1, -30);

		       	 	 dxl_setOperatingMode(2, VELOCITY_MODE);
		       	 	  dxl_torque(2, TORQUE_ON);
		       	 	   dxl_setGoalVelocity(2, 140);
		       	    	}

    	 	   //droite arrière
	    	else if(rec_buf1[0]=='y' || rec_buf2[0] == 'y')
 	{
	       	 	dxl_setOperatingMode(1, VELOCITY_MODE);
	       	 	 dxl_torque(1, TORQUE_ON);
	       	 	 dxl_setGoalVelocity(1, 30);

	       	 	 dxl_setOperatingMode(2, VELOCITY_MODE);
	       	 	  dxl_torque(2, TORQUE_ON);
	       	 	   dxl_setGoalVelocity(2, -140);
	       	    	}


	    }
	    return 0;
}

//=====================================================================================
//		GPIO EXTERNAL INTERRUPT CALLBACK
//=====================================================================================
void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{
	switch(GPIO_Pin)
	{
	case GPIO_PIN_0 :
					break;
	case GPIO_PIN_13 :	term_printf("USER BUTTON PUSHED \n\r");	// USER BUTTON
					break;
	default : 		break;

	}
}
//=====================================================================================
//		TIMER INTERRUPT CALLBACK
//=====================================================================================
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim)
{
	if (htim==&TimHandle_period)
	{
		term_printf("Tick Timer period elapsed \n\r");
	}
}

//====================================================================================
