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

1. Download the repository: `git clone https://github.com/returntocorp/semgrep`
2. Set up the development environment: `make dev-setup`
3. Install `opam`
	
	```
	apt-get install opam
	opam init
	eval $(opam config env)
	```

4. Build: `make`
5. Install `pipenv`: `sudo apt install pipenv`
6. Downgrade `ruamel.yaml==0.16.0`: `pip install 'ruamel.yaml==0.16.0'`
7. Install Semgrep's CLI
	
	```
	cd cli
	python setup.py install
	```