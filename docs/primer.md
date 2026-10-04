# RF primer

This page gives you the background for the whole track. Read it once before challenge 01. Come
back to it when you are stuck.

Words in **bold** are terms you will see again in the challenges.

## 1. What is in a recording

A radio receiver listens to a small part of the radio band. The middle of that part is called
the **centre frequency**. The receiver measures the signal many times each second and saves
each measurement. One measurement is one **sample**.

Each sample is a pair of numbers, called **I** and **Q**. In Python we store the pair as one
complex number: `I + jQ`.

A good way to picture one sample is as an arrow drawn from the middle of a clock face:

- The **length** of the arrow is how strong the signal is at that moment. This is the
  **amplitude**.
- The **direction** of the arrow is called the **phase**.
- From one sample to the next, the arrow may turn. How fast it turns is the **frequency** of
  the signal, measured from the centre frequency.

So:

- A signal exactly at the centre frequency is an arrow that does not turn.
- A signal 1000 Hz above the centre turns 1000 times each second in one direction.
- A signal 1000 Hz below the centre turns 1000 times each second in the other direction.

This is why each sample needs two numbers. With two numbers you can tell "above the centre"
from "below the centre". With one number you cannot.

The **sample rate** is the number of samples per second. We write it as `fs`. A recording with
sample rate `fs` shows the frequencies from `-fs/2` to `+fs/2` around the centre.

```python
amplitude = np.abs(iq)      # length of each arrow
phase     = np.angle(iq)    # direction of each arrow
```

## 2. Look at the signal first

Before you calculate anything, make two pictures.

**Picture 1: amplitude over time.** This shows you when something is transmitting.

**Picture 2: a spectrogram.** This shows you which frequencies are in use, and when. To make
it, the computer cuts the recording into short blocks and finds the frequencies in each block.
Some programs call this picture a "waterfall".

```python
import matplotlib.pyplot as plt

plt.specgram(iq, NFFT=1024, Fs=fs, noverlap=512)
plt.xlabel("time (seconds)")
plt.ylabel("frequency from centre (Hz)")
plt.show()
```

A spectrogram has a limit. `NFFT` is the number of samples in each block.

- Long blocks show frequency in fine detail, but blur fast changes in time.
- Short blocks show fast changes in time, but blur frequency.

A block of `N` samples cannot separate two frequencies closer than `fs / N` hertz. It cannot
show an event shorter than `N / fs` seconds. You cannot have both at once.

## 3. Four basic steps

Almost every challenge is some mix of these four steps.

### Step 1: Tune

A signal may sit away from the centre, at some frequency `f0`. To move it to the centre,
multiply the recording by an arrow that turns the opposite way:

```python
n = np.arange(len(iq))
tuned = iq * np.exp(-2j * np.pi * f0 * n / fs)
```

### Step 2: Filter

After tuning, your signal is in the middle, but other signals are still in the recording. A
**low-pass filter** keeps what is near the middle and removes the rest.

```python
from scipy.signal import firwin, lfilter

taps = firwin(257, cutoff_hz, fs=fs)
narrow = lfilter(taps, 1.0, tuned)
```

`cutoff_hz` is how far from the middle you want to keep.

### Step 3: Decimate

After filtering, the signal is narrow, so you have more samples than you need. To
**decimate** by `D` means to keep one sample in every `D`. The new sample rate is `fs / D`.

```python
small = narrow[::D]
```

Always filter before you decimate. If you do not, the signals you wanted to remove will fold
back on top of the one you want.

Doing steps 1, 2 and 3 together is called **channelising**.

### Step 4: Demodulate

To **demodulate** means to get the message back out of the radio signal. How you do this
depends on how the message was put in. The next section explains.

## 4. Ways to put a message on a radio signal

A plain radio signal with no message on it is called a **carrier**. To send a message, the
sender changes the carrier in some way. This is called **modulation**.

