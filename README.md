# RF Analysis Track

Welcome. This track has ten challenges about radio signals. They start easy and get harder.

In each challenge you get a recording of a radio signal. Somewhere in that recording is a
**flag**. Your job is to find it and submit it in the CTFd portal, under **RF Analysis Track**.

You do not need a radio. You do not need to know anything about radio yet. You need Python,
patience, and the habit of plotting things until they make sense.

## The challenges

| #  | Challenge                                         | Points | Level          |
|----|---------------------------------------------------|-------:|----------------|
| 01 | [Dots and Dashes](challenges/01-dots-and-dashes/) |     50 | Warm-up        |
| 02 | [The Header Lies](challenges/02-the-header-lies/) |    100 | Easy           |
| 03 | [Sub-Audible](challenges/03-sub-audible/)         |    150 | Easy           |
| 04 | [Modem Hiss](challenges/04-modem-hiss/)           |    200 | Medium         |
| 05 | [Crowded Band](challenges/05-crowded-band/)       |    250 | Medium         |
| 06 | [Quiet Carrier](challenges/06-quiet-carrier/)     |    300 | Medium to hard |
| 07 | [Who Keyed Up?](challenges/07-who-keyed-up/)      |    350 | Hard           |
| 08 | [Under the Floor](challenges/08-under-the-floor/) |    400 | Hard           |
| 09 | [Hopscotch](challenges/09-hopscotch/)             |    450 | Hard           |
| 10 | [One True Radio](challenges/10-one-true-radio/)   |    500 | Hardest        |

Each challenge has its own folder. Inside you will find:

- the recording files;
- a `README.md` that tells you the story, what the files are, what you are told about the
  signal, and what the flag looks like.

**Do the challenges in order.** Later challenges reuse the code you write for earlier ones. If
you skip ahead, you will have to come back.

## Hints

The challenge pages do not contain hints. Hints are in the CTFd portal, on each challenge.
Opening a hint costs points, so try on your own first.

## Flags

- Every flag looks like `RFCTF{...}`.
- In some challenges you decode a text message, and the flag appears inside it. Submit it
  exactly as you see it.
- In other challenges you build the flag from what you find. The challenge page shows the
  exact format, with an example.
- Capital and small letters matter.
- You never need to guess a flag. If you are guessing, you have missed a step. Go back to the
  signal.

## Setting up

You need Python 3.

```bash
git clone https://github.com/assist-ai-bot/rf-analysis-ctf.git
cd rf-analysis-ctf
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Now check that everything works:

```bash
python3 tools/rfctf.py challenges/01-dots-and-dashes/keyed_carrier
```

This prints a few facts about the first recording and saves a picture of it in the same
folder. If you see that, you are ready.

## Read this first

Before you start challenge 01, read [docs/primer.md](docs/primer.md). It is one page. It
explains:

- what a radio recording is;
- how to load one in Python;
- the few basic steps that every challenge is built from.

## The recording files

Nine of the ten challenges use a standard format called **SigMF**. One recording is two files
with the same name:

| File              | What is inside                                               |
|-------------------|--------------------------------------------------------------|
| `name.sigmf-meta` | A small text file. It gives the sample rate and a short note |
| `name.sigmf-data` | The recording itself, as a long list of numbers              |

The numbers are 16-bit whole numbers. They come in pairs: the first of each pair is called
**I** and the second is called **Q**. One pair is one sample. The primer explains what I and Q
mean.

You can load a recording like this:

```python
import json
import numpy as np

meta = json.load(open("name.sigmf-meta"))
raw  = np.fromfile("name.sigmf-data", dtype="<i2").astype(np.float64)

iq = raw[0::2] + 1j * raw[1::2]                # one complex number per sample
fs = meta["global"]["core:sample_rate"]        # samples per second
```

The file `tools/rfctf.py` has a function `load_sigmf()` that does the same thing, and a few
other small helpers. You may use it or write your own.

Challenge 02 is different. It gives you a `.wav` file, and understanding that file is part of
the challenge.

## Tools

You can solve every challenge with Python and `numpy`. The package `scipy` saves some typing,
and `matplotlib` draws the plots.

These free programs are also useful. None of them is required.

| Program                                                 | What it is good for                          |
|---------------------------------------------------------|----------------------------------------------|
| [inspectrum](https://github.com/miek/inspectrum)        | Scrolling through a recording as a picture   |
| [Universal Radio Hacker](https://github.com/jopohl/urh) | Looking at simple digital signals            |
| [Audacity](https://www.audacityteam.org/)               | Listening to sound you have recovered        |
| [GNU Radio](https://www.gnuradio.org/)                  | Building a receiver from ready-made blocks   |
| [minimodem](https://github.com/kamalmostafa/minimodem)  | Decoding common sound-based modems           |

We suggest you write your own code for the early challenges. The later ones are much easier
when you understand each step yourself.

## Rules

1. Work alone, unless your organiser tells you otherwise.
2. Do not try many flags in the portal hoping one is right.
3. Do not share flags or solutions with other participants during the event.
4. Keep notes. You may be asked to explain how you found a flag.
5. If you think a challenge is broken, tell an organiser. Do not tell other participants.

## Where the signals come from

The radio signals in this track are real. They were recorded from real walkie-talkies and
published as a public dataset:

> Muhammad Zahid, *CommRad RF: A dataset of communication radio signals for detection,
> identification and classification*, Zenodo, 2024.
> <https://zenodo.org/records/14192970> (licence: CC BY 4.0)

In the original recordings, someone presses the talk button on a radio and says nothing. For
this track we took those recordings and changed them: we cut them, added messages to them,
mixed several together and, in some challenges, added noise.

The small quirks of each radio are still in the recordings. They belong to the real radios.

You do not need to download the dataset.

## What is in this repository

```
README.md               this page
docs/primer.md          the background you need, in one page
tools/rfctf.py          small helper functions (optional)
requirements.txt        the Python packages to install
challenges/NN-name/     one folder per challenge: its README and its recordings
```

## Licence

The code and text here use the MIT licence. The recordings are based on the CommRad RF dataset
and are shared under CC BY 4.0, the same licence as the original. See [LICENSE](LICENSE).
