# Hardware Scanner

This repository contains a small Python script that collects information about the processor(s) of a Windows machine using WMI and prints the details to the console.

I'll make collect more information after!

## What the code does
- Opens a WMI connection to access hardware information.
- Retrieves all `Win32_Processor` objects, covering every installed CPU.
- For each CPU, prints:
  - Name and manufacturer.
  - Current frequency (`CurrentClockSpeed`) and maximum frequency (`MaxClockSpeed`).
  - Physical core count (`NumberOfCores`) and logical cores/threads (`NumberOfLogicalProcessors`).
  - Socket, `DeviceID`, and `ProcessorId`.
- On failure, catches the exception and prints the error message.

## Main file
- Script: [hardware_scanner/cpu.py](hardware_scanner/cpu.py)
- Entry point: calls `cpu_info()` when executed directly.

## Requirements
- Windows (the script uses WMI).
- Python 3.8+.
- `wmi` library installed.

### Install dependency
```bash
pip install wmi
```

## How to run
From the project directory:
```bash
python hardware_scanner/cpu.py
```

## Expected output (example)
```
========================================
CPU: 0
========================================
Name: Intel(R) Core(TM) ...
Manufacturer: GenuineIntel
Current Frequencie: 3200MHz
Maximum Frequencie: 3600MHz
Cores: 4
Threads: 8
Socket: U3E1
Device ID: CPU0
Processor ID: BFEBFBFF000906EA
```

## Notes
- Some values may vary depending on permissions or BIOS/firmware configuration.
- On systems with multiple physical CPUs, the script prints one block per position.