| Name     | What the sender changes                                  | How you read it                                         |
|----------|----------------------------------------------------------|---------------------------------------------------------|
| **OOK**  | Switches the carrier on and off                          | Look at the amplitude                                   |
| **FM**   | Moves the carrier's frequency up and down with the sound | Measure the frequency at each moment (see below)        |
| **FSK**  | Jumps the carrier between two frequencies, one per bit value | Measure the frequency, then check if it is high or low |
| **AFSK** | Sends two different sound tones, one per bit value, using FM | Undo the FM, then check which tone is present        |
| **BPSK** | Flips the carrier's phase by half a turn, or does not    | Compare the phase of one symbol with the next           |

### Undoing FM

Remember that frequency is how fast the arrow turns. So to get the frequency, measure the
angle between each sample and the one before it:

```python
freq_hz = np.angle(iq[1:] * np.conj(iq[:-1])) * fs / (2 * np.pi)
```

For a walkie-talkie, `freq_hz` is the sound that was sent. You can save it as a WAV file and
listen to it. You can also look at which tones it contains.

When no radio is transmitting, `freq_hz` is just loud noise. Ignore the parts where the
amplitude is small.

## 5. How walkie-talkies behave

**Push-to-talk.** A walkie-talkie transmits only while its talk button is held down. Pressing
the button is called **keying up**. Releasing it is called keying down. When the radio keys
up, the carrier appears and takes a few thousandths of a second to settle.

**FM voice.** A walkie-talkie sends voice using FM. The carrier moves a few kilohertz up and
down. One channel is 12.5 kHz wide.

**CTCSS (privacy tones).** Many radios add a steady low tone under the voice. It is lower than
speech, so you do not notice it. A receiver set to the same tone turns its speaker on. Other
receivers stay silent. The tone always comes from a standard list of frequencies between
67.0 Hz and 250.3 Hz.

**DTMF (keypad tones).** These are the tones a telephone keypad makes. Each key plays two
tones at the same time: one for its row and one for its column.

|            | 1209 Hz | 1336 Hz | 1477 Hz | 1633 Hz |
|------------|:-------:|:-------:|:-------:|:-------:|
| **697 Hz** |    1    |    2    |    3    |    A    |
| **770 Hz** |    4    |    5    |    6    |    B    |
| **852 Hz** |    7    |    8    |    9    |    C    |
| **941 Hz** |    *    |    0    |    #    |    D    |

## 6. Sending bits and bytes

**Bit rate.** This is how many bits are sent each second. At 1200 bits per second, one bit
lasts 1/1200 of a second. You will also see the word **baud**, which here means the same
thing.

**Serial framing.** The sender and the receiver do not share a clock. So the sender needs a
way to show where each byte begins. The usual way works like this:

1. When nothing is being sent, the line stays at `1`.
2. To begin a byte, the sender sends one `0`. This is the **start bit**.
3. Then it sends the eight bits of the byte, lowest bit first.
4. Then it sends one `1`. This is the **stop bit**.

So each byte takes 10 bits. To decode, look for the moment the line drops from `1` to `0`.
That is the start of a byte. Then read the value in the middle of each of the next nine bits.

**ASCII.** The standard way to store text as bytes. For example, the byte 65 is the letter
`A`.

## 7. Averaging

Noise is random. If you average many samples of noise, the result gets close to zero. A real
signal is not random, so it stays.

The more samples you average, the more clearly the signal stands out from the noise. A signal
that you cannot see in single samples can become obvious after you combine enough of them.

## 8. When you are stuck

- Plot it. Zoom in. Plot it again.
- Check your sample rate. A wrong `fs` is the most common mistake.
- Check that you are looking at one signal and not several on top of each other.
- Try an easy version first. Make a clean test signal yourself and decode that. Then go back
  to the recording.
- Read the challenge page again. Every number on it is there because you need it.
- Look at the hints in the portal.
