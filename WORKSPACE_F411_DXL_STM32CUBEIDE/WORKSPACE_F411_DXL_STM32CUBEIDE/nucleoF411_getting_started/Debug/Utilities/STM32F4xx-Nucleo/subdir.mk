################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (10.3-2021.10)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Utilities/STM32F4xx-Nucleo/stm32f4xx_nucleo.c 

OBJS += \
./Utilities/STM32F4xx-Nucleo/stm32f4xx_nucleo.o 

C_DEPS += \
./Utilities/STM32F4xx-Nucleo/stm32f4xx_nucleo.d 


# Each subdirectory must supply rules for building sources it contributes
Utilities/STM32F4xx-Nucleo/%.o Utilities/STM32F4xx-Nucleo/%.su Utilities/STM32F4xx-Nucleo/%.cyclo: ../Utilities/STM32F4xx-Nucleo/%.c Utilities/STM32F4xx-Nucleo/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DSTM32 -DSTM32F4 -DSTM32F411RETx -DNUCLEO_F411RE -DDEBUG -DSTM32F411xE -DUSE_HAL_DRIVER -c -I"/home/kerhoas/WORKSPACE_WEB2/CONCEPTION_ROBOTIQUE_/WORKSPACE_F411_DXL_STM32CUBEIDE/nucleoF411_getting_started/HAL_Driver/Inc/Legacy" -I"/home/kerhoas/WORKSPACE_WEB2/CONCEPTION_ROBOTIQUE_/WORKSPACE_F411_DXL_STM32CUBEIDE/nucleoF411_getting_started/Utilities/STM32F4xx-Nucleo" -I"/home/kerhoas/WORKSPACE_WEB2/CONCEPTION_ROBOTIQUE_/WORKSPACE_F411_DXL_STM32CUBEIDE/nucleoF411_getting_started/inc" -I"/home/kerhoas/WORKSPACE_WEB2/CONCEPTION_ROBOTIQUE_/WORKSPACE_F411_DXL_STM32CUBEIDE/nucleoF411_getting_started/CMSIS/device" -I"/home/kerhoas/WORKSPACE_WEB2/CONCEPTION_ROBOTIQUE_/WORKSPACE_F411_DXL_STM32CUBEIDE/nucleoF411_getting_started/CMSIS/core" -I"/home/kerhoas/WORKSPACE_WEB2/CONCEPTION_ROBOTIQUE_/WORKSPACE_F411_DXL_STM32CUBEIDE/nucleoF411_getting_started/HAL_Driver/Inc" -O0 -ffunction-sections -Wall -fcommon -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Utilities-2f-STM32F4xx-2d-Nucleo

clean-Utilities-2f-STM32F4xx-2d-Nucleo:
	-$(RM) ./Utilities/STM32F4xx-Nucleo/stm32f4xx_nucleo.cyclo ./Utilities/STM32F4xx-Nucleo/stm32f4xx_nucleo.d ./Utilities/STM32F4xx-Nucleo/stm32f4xx_nucleo.o ./Utilities/STM32F4xx-Nucleo/stm32f4xx_nucleo.su

.PHONY: clean-Utilities-2f-STM32F4xx-2d-Nucleo

