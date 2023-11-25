---
title: Setting up a header-based automatic labeller for Gmail
summary: A guide for setting up a header-based automatic labeller for Gmail
tags:
  - productivity
  - email
date: 2023-11-25
slug: header-based-filter-gmail
---

The purpose of this guide is to set up a new hourly-executed App Script for:

1. Iterating through all emails in your Inbox; and
2. Archive and label each thread that has at least one email with a custom header.

# Requirements

- A label in Gmail, that you want to attach to this script

# Setup

## I. Creating a new App Script

1. Access the [App Script dashboard](https://script.google.com/home).
2. Press the "New project" button on the left.
3. Click the name of the project, and set it to "AutoLabeller".
4. Paste the below code snippet:
5. Change the configuration of the script:
    - `SEARCHED_HEADER`: SMTP header to be searched. For example, `X-ACME-Shared-Email: true`; and
    - `LABEL`: Gmail label to be attached to the emails. For example, the nested label `shared-inboxes/acme`.
6. Add a new service, choose Gmail API, and click "Add".

```js
const MAX_AGE = "1h"
const SEARCHED_HEADER = ""
const LABEL = ""

function processInbox() {
	var label = GmailApp.getUserLabelByName(LABEL)
	var threads = GmailApp.search("label:inbox newer_than:" + MAX_AGE)

	for (var i = 0; i < threads.length; i++) {
		var thread = threads[i]

		if (hasHeader(thread)){
			thread.addLabel(label)
			thread.moveToArchive()

			console.log("Detected email to label, with ID " + thread.getId())
		}
	}
}

function hasHeader(thread) {
	var messages = thread.getMessages()

	for (var j = 0; j < messages.length; j++) {
		var message = messages[j]

		var body = message.getRawContent()
		if (body.indexOf(SEARCHED_HEADER) > -1) {
			return true
		}
	}

	return false
}
```

## II. Creating a Trigger

1. Select the clock icon from the left menu.
2. Press the "Add Trigger" button.
3. Choose the following details:
    - Function: `processInbox`;
    - Time-based trigger: "Hour timer"; and
    - Interval: "Every hour".
4. Save the timer.

## III. Deploying the Script

1. Press the "Deploy" button from the top menu, and choose "New Deployment".
2. Choose the "Web app" type, and change the description to "Script for labelling email by inspecting the headers".
3. Press the "Deploy" button.
