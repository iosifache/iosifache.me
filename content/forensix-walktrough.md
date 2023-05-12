---
title: Chrome Forensics with ForensiX
tags:
  - forensics
  - docker
  - walkthrough
date: 2022-11-05
slug: forensix-walktrough
---

# Scenario

Given a dump of an `%APPDATA%` folder from a Windows host, retrieve Chrome usage data.

The above-mentioned folder is taken from the [Digging In The Dump](https://github.com/8061xjl/ctfarchive-sctf-3.0/tree/main/files/forensics/digging-in-the-dump) challenge, part of Sieberrsec CTF 3.0.

# Choosing a Tool

As my primary operating system is Ubuntu, I skipped tools like [BrowsingHistoryView](https://www.nirsoft.net/utils/browsing_history_view.html) and [MiTeC Internet History Browser](https://www.mitec.cz/ihb.html), which are Windows-only.

Searching out on GitHub, I found the bachelors project of [Adam Chmara](https://github.com/ChmaraX), [ForensiX](https://github.com/ChmaraX/forensix). It is "_Google Chrome forensic tool to process, analyze and visualize browsing artifacts_", built on Docker Compose and with a beautiful, web-based user interface.

Another alternative was [`browser-history`](https://github.com/browser-history/browser-history), a Python3 library and CLI tool which supports the most popular browsers.

# Filtering the Artifacts

1. Create a folder to dump the multipart archive: `mkdir data`.
2. Download the challenge files with:

        for i in {1..6} do; wget https://github.com/8061xjl/ctfarchive-sctf-3.0/blob/main/files/forensics/digging-in-the-dump/AppData.zip.00$i\?raw\=true -o data/AppData.zip.part$i; done

3. Recreate the original archive from its parts: `cat data/AppData.zip.part* > data/AppData.zip`.
4. Check the validity of the created archive:

        $ unzip -t ../data/AppData.zip
        Archive:  ../data/AppData.zip
        warning [../data/AppData.zip]:  50331648 extra bytes at beginning or within zipfile
        (attempting to process anyway)
            testing: AppData/                 OK
            testing: AppData/Local/           OK
            testing: AppData/LocalLow/        OK
            [...]
        No errors detected in compressed data of ../data/AppData.zip.

5. Extract the content, namely the `AppData` folder: `unzip data/AppData.zip -d data/AppData`.
6. List the files linked to the default Chrome profile:

        $ ls data/AppData/Local/Google/Chrome/User\ Data/Default
        'Affiliation Database'           Favicons-journal                          'Login Data For Account-journal'               shared_proto_db
        'Affiliation Database-journal'  'Feature Engagement Tracker'               'Login Data-journal'                           Shortcuts
        AutofillStrikeDatabase         'GCM Store'                                 Network                                       Shortcuts-journal
        blob_storage                   'Google Profile.ico'                       'Network Action Predictor'                    'Site Characteristics Database'
        BudgetDatabase                  GPUCache                                  'Network Action Predictor-journal'             Storage
        Cache                           heavy_ad_intervention_opt_out.db           optimization_guide_hint_cache_store          'Sync Data'
        'Code Cache'                     heavy_ad_intervention_opt_out.db-journal   optimization_guide_model_and_features_store  'Top Sites'
        coupon_db                       History                                    Preferences                                  'Top Sites-journal'
        databases                       History-journal                            PreferredApps                                'Trusted Vault'
        data_reduction_proxy_leveldb    IndexedDB                                  QuotaManager                                  VideoDecodeStats
        'Download Service'              'Local Extension Settings'                  QuotaManager-journal                         'Visited Links'
        'Extension Rules'               'Local Storage'                            'Safe Browsing Network'                       'Web Data'
        Extensions                      LOCK                                      'Search Logos'                                'Web Data-journal'
        'Extension Scripts'              LOG                                       'Secure Preferences'
        'Extension State'               'Login Data'                                Sessions
        Favicons                       'Login Data For Account'                   'Session Storage'

# Installing ForensiX

1. Clone ForensiX: `git clone https://github.com/ChmaraX/forensix.git`.
2. Place Chrome's `Default` into ForensiX's volume: `cp -r data/AppData/Local/Google/Chrome/User\ Data/Default/* forensix/data`.
3. Install ForensiX via `cd forensix && ./install.sh`. The process may take several minutes as hundreds of megabytes are downloaded.
4. Start ForensiX: `./startup.sh`.
5. Check the created containers:

        $ docker container ls
        CONTAINER ID   IMAGE                     COMMAND                  CREATED          STATUS          PORTS                                           NAMES
        8c55799727b7   chmarax/forensix:client   "docker-entrypoint.s…"   31 seconds ago   Up 29 seconds   0.0.0.0:3000->3000/tcp, :::3000->3000/tcp       forensix-client
        e972dda0247e   chmarax/forensix:server   "npm start"              31 seconds ago   Up 30 seconds   0.0.0.0:3001->3001/tcp, :::3001->3001/tcp       forensix-server
        20ae98404ddc   mongo:latest              "docker-entrypoint.s…"   32 seconds ago   Up 30 seconds   0.0.0.0:27017->27017/tcp, :::27017->27017/tcp   forensix-mongodb

6. Access the web UI at `http://localhost:3000`.
7. Create an account.
8. Log in with the created account.

# Extracting Information with ForensiX

1. By operating ForensiX, the following information can be extracted:
   - Country: Singapore
   - Chrome version: `96.0.4664.110`
   - Screen resolution: `718x1014`
   - Most used username: `Alex24`
   - Browser activity period: only 24 December 2021
   - Visited websites: Google, Bing
   - Favicons: Google, Bing, other Singaporean websites
   - Stored credentials, in which the password is encrypted and hex-encoded: `Alex24:763130EE90D405CD2F46F8F8026EC964434AEF7FFC39DE825C1700FAA0B50752EF2EFBF5E23C4F688A4F47DB` from a CTF-specific website, `http://challs.sieberrsec.tech:23547/dcfa237943d4fd7e2a514ca54642efaccd2cdbd5003bfb19a1e70737273e1190/`
   - Cached content: stylesheets, scripts, fonts, GIFs.

![Shallow information](/images/forensix-walktrough/main.png)

![History](/images/forensix-walktrough/history.png)

![Cached content](/images/forensix-walktrough/cache.png)

![Favicons](/images/forensix-walktrough/favicons.png)

# Uninstalling ForensiX

1. Uninstall ForensiX: `./teardown.sh`.

---

# References

- [ForensiX repository](https://github.com/ChmaraX/forensix)
- [Chromium Documentation on User Data Directories](https://chromium.googlesource.com/chromium/src/+/master/docs/user_data_dir.md)
