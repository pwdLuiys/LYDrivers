def cpu_info():
    import wmi
    try:
        def line(msg):
            print('=' * 40)
            print(msg)
            print('=' * 40)

        # Connect WMI with the 'target' we want, in this case, the CPU, the processor.
        connect = wmi.WMI()

        # Then we create a var that will recieve ALL the content for ALL processors in your pc.
        fCpu = connect.Win32_Processor()

        # For each CPU and their position in your Personal Computer/Server, show on the screen:
        for position, cpu in enumerate(fCpu):
            line(f'CPU: {position}')
            print(f'Name: {cpu.Name}')
            print(f'Manufacturer: {cpu.Manufacturer}')
            print(f'Current Frequencie: {cpu.CurrentClockSpeed}MHz')
            print(f'Maximum Frequencie:  {cpu.MaxClockSpeed}MHz')
            print(f'Cores: {cpu.NumberOfCores}')
            print(f'Threads: {cpu.NumberOfLogicalProcessors}')
            print(f'Socket: {cpu.SocketDesignation}')
            print(f'Device ID: {cpu.DeviceID}')
            print(f'Processor ID: {cpu.ProcessorId}')
    except Exception as error1:
        print(f'Error: {error1}')
        return None
if __name__ == "__main__":
    cpu_info()
