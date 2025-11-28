#
# @brief   mypro
# @version 1.0.1
# @date    2025-11-28
# @company None, free software to use 2025
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

include toolchain.mk
include cflags.mk
include odflags.mk
include csflags.mk
include sources.mk
include objects.mk

EXECUTABLE = mypro

LSS += \
	$(EXECUTABLE).lss

SIZEDUMMY += \
	sizedummy

CLEAN_LIST += \
	$(OBJECTS) \
	$(SIZEDUMMY) \
	$(LSS) \
	$(EXECUTABLE)

all: $(SOURCES) $(EXECUTABLE) $(LSS) $(SIZEDUMMY)

$(OBJECTS): $(SOURCES)
	@echo 'Invoking: compile unit'
	$(CC) $(CFLAGS) -c -o $@ $<
	@echo ' '

$(EXECUTABLE): $(OBJECTS)
	@echo 'Invoking: link executable'
	$(CC) $(CFLAGS) -o $@ $^
	@echo 'Finished building: $@'
	@echo ' '

$(EXECUTABLE).lss: $(EXECUTABLE)
	@echo 'Invoking: create extended listing'
	$(OD) $(ODFLAGS) $(EXECUTABLE) > $@
	@echo 'Finished building: $@'
	@echo ' '

sizedummy: $(EXECUTABLE)
	@echo 'Invoking: print size'
	$(CS) $(CSFLAGS) $(EXECUTABLE)
	@echo 'Finished building: $@'
	@echo ' '

clean:
	@for item in $(CLEAN_LIST);do echo "${RM} $${item}";$(RM) $$item;done
	@echo ' '

.PHONY: all clean

