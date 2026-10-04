# 09 · Hopscotch

**Points:** 450 · **Level:** hard

## The story

One station in this recording never stays on one channel. It sends a little, jumps to another
channel, sends a little more, and jumps again. It does this several times each second.

Three ordinary stations stay on fixed channels and keep transmitting the whole time.

The jumping station's message only makes sense when you follow it across the band and join its
pieces in the right order.

## Your files

| File                     | What it is                                      |
|--------------------------|-------------------------------------------------|
| `hopper.sigmf-data/meta` | A 6.5-second recording, 200 000 samples/second  |

## What you are told

**The channels**

- There are 16 channels, numbered 0 to 15. They are 12.5 kHz apart.
- Channel `k` sits at `(k − 7.5) × 12.5 kHz`. So channel 0 is at −93.75 kHz and channel 15 is
  at +93.75 kHz.
- Three channels are used by the fixed stations for the whole recording. They are not part of
  the message. The jumping station never uses those three channels.

**The jumping station**

- It sends bits by moving its signal a little above the channel centre for one bit value, and
  the same amount below for the other. There are no audio tones.
- The speed is 1200 bits per second.
- Each byte is sent as 10 bits: one start bit (`0`), eight data bits (lowest bit first), one
  stop bit (`1`). When nothing is being sent, the line stays at `1`.
- The bytes are ASCII text.
- Every jump carries whole bytes. No byte is split between two jumps.

**What you are not told**

- How long the station stays on each channel.
- The order of the channels.
- How far the signal moves above and below the centre.
- Which side means `1`.

## The flag

The joined-up text contains the flag, written as `RFCTF{...}`. The message repeats, so you
will see the flag more than once.
