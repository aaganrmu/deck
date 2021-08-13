# Hardware planning

## Electronics

### Raspberry PI

- Power switch
- Shutdown button (GPIO)
- Secondary display button (GPIO, toggles/cycles python script that draws)
- Main display switch (GPIO, toggles `vcgencmd display_power 0/1`)
- Status LED (lightpipe/solder on new one)

### Main display

- Power switch

### Secondary display

- Hardware status (time/cpu/disk/mem/IP/wifi)
- Nice logos
- Big timer
- Switchable by button

### Powerbank

- Status LEDS (lightpipes/solder on new ones)

### Keyboard

- Can be removed?

### Other IO

- Buzzer?
- Acceleration sensors?

### Ports

- Charging port
- Remaining GPIO?
- 3.5 mm jack?

## AESTHETICS

- Body: old cheap keyboard kit? Other portable device that's cheap?
- Cyrilic keyboard because why not.
- ASCII art on boot.
- Stickers/labels everywhere.
- ASCII art on secondary display is an option.
- Carry handle(s).
- Scuffed.
- 

## Software

### Hardware service
Handles GPIO buttons, leds, secondary display etc.

### Timer scripts?
Visible on secondary display, buzzer