---
title: The Open Source Fortress
tags:
  - threat-modelling
  - secret-scanning
  - dependency-scanning
  - linting
  - code-querying
  - fuzzing
  - symbolic-execution
  - owasp-threat-tragon
  - gitleaks
  - osv-scanner
  - flawfinder
  - semgrep
  - open-source
  - defcamp
  - ubuntu-summit
  - status-update
date: 2023-12-18
slug: ossfortress
---

Multiple posts on social media contributed to the creation of [The Open Source Fortress](https://ossfortress.io), a workshop that explains what open source tools are available for discovering vulnerabilities in codebases and how to use them.

The workshop employs a customised, purposely insecure Python and C codebase to demonstrate the use of different techniques and tools:

- Threat modelling with OWASP Threat Dragon;
- Secret scanning with Gitleaks;
- Dependency scanning with Google Open Source Security Team's OSV-Scanner;
- Linting with Bandit and flawfinder;
- Code querying with Semgrep;
- Fuzzing with AFL++; and
- Symbolic execution with KLEE.

Sounds appealing? You can begin by reading more about the workshop on [its home page](https://ossfortress.io), then complete the tasks, making sure to verify [the accompanying checklist](https://ossfortress.io/checklist) or [cheatsheet with vulnerability detection commands](https://ossfortress.io/cheatsheet).

What if the workshop misses covering an excellent tool you're using to uncover flaws in your codebase? Both the workshop and the goat-like application are open sourced on [GitHub](https://github.com/iosifache/oss_fortress). You can spend a few seconds opening an issue with the details of this tool, or a dozen minutes writing a guide for it. The makers of that tool will be pleased to learn that you took the time to publicise their work!

Furthermore, the community became aware of this work because of two conferences.

[Ubuntu Summit](https://events.canonical.com/event/31/), held this year in Latvia's capital, provided an ideal setting for the workshop's debut: a group of open source, Linux, and Ubuntu enthusiasts learned about the information included in the workshop and worked on the proposed tasks.

The other conference was Bucharest's [DefCamp](https://def.camp/), where I gave [a 30-minute talk](https://ossfortress.io/defcamp) about vulnerability detection concepts and received feedback. The potential of DefCamp to bring together the Romanian community in the same location, in addition to the participants from other countries, was the icing on the cake. It was fantastic to talk with old friends, folks I had only communicated with online, and interesting people I met at this year's conference.
