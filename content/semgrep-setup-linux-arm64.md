---
title: Building Semgrep for Linux on arm64
tags:
  - semgrep
  - linux
  - arm64
  - walkthrough
date: 2023-06-09
slug: semgrep-setup-linux-arm64
---

> As per [PR #8243](https://github.com/returntocorp/semgrep/pull/8243), it is now possible to just `pip install semgrep`.

1. Download the repository: `git clone https://github.com/returntocorp/semgrep`
2. Set up the development environment: `make dev-setup`
3. Install `opam`: `apt-get install opam`
4. Initialise `opam`: `opam init && eval $(opam config env)`
5. Build: `make`
6. Install `pipenv`: `sudo apt install pipenv`
7. Downgrade `ruamel.yaml==0.16.0`: `pip install 'ruamel.yaml==0.16.0'`
8. Install the Semgrep CLI: `cd cli && python setup.py install`
