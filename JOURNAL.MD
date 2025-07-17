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