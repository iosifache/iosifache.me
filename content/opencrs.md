---
title: A Novel Open Source Cyber Reasoning System
tags:
  - binary-analysis
  - dataset
  - attack-surface-approaximation
  - vulnerability-discovery
  - automatic-exploit-generation
  - fuzzing
  - dynamic-binary-instrumentation
  - afl++
  - qbdi
  - latex
  - open-source
  - status-update
date: 2023-07-30
slug: opencrs
---

This month marked the end of my two-year master's degree at the University POLITECHNICA of Bucharest's Advanced Cybersecurity speciality. In addition to the coursework, these years involved research.

The work began with a suggestion from my coordinator, Adrian-Răzvan Deaconescu. He brought up a term that I was unfamiliar with: cyber reasoning systems. Following some additional research, I discovered that DARPA held a competition called Cyber Grand Challenge in 2016, which was a CTF-style competition with automated players represented by cyber reasoning systems. The latter are automated sets of software components meant to automatically find, exploit, and patch executable vulnerabilities.

Despite the passing of seven years, the open source CRS landscape has remained unchanged. This observation was the source of the story's intrigue and the impetus for a joint endeavour with Claudiu Ghenea to create an open source cyber reasoning system, OpenCRS.

Fast forward to today, and we've completed the majority of the modules that comprise a CRS. Personally, I contributed to the development of several modules that are now housed in the [OpenCRS organization on GitHub](https://github.com/CyberReasoningSystem):
- A dataset ([module](https://github.com/CyberReasoningSystem/dataset) and [resulting dataset](https://github.com/CyberReasoningSystem/opencrs_dataset)) containing public test suites of vulnerable ELF programs;
- A [module](https://github.com/CyberReasoningSystem/attack_surface_approximation) that uses static analysis with Ghidra and handcrafted arguments fuzzing with QBDI as a dynamic binary instrumentation engine to estimate the attack surface of an executable;
- A vulnerability discovery [module](https://github.com/CyberReasoningSystem/vulnerability_detection) that fuzzes using AFL++; and
- A [module](https://github.com/CyberReasoningSystem/automatic_exploit_generation) focusing on automated exploitation, based on a [fork](https://github.com/CyberReasoningSystem/zeratool_lib) intended to improve an existing open source project.

Aside from that, my thesis, "OpenCRS: Attack Surface Approximation, Vulnerabilities Discovery, and Automatic Exploitation of Binaries", is [available on GitHub](https://github.com/iosifache/MastersThesis). Because there were no updated templates, I generated [several](https://github.com/cs-pub-ro/templates/pull/1) in the hopes that they will be merged and used by future generations in the department.

OpenCRS is not yet fully functional because there is no orchestration module to coordinate all of the previously created modules. However, the project will be continued by future generations of students, and I am convinced that it will be ready for production in the near future.
