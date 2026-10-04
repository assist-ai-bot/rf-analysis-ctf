# 06 · Quiet Carrier

**Points:** 300 · **Level:** medium to hard

## The story

A radio is transmitting, but nobody is speaking. On a spectrogram you see one clean line. On a
speaker you hear silence. The operator says nothing is being sent.

That is not true. Something is pushing the signal up and down by a tiny amount, and those tiny
pushes are data.

## Your files

| File                           | What it is                                     |
|--------------------------------|------------------------------------------------|
| `idle_carrier.sigmf-data/meta` | A 7.5-second recording, 25 000 samples/second  |

## What you are told

- The strength of the signal carries no information.
- The data is a stream of bits.
- Each byte is sent as 10 bits: one start bit (`0`), eight data bits (lowest bit first), one
  stop bit (`1`). When nothing is being sent, the line stays at `1`.
- The bytes are ASCII text.
- You are **not** told the speed, the size of the push, or which direction means `1`.

## The flag

The decoded text contains the flag, written as `RFCTF{...}`.
