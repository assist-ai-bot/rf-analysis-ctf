# 07 · Who Keyed Up?

**Points:** 350 · **Level:** hard

## The story

Six people each carry a walkie-talkie. All six radios are the same make and model, and all are
set to the same channel.

Sixteen times, someone pressed the talk button and said nothing. Your job is to say which
radio it was, each time.

The recordings contain no voice, no name and no data. There is only the bare radio signal.
These are real recordings of real radios. Nothing was added to mark one radio from another. If
the radios can be told apart, it is because of how each radio itself behaves.

## Your files

| Path                              | What it is                                             |
|-----------------------------------|--------------------------------------------------------|
| `reference/radio_A_1 … radio_F_3` | Three labelled recordings of each radio, A to F        |
| `unknown/unknown_01 … unknown_16` | Sixteen recordings with no label                       |

Every recording is 1.5 seconds long, at 25 000 samples per second.

## What you are told

- One receiver made all the recordings. It was tuned to the same frequency every time.
- Each recording is a different transmission. No unknown recording is a copy of a reference
  recording.
- Signal strength changes from one recording to the next. It does not tell you which radio it
  is.
- Each unknown recording comes from exactly one of the six radios.

## The flag

The letters of the radios that made `unknown_01` to `unknown_16`, in that order, with nothing
between them.

Example: if the first three unknowns are radios C, A and C, the flag starts `RFCTF{CAC…`. The
full flag has sixteen letters.
