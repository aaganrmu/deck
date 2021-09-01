# Hardware planning

## Electronics

### Raspberry PI

- GPIO header directly attached to board
- Power switch
- Shutdown button (GPIO)
- Secondary display mode button (GPIO, toggles/cycles python script that draws)
- Monitor display switches to disable them (GPIO, `vcgencmd display_power 0/1` for main and stops service for secondary)
- Status LED (GPIO)

### Main display

- Power switch
- Buttons for menu, custom board?

### Secondary display

- Hardware status (time/cpu/disk/mem/IP/wifi)
- Nice logos
- Mode switchable by button
- Power switch (USE 3.3V RAIL)

### Powerbank

- Status LEDS (lightpipes/solder on new ones)

### Keyboard

- USB, wired
- Can be removed?

### Other IO

- Buzzer?
- Acceleration sensors?

### Ports

- Charging port
- More USB-ports
- Ethernet?
- Remaining GPIO?
- 3.5 mm jack?

## AESTHETICS

- Body: ~~old cheap keyboard kit? Other portable device that's cheap?~~ It will never fit, build something myself. Wood frame for strenght, plastic plates for body. Or triplex + paint.
- Cyrilic keyboard because why not.
- ASCII art on boot.
- Stickers/labels everywhere.
- ASCII art on secondary display is an option.
- Carry handle(s).
- Scuffed.
