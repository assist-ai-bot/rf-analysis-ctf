# 02 · The Header Lies

**Points:** 100 · **Level:** easy

## The story

A colleague gives you one file from a public collection of walkie-talkie recordings. Their
note says:

> "It opens in any audio player, but it sounds like rubbish. The radio was sending something.
> I think the file is not what it claims to be."

## Your files

| File               | What it is                                                        |
|--------------------|-------------------------------------------------------------------|
| `capture_0042.wav` | One recording, stored the same way as every file in that collection |

## What you are told

- The file is a valid WAV file.
- Its header says: two channels, 32-bit samples, 50 000 samples per second.
- The header is misleading. The file really holds one radio recording made of I/Q samples.
- The radio is an FM walkie-talkie.
- While it transmits, someone presses keys on its keypad. Each key makes a tone, like the keys
  on a telephone.

## The flag

The keys that were pressed, in order, with nothing between them.

Example: if the keys are `1`, `2`, `3`, the flag is `RFCTF{123}`.
