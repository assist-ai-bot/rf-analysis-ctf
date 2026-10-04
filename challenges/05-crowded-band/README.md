# 05 · Crowded Band

**Points:** 250 · **Level:** medium

## The story

Until now, each recording held one radio on one channel. This recording is much wider. It
covers 200 kHz of the radio band, and several stations are transmitting at the same time on
different channels. Some send data, some send other things.

The flag was sent in pieces, by more than one station.

## Your files

| File                       | What it is                                       |
|----------------------------|--------------------------------------------------|
| `wideband.sigmf-data/meta` | An 11.5-second recording, 200 000 samples/second |

## What you are told

- Channels are 12.5 kHz apart. Every channel sits at a multiple of 12.5 kHz from the middle of
  the recording: 0 Hz, ±12.5 kHz, ±25 kHz, and so on.
- Several channels are in use.
- The stations have different strengths and start at different times.
- Some stations send the same kind of data as in challenge 04.
- Each piece of the flag says which piece it is.
- Some stations are there only to distract you.

## The flag

Put the pieces together in the order they give. The result is the flag, written as
`RFCTF{...}`.
