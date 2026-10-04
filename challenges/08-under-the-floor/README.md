# 08 · Under the Floor

**Points:** 400 · **Level:** hard

## The story

This channel looks simple. You see noise, and you see one strong signal from a walkie-talkie a
few kilohertz from the middle. That strong signal is not the one you want.

A second transmitter is also here. It is weaker than the noise at every moment and at every
frequency, so no plot of the recording will show it. You can still read it, because you know
the secret pattern it uses.

## Your files

| File                            | What it is                                    |
|---------------------------------|-----------------------------------------------|
| `noisy_channel.sigmf-data/meta` | A 4.6-second recording, 25 000 samples/second |

## What you are told

The hidden signal uses a method called **direct-sequence spread spectrum**. The sender takes
each data bit and multiplies it by a long, fast pattern of +1 and −1 values. Each value in the
pattern is called a **chip**.

**Where it is.** Exactly in the middle of the recording (0 Hz).

**How fast.** 12 500 chips per second. Each chip is exactly 2 samples long.

**The pattern.** It is 127 chips long and repeats with no gaps. Build it like this:

```
s[0] … s[6] = 1
s[n] = s[n-7] XOR s[n-4]        for n = 7 … 126
```

Then turn each bit into a chip: bit `0` becomes `+1`, bit `1` becomes `-1`.

To check your work, the first 24 chips are:

```
-------++++---+----++-+-
```

**The data.** One data bit is sent for each full pattern (127 chips, which is 254 samples).

- If the data bit is `1`, the pattern is sent with the opposite sign to the pattern before it.
- If the data bit is `0`, the pattern is sent with the same sign as the pattern before it.

**The bytes.** ASCII text, eight bits per byte, highest bit first. There are no start or stop
bits.

**The start.** The hidden signal does not begin at the start of the recording. You are not
told where it begins.

## The flag

The decoded text contains the flag, written as `RFCTF{...}`.
