# 04 · Modem Hiss

**Points:** 200 · **Level:** medium

## The story

Someone has connected a modem to a walkie-talkie. When the radio transmits, you do not hear a
voice. You hear a harsh, warbling hiss. That hiss is text, sent as sound.

## Your files

| File                     | What it is                                    |
|--------------------------|-----------------------------------------------|
| `beacon.sigmf-data/meta` | An 8.7-second recording, 25 000 samples/second |

## What you are told

- There is one FM transmission.
- The sound it carries is made of two tones. A `1` bit is a 1200 Hz tone. A `0` bit is a
  2200 Hz tone. This scheme is called **Bell 202**.
- The speed is 1200 bits per second.
- Each byte is sent as 10 bits:
  - one start bit, which is always `0`;
  - eight data bits, lowest bit first;
  - one stop bit, which is always `1`.
- When nothing is being sent, the line stays at `1`.
- The bytes are plain ASCII text.

## The flag

The text contains the flag, written as `RFCTF{...}`. Submit it exactly as you decode it.

Keep the decoder you write here. You will use it again in later challenges.
