---
title: Fuzzing an Open-Source Project with AFL
summary: Guide for using American Fuzzy Lop to find multiple vulnerabilities into an open-source project
tags:
  - fuzzing
  - open-source
  - afl
  - gdb
  - walkthrough
date: 2022-09-18
slug: open-source-fuzzing
---

# Steps to Reproduce

## Setting Up the Fuzzing Environment

The first step that needs to be completed is the setup of the fuzzing environment. As the manual installation could be a draining process, it can be used an unofficial Docker image (namely [`mykter/afl-training`](https://hub.docker.com/r/mykter/afl-training/dockerfile)) with all the tools already installed. This was primarily used for a workshop in which concepts about the fuzzer American Fuzzy Lop (AFL) are introduced via practical exercises.

1. Install Docker by running the official installation script.

        curl -fsSL https://get.docker.com -o /tmp/get-docker.sh
        sh /tmp/get-docker.sh

2. Pull the image and create a container (in the privileged mode, with the `2222` port exposed and a password set as environment variable).

        docker run \
        --privileged \
        --publish 2222:2222 \
        --env PASSMETHOD=env --env PASS=thispasscantbefuzzed \
        ghcr.io/mykter/fuzz-training

3. Log in into the created container, by using the `fuzzer` account with the set password and the `2222` port.

        ssh fuzzer@localhost -p 2222

## Finding and Compiling (with Instrumentation) an Open-Source Project

In this guide, due to the different build processes implemented by each project, a specific open-source one was chosen: [HiColor](https://github.com/dbohdan/hicolor). It is a quite popular (judging by the stars on GitHub) program for converting PNG images into 15- or 16-bit RBG color ones.

1. Clone the project into the home of the `fuzzer` user (the default directory after the above login).

        git clone https://github.com/dbohdan/hicolor
        cd ~/hicolor

2. AFL could benefit from the fact that the source code is available, for performing a fuzzing in the whitebox approach. For achieving this, the binary needs to incorporate instrumentation artifacts, so the compilation needs to be a little altered. Optionally, the Makefile could be edited by adding the `-g` option to the `CFLAG` variables to include debug symbols into the executable.

        CC=afl-clang CXX=afl-clang++ make

## Fuzzing

As the fuzzer would be helped by valid inputs from which it could later mutate for generating new inputs, sample PNG images could be offered to AFL.

1. Create a directory for storing sample images.

        mkdir --parents ~/sample_images/png
        cd ~/samples_images/png

2. Manually download 5 PNG images in the newly created directory.
3. Transform each image into its `.hic` (HiColor format) correspondent.

        mkdir ~/sample_images/hic
        find . \
        -name "*.png" \
        -exec ~/hicolor encode {} ~/sample_images/hic/{}.hic \;

4. Solve the AFL errors (only if it is required).

        export AFL_I_DONT_CARE_ABOUT_MISSING_CRASHES=1
        echo performance \
        | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

4. Start the fuzzing for the encoding functionality

        cd ~/hicolor
        afl-fuzz \
        -m none \
        -i ~/sample_images/png \
        -o encode_results \
        ./hicolor encode \
        @@ /dev/null

5. Start the fuzzing for the decoding functionality

        afl-fuzz \
        -m none \
        -i ~/sample_images/hic \
        -o decode_results \
        ./hicolor decode \
        @@ /dev/null

1. Start the fuzzing for the custom format parsing functionality

        afl-fuzz \
        -m none \
        -i ~/sample_images/hic \
        -o info_results \
        ./hicolor info \
        @@ /dev/null

## Analyzing the Results

After running the last 3 commands, the following outputs are generated:

<details>

<summary>Encode Functionality Fuzzing</summary>

```
               american fuzzy lop ++3.00c (default) [fast] {0}
┌─ process timing ────────────────────────────────────┬─ overall results ────┐
│        run time : 0 days, 0 hrs, 6 min, 14 sec      │  cycles done : 0     │
│   last new path : 0 days, 0 hrs, 1 min, 25 sec      │  total paths : 1024  │
│ last uniq crash : 0 days, 0 hrs, 4 min, 41 sec      │ uniq crashes : 8     │
│  last uniq hang : none seen yet                     │   uniq hangs : 0     │
├─ cycle progress ───────────────────┬─ map coverage ─┴──────────────────────┤
│  now processing : 1000.8 (97.7%)   │    map density : 0.05% / 0.11%        │
│ paths timed out : 143 (13.96%)     │ count coverage : 1.47 bits/tuple      │
├─ stage progress ───────────────────┼─ findings in depth ───────────────────┤
│  now trying : splice 1             │ favored paths : 17 (1.66%)            │
│ stage execs : 55/73 (75.34%)       │  new edges on : 18 (1.76%)            │
│ total execs : 479k                 │ total crashes : 8 (8 unique)          │
│  exec speed : 1327/sec             │  total tmouts : 1688 (8 unique)       │
├─ fuzzing strategy yields ──────────┴───────────────┬─ path geometry ───────┤
│   bit flips : n/a, n/a, n/a                        │    levels : 7         │
│  byte flips : n/a, n/a, n/a                        │   pending : 4.29G     │
│ arithmetics : n/a, n/a, n/a                        │  pend fav : 0         │
│  known ints : n/a, n/a, n/a                        │ own finds : 24        │
│  dictionary : n/a, n/a, n/a                        │  imported : 0         │
│havoc/splice : 32/224k, 0/236k                      │ stability : 100.00%   │
│   py/custom : 0/0, 0/0                             ├───────────────────────┘
│        trim : 99.54%/11.9k, n/a                    │          [cpu000: 62%]
└────────────────────────────────────────────────────┘
```

</details>

<details>

<summary>Decode Functionality Fuzzing</summary>

```
               american fuzzy lop ++3.00c (default) [fast] {0}
┌─ process timing ────────────────────────────────────┬─ overall results ────┐
│        run time : 0 days, 0 hrs, 2 min, 43 sec      │  cycles done : 0     │
│   last new path : 0 days, 0 hrs, 0 min, 3 sec       │  total paths : 1160  │
│ last uniq crash : none seen yet                     │ uniq crashes : 0     │
│  last uniq hang : none seen yet                     │   uniq hangs : 0     │
├─ cycle progress ───────────────────┬─ map coverage ─┴──────────────────────┤
│  now processing : 1090.1 (94.0%)   │    map density : 0.43% / 0.51%        │
│ paths timed out : 1 (0.09%)        │ count coverage : 5.56 bits/tuple      │
├─ stage progress ───────────────────┼─ findings in depth ───────────────────┤
│  now trying : trim 1024/1024       │ favored paths : 35 (3.02%)            │
│ stage execs : 107/137 (78.10%)     │  new edges on : 36 (3.10%)            │
│ total execs : 26.6k                │ total crashes : 0 (0 unique)          │
│  exec speed : 679.2/sec            │  total tmouts : 63 (1 unique)         │
├─ fuzzing strategy yields ──────────┴───────────────┬─ path geometry ───────┤
│   bit flips : n/a, n/a, n/a                        │    levels : 3         │
│  byte flips : n/a, n/a, n/a                        │   pending : 722       │
│ arithmetics : n/a, n/a, n/a                        │  pend fav : 29        │
│  known ints : n/a, n/a, n/a                        │ own finds : 159       │
│  dictionary : n/a, n/a, n/a                        │  imported : 0         │
│havoc/splice : 120/7524, 39/3989                    │ stability : 100.00%   │
│   py/custom : 0/0, 0/0                             ├───────────────────────┘
│        trim : 76.39%/5762, n/a                     │          [cpu000:112%]
└────────────────────────────────────────────────────┘
```

</details>

<details>

<summary>Custom Format Parsing Functionality Fuzzing</summary>

```
              american fuzzy lop ++3.00c (default) [fast] {0}
┌─ process timing ────────────────────────────────────┬─ overall results ────┐
│        run time : 0 days, 0 hrs, 2 min, 24 sec      │  cycles done : 1     │
│   last new path : none yet (odd, check syntax!)     │  total paths : 1001  │
│ last uniq crash : none seen yet                     │ uniq crashes : 0     │
│  last uniq hang : none seen yet                     │   uniq hangs : 0     │
├─ cycle progress ───────────────────┬─ map coverage ─┴──────────────────────┤
│  now processing : 0.1160 (0.0%)    │    map density : 0.01% / 0.01%        │
│ paths timed out : 0 (0.00%)        │ count coverage : 1.00 bits/tuple      │
├─ stage progress ───────────────────┼─ findings in depth ───────────────────┤
│  now trying : splice 1             │ favored paths : 1 (0.10%)             │
│ stage execs : 16/32 (50.00%)       │  new edges on : 1 (0.10%)             │
│ total execs : 376k                 │ total crashes : 0 (0 unique)          │
│  exec speed : 2193/sec             │  total tmouts : 0 (0 unique)          │
├─ fuzzing strategy yields ──────────┴───────────────┬─ path geometry ───────┤
│   bit flips : n/a, n/a, n/a                        │    levels : 1         │
│  byte flips : n/a, n/a, n/a                        │   pending : 0         │
│ arithmetics : n/a, n/a, n/a                        │  pend fav : 0         │
│  known ints : n/a, n/a, n/a                        │ own finds : 0         │
│  dictionary : n/a, n/a, n/a                        │  imported : 0         │
│havoc/splice : 0/296k, 0/71.8k                      │ stability : 100.00%   │
│   py/custom : 0/0, 0/0                             ├───────────────────────┘
│        trim : 100.00%/28, n/a                      │          [cpu000: 87%]
└────────────────────────────────────────────────────┘
```

</details>

From this information, a coarse conclusion can be formed: only the encoding functionality has a poor implementation due to the multiple unique crashes that AFL could find. For the rest of the functionalities, namely the decoding and the custom format parsing, the fuzzer does not find any vulnerability.

## Analysis of One Crash

The first generated crash was chosen and further analyzed with dynamic techniques, namely debugging. `gdb` was instructed to automatically start the program for encoding, with the file that generated the first crash. It needs to be mentioned that the names of the dumped files could vary depending on multiple factors (order of finding crashes, time, current operation).

```bash
gdb \
  --ex run
  --args ./hicolor encode encode_results/default/crashes/id:000000,sig:11,src:001013,time:93879,op:havoc,rep:2 encoded.hic
```

The line on which the program generates a `SIGSERV` is the one highlighted below. It tries (and fails) to dereference the `rgb_img` pointer, which is `NULL`.

```c
|   29   hicolor_rgb* cp_to_rgb(const cp_image_t img)                                │
│   30   {                                                                           │
│   31       hicolor_rgb* rgb_img = malloc(sizeof(hicolor_rgb) * img.w * img.h);     │
│   32                                                                               │
│   33       for (uint32_t i = 0; i < (uint32_t) img.w * (uint32_t) img.h; i++) {    │
│  >34           rgb_img[i].r = img.pix[i].r;                                        │
│   35           rgb_img[i].g = img.pix[i].g;                                        │
│   36           rgb_img[i].b = img.pix[i].b;                                        │
│   37       }                                                                       │
│   38                                                                               │
│   39       return rgb_img;                                                         │
│   40   }
```

By inspecting the parameters used in the `malloc` call (with the command `p img`), huge values can be observed. This means that the product on the line 31 results in 34582635452664. This value is in fact not truncated (it can be stored into an `unsigned int`, on a 64-bit architecture) and the `malloc` is instructed to allocate 31 terabytes on the stack, it fails and returns a `NULL` pointer.

```
{
w = 0xf3ff,
h = 0xb000258,
pix = 0x0
}
```

The PNG image that generated the crash can be analyzed with `file`, which only parses the header of the file, or with `identify`, a utility from the ImageMagick suite, which investigate the PNG file more deeply.

```bash
file encode_results/default/crashes/id:000000,sig:11,src:001013,time:93879,op:havoc,rep:2
encode_results/default/crashes/id:000000,sig:11,src:001013,time:93879,op:havoc,rep:2: PNG image data, 62463 x 184549976, 8-bit/color RGB, non-interlaced
```

```bash
identify ../crashes/id:000007,sig:11,src:001013,time:93879,op:havoc,rep:2
identify-im6.q16: insufficient image data in file `../crashes/id:000007,sig:11,src:001013,time:93879,op:havoc,rep:2' @ error/png.c/ReadPNGImage/4098.
```

By correlating this information with the [source code](https://github.com/dbohdan/hicolor/blob/master/cli.c) of the analyzed program, the root cause can be reached. AFL, in its input generation phase, modified the sizes (height and width) stored in the PNG header with the large sizes seen in the `file` command output. The project uses an open-source header-only C library (namely `cute_png.h`) to loads the PNG files.

Further, both the library and `hicolor` does not check if the image is valid (like `identify`, which detects that the declared pixels from the header are not stored in the data section too) and the image is loaded as it is. When the image needs to be converted to the custom file format, the `malloc` fails and the programs tries to dereference a `NULL` pointer, which raises a `SIGSERV`.

# Last Step

The bug discovered in this guide was reported by creating a [new issue](https://github.com/dbohdan/hicolor/issues/2) on the repository.

---

# References

- [AFL Documentation](https://afl-1.readthedocs.io/en/latest/index.html)
- ["Fuzzing with AFL" Workshop](https://github.com/mykter/afl-training)
