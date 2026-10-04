# 10 · One True Radio

**Points:** 500 · **Level:** hardest

## The story

A station called `K7ILO` is sending a secret key. The key is 32 characters long and is sent in
eight pieces.

Four other radios are pretending to be `K7ILO`. They use the same name, the same message
format and the same channels. Each of them sends eight pieces of a key that is wrong.

Every message decodes without errors. Nothing written in a message tells you if it is real.

You have one extra file: a clean recording of the real radio, made earlier.

## Your files

| File                                      | What it is                                                      |
|-------------------------------------------|-----------------------------------------------------------------|
| `net_traffic.sigmf-data/meta`             | All the messages. 20.3 seconds, 100 000 samples/second          |
| `genuine_radio_reference.sigmf-data/meta` | The real radio transmitting with no sound. 1.5 seconds, 25 000 samples/second |

## What you are told

**The channels**

- Four channels are used. They sit at −37.5 kHz, −12.5 kHz, +12.5 kHz and +37.5 kHz.
- The radios move between the channels. The channel does not tell you who is sending.
- Signal strength changes from message to message. It does not tell you who is sending either.

**The messages**

- There are 40 messages: eight from each of the five radios.
- Each message is one short FM transmission. It carries data in the same way as challenge 04.
- The text of each message looks like `K7ILO F<n>/8 <four hex characters>`. Here `<n>` is the
  piece number, from 1 to 8.

**The recordings**

- One receiver made both recordings.

## The flag

Take the four hex characters from pieces 1 to 8 **of the real radio**, in order, with nothing
between them.

Example: if the real pieces are `0a1b`, `2c3d`, and so on, the flag starts
`RFCTF{0a1b2c3d…`. The part inside the braces is 32 lower-case hex characters.
