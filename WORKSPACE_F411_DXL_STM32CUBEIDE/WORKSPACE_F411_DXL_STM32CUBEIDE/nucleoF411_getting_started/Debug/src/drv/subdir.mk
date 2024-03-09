################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (10.3-2021.10)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/drv/drv_i2c.c \
../src/drv/drv_spi.c \
../src/drv/drv_uart.c 

OBJS += \
./src/drv/drv_i2c.o \
./src/drv/drv_spi.o \
./src/drv/drv_uart.o 

C_DEPS += \
./src/drv/drv_i2c.d \
./src/drv/drv_spi.d \
./src/drv/drv_uart.d 


# Each subdirectory must supply rules for building sources it contributes
src/drv/%.o src/drv/%.su src/drv/%.cyclo: ../src/drv/%.c src/drv/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DSTM32 -DSTM32F4 -DSTM32F411RETx -DNUCLEO_F411RE -DDEBUG -DSTM32F411xE -DUSE_HAL_DRIVER -c -I"/home/kerhoas/WORKSPACE_WEB2/CONCEPTION_ROBOTIQUE_/WORKSPACE_F411_DXL_STM32CUBEIDE/nucleoF411_getting_started/HAL_Driver/Inc/Legacy" -I"/home/kerhoas/WORKSPACE_WEB2/CONCEPTION_ROBOTIQUE_/WORKSPACE_F411_DXL_STM32CUBEIDE/nucleoF411_getting_started/Utilities/STM32F4xx-Nucleo" -I"/home/kerhoas/WORKSPACE_WEB2/CONCEPTION_ROBOTIQUE_/WORKSPACE_F411_DXL_STM32CUBEIDE/nucleoF411_getting_started/inc" -I"/home/kerhoas/WORKSPACE_WEB2/CONCEPTION_ROBOTIQUE_/WORKSPACE_F411_DXL_STM32CUBEIDE/nucleoF411_getting_started/CMSIS/device" -I"/home/kerhoas/WORKSPACE_WEB2/CONCEPTION_ROBOTIQUE_/WORKSPACE_F411_DXL_STM32CUBEIDE/nucleoF411_getting_started/CMSIS/core" -I"/home/kerhoas/WORKSPACE_WEB2/CONCEPTION_ROBOTIQUE_/WORKSPACE_F411_DXL_STM32CUBEIDE/nucleoF411_getting_started/HAL_Driver/Inc" -O0 -ffunction-sections -Wall -fcommon -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-src-2f-drv

clean-src-2f-drv:
	-$(RM) ./src/drv/drv_i2c.cyclo ./src/drv/drv_i2c.d ./src/drv/drv_i2c.o ./src/drv/drv_i2c.su ./src/drv/drv_spi.cyclo ./src/drv/drv_spi.d ./src/drv/drv_spi.o ./src/drv/drv_spi.su ./src/drv/drv_uart.cyclo ./src/drv/drv_uart.d ./src/drv/drv_uart.o ./src/drv/drv_uart.su

.PHONY: clean-src-2f-drv

