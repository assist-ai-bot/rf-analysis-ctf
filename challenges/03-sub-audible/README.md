# 03 · Sub-Audible

**Points:** 150 · **Level:** easy

## The story

Four people share one radio channel. Each person has set a different "privacy tone" on their
radio. A privacy tone is a low hum that the radio adds under the voice. It is too low to
notice when you listen, but it is there.

Each of the four people speaks once. Find the tone that each radio uses.

## Your files

| File                                 | What it is                                   |
|--------------------------------------|----------------------------------------------|
| `four_transmissions.sigmf-data/meta` | A 26-second recording, 25 000 samples/second |

## What you are told

- There are four transmissions, one after the other. Each comes from a different radio.
- Some transmissions are stronger than others.
- All four are FM. Each carries speech-like sound and one steady privacy tone.
- The technical name for the privacy tone is **CTCSS**.
- Every tone is one of these standard frequencies, in hertz:

```
 67.0  69.3  71.9  74.4  77.0  79.7  82.5  85.4  88.5  91.5
 94.8  97.4 100.0 103.5 107.2 110.9 114.8 118.8 123.0 127.3
131.8 136.5 141.3 146.2 151.4 156.7 162.2 167.9 173.8 179.9
186.2 192.8 203.5 210.7 218.1 225.7 233.6 241.8 250.3
```

## The flag

The four tones in the order they were sent. Write each one exactly as it appears in the table
above, and join them with underscores.

Example: if the tones are 67.0, then 100.0, then 250.3, then 88.5, the flag is
`RFCTF{67.0_100.0_250.3_88.5}`.
