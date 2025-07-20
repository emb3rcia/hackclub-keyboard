---
title: "hackclub-keyboard"
author: "emb3rcia"
description: "First keyboard i fully made! Also replacement for my old keyboard bought for ~7.5$ with dying spacebar"
created_at: "2025-7-17"
---

# July 17: Started the project!
3:50 PM | About 2 hours ago i started planning out the project in notepad, slept for 30 mins, woke up fresh after a nap and made first iteration product list
| Amount and item | Link | Price (in PLN) | Description of item |
| ----------- | ----------- | ----------- | ----------- |
| 1x RP2040-zero | [link](https://botland.com.pl/plytki-z-mikrokontrolerem-rp2040/20536-rp2040-zero-plytka-z-mikrokontrolerem-rp2040-wersja-mini-waveshare-20187-5904422381561.html) | 17.90 | MCU |
| 1x MCP23017 | [link](https://botland.com.pl/ekspandery-wyprowadzen/2556-mcp23017-ekspander-wyprowadzen-i2c-16-kanalowy-5904422373399.html) | 11.90 | MCU Pin extender |
| 100x 1N4148 | [link](https://botland.com.pl/diody-prostownicze/4927-dioda-prostownicza-1n4148-100v-015a-10szt-5903351244442.html) | 9.00 | Diodes to make diode matrix layout and ensure antighosting, 12 more than required in case of DOA ones etc|
| 100x LED-ALS-1206W-00330-120 | [link](https://kamami.pl/diody-led-smd/59133-dioda-led-biala-1206-kat-120o-swiatlosc-1500-mcd-20ma-32v-rohs-5906623491957.html) | 58.00 | SMD Diodes for backlight, they are constant white as i dont need some fancy rgb, just to see keys in darkness, same, 12 more than required in case of DOA ones etc |
| 110x Gateron Hot-Swap Switch Socket | [link](https://allegro.pl/oferta/gniazda-gateron-hot-swap-switch-socket-110-szt-13664414479?bi_s=ads&bi_m=showitem%3Adesktop%3Atop%3Aactive&bi_c=MjA3ZDkwMWQtM2U0Zi00NWIxLTgwZTYtODgxNGNlODQ1MTAxAA&bi_t=ape&emission_unit_id=c762ae35-7e58-4859-bbe5-7aaf79941617) | 99.95 | Sockets ensuring that keyboard is hot-swappable, 22 more because i couldn't find cheap switch sockets that wasn't few weeks/months to deliver, and deadline is in 2 weeks |
| 120x GLORIOUS PC Kailh Box Brown | [link](https://www.mediaexpert.pl/komputery-i-tablety/klawiatury-komputerowe/przelaczniki-do-klawiatur/przelaczniki-glorious-pc-kailh-box-brown-120-szt?gQT=2) | 119.00 | Switches, same as with sockets, also i couldn't even find ones that were cheaper than these, most of them were like 2.5-3.5 PLN per, which would have been too much money |
| 1x SH1106 OLED 1,3'' 128x64px | [link](https://botland.com.pl/wyswietlacze-oled/8246-wyswietlacz-oled-niebieski-graficzny-13-128x64px-i2c-v2-niebieskie-znaki-5904422311339.html) | 29.90 | OLED Screen |
| 1x DFRobot EC11 | [link](https://botland.com.pl/enkodery/9533-czujnik-obrotu-impulsator-enkoder-obrotowy-dfrobot-ec11-6959420912414.html) | 13.90 | Volume Knob |
| 88x Keycap | already have in my current keyboard | 0.00 | Keycaps |
| kamami.pl delivery | - | 8.90 | - |
| botland.com.pl delivery | - | 8.99 | - |
| Other deliveries | - | 0.00 | They are free |
| Total | - | 377.44 PLN (~102.72 USD) | - |

I searched for local sites for cheaper (and primarily faster) deliveries. Also i found that some of the items like switches, sockets and LEDs were cheaper in Poland, I would probably find them even cheaper on Aliexpress, but delivery time would be enormous.

anyways, its 4:18 PM, i am going to start making PCB

5:58 PM ended designing for today


# July 18: Journal, PCB and possibly a case!
7:05 PM, made hackatime account and connected it to VSC few seconds ago! Right now i am going to add images for what i had done yesterday as i forgot to do that then. After that i will continue making PCB!
![Oh no! The image didn't load :<. It was an image of schematic at the time of writing it. Please send an message to me on slack about it, i will fix is ASAP!](assets/schematic-july18.png)
On the right you can see keyboard switch sockets, it is wired like mess cause i wanted to make it in the size and shape of actual keyboard for reference! Although i know i will need to make it again later in pcb editor :<
Decided to change rp2040-zero for rpi pico as it has more ports, for the few missing needed ports i will use Waveshare 3708 PCF8574 expander module as it costs only 2 PLN (less than half a dollar!) more, i dont need to use pull-up resistors etc which will simplify pcb and will be also cheaper in the long term probably. And it gives me more than enough ports!
Resigned from screen and expander whatsoever, after a bit of thinking i came to conclusion that i dont need it, i wouldn't see the screen anyway *(i was stuck at writing this word for a minute cause i forgot that it is anyway not anywhere and was sensing i wrote it wrong lol)* and it is only complicating the PCB and making whole thing bigger
I also resigned from LED backlighting, i figured it is too much work for me as it is my second hardware project ever, and first keyboard (excluding hackpad), especially since it has hot-swap.
10:41 PM ended designing for today, almost 4h straight, at the end: i resigned from screen, expander and backlighting. Connected everything in schematic. Laid out everything on PCB. Left for me for making phisical part of the project is wire everything together using paths and design 3d case for it. And of course connect it all when it arrives.
![Oh no! The image didn't load :<. It was a screenshot from PCB Editor in KiCad at the time of writing it. Please send an message to me on slack about it, i will fix is ASAP!](assets/pcb-july18.png)

# July 19: The day of making traces
7:06 PM starting working on PCB, need to make traces for everything, but first i will label each key socket for convienency
8:15 PM finished routing traces! This is how it looks now:
![Oh no! The image didn't load :<. It was a screenshot from PCB Editor in KiCad at the time of writing it. Please send an message to me on slack about it, i will fix is ASAP!](assets/pcb-july19.png)
And this is how it looks in KiCad 3D model viewer:
![Oh no! The image didn't load :<. It was a screenshot from PCB 3D Model Viewer in KiCad at the time of writing it. Please send an message to me on slack about it, i will fix is ASAP!](assets/pcb-3d-july19.png)
8:36 PM - 9:41 PM took a break for food, right now i need to make case
10:12 PM ending designing for today, hoping tommorow will be last day of designing! Make body of the case (well, kinda), tommorow need to make plate etc

# July 20: The birth of the case
3:53 PM i am starting 3d modeling for today, hoping it wouldn't be as big of a chore as i suppose
5:24 PM ended designing 3d case! It wasnt as frustrating as i thought.
5:53 PM made screw holes i forgot to do! i am gonna add images to the journal of project rn!
![Oh no! The image didn't load :<. It was a screenshot from Fusion 360 at the time of writing it. Please send an message to me on slack about it, i will fix is ASAP!](assets/3d-july20-1.png)
![Oh no! The image didn't load :<. It was a screenshot from Fusion 360 at the time of writing it. Please send an message to me on slack about it, i will fix is ASAP!](assets/3d-july20-2.png)
![Oh no! The image didn't load :<. It was a screenshot from Fusion 360 at the time of writing it. Please send an message to me on slack about it, i will fix is ASAP!](assets/3d-july20-3.png)
![Oh no! The image didn't load :<. It was a screenshot from Fusion 360 at the time of writing it. Please send an message to me on slack about it, i will fix is ASAP!](assets/3d-july20-4.png)