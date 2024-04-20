def initialize_dio_register():
    port = input("type PORTA or PORTB or PORTC or PORTD")
    state = str(input("type INPUT or OUTPUT or IN_PULLUP"))
    pin_number = int(input("type pin number from 0 to 7"))
    pin_direction = open("embedded c/DIO/set_pin_direction.txt", "r")
    config_file.write(f"void DIO_vSetPinDirection({port}, {pin_number}, {state})\n")
    config_file.write(pin_direction.read())

def DIO_WRITE_PIN():
    port = input("type PORTA or PORTB or PORTC or PORTD")
    value = str(input("type HIGH or LOW"))
    pin_number = int(input("type pin number from 0 to 7"))
    DIO_WRITE_FILE=open("embedded c/DIO/DIO_write_pin.txt" , "r")
    config_file.write(f"\nvoid DIO_vWritePin({port}, {pin_number}, {value})\n")
    config_file.write(DIO_WRITE_FILE.read())

def DIO_TOGGLE_PIN():
    port = input("type PORTA or PORTB or PORTC or PORTD")
    pin_number = int(input("type pin number from 0 to 7"))
    DIO_TOGGLE_FILE = open("embedded c/DIO/DIO_Toggle_pin.txt", "r")
    config_file.write(f"\nvoid DIO_vTogglePin({port}, {pin_number})\n")
    config_file.write(DIO_TOGGLE_FILE.read())

def DIO_GET_PIN_VALUE():
    port = input("type PORTA or PORTB or PORTC or PORTD")
    pin_number = int(input("type pin number from 0 to 7"))
    DIO_GET_PIN_FILE = open("embedded c/DIO/DIO_Get_pin_value.txt", "r")
    config_file.write(f"\nuint8 DIO_u8GetPinValue({port}, {pin_number})\n")
    config_file.write(DIO_GET_PIN_FILE.read())

dio_interface = open("embedded c/DIO/DIO_Interface.h", "r")
print(dio_interface.read())
config_file = open("config_file.c", "r+")

initialize_dio_register()
DIO_WRITE_PIN()
DIO_TOGGLE_PIN()
DIO_GET_PIN_VALUE()
config_file.close()