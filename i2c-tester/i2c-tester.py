# from smbus import SMBus

address = 0
bus = SMBus(1)

while True:
    print('0: Set Address\n1: Write Data\n2: Read Data\n')
    cmd = int(input('Command>>>'))
    if (cmd == 0):
        address = int(input('Address>>>'))
    elif (cmd == 1):
        bus.write_byte(address, int(input('Data [0:255]>>>')))
    elif (cmd == 2):
        print(bus.read_byte(address))
    else:
        print('Invalid Command')
