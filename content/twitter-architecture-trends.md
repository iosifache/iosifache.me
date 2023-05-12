---
title: Trends in Twitter’s Architecture
summary: Study case about trends in Twitter’s architecture, as observed from public information
tags:
  - architecture
  - startup
  - twitter
  - study-case
date: 2023-02-05
slug: twitter-architecture-trends
---

# Twitter In a Nutshell

Twitter is an **online service** that uses 280-character messages (named tweets) for two primary roles:

- **Social media**: Users can share their content and consume the one created by others.
- **Social networking**: Users can expand their network by connecting with others who have similar interests.

Jack Dorsey, Noah Glass, Biz Stone, and Evan Williams created Twitter in March 2006. The following year, they launched it. Twitter grew from 50 million users in 2010 to 300 million in 2015. The usage slowly increased to 400 million in 2022. In the same year, Elon Musk bought all shares (TWTR, listed on New York Stock Exchange), and Twitter became a privately-held company.

![Monthy Active Users](/images/twitter-architecture-trends/mau.webp)

# Modus Operandi

We can consider Twitter a **consumption platform**. In 2013, Raffi Krikorian, the VP of Engineering, stated that there were 300.000 queries and only 6.000 writes per second.

Some statistics from 2022 support consumption even more. The website has 400 million active users and 60 billion tweets per month. This means that each user has 15 tweets per month on average. In addition, users spend the remaining 3 hours per month (6 minutes per day) reading other people's tweets.

This characteristic is relevant for architectural reasons. Engineering teams **need to optimize the read path of the service-oriented architecture**. The decision comes with a possible performance compromise on the writing path.

The user relationship can be broadly divided into the following categories:

|  | Push, i.e. server-initiated | Pull, i.e. user-initiated |
| --- | --- | --- |
| Targeted, i.e. detected by algorithms to be relevant for a user | A stream of tweets pushed to a user. It helps to maintain the timeline experience after the initial load. | Data that Twitter consider to be relevant for you. Like timeline API. |
| Queried, i.e. specifically requested by the user | A stream of tweets pushed to a user, from tracked terms or followed accounts. | A query for specific tweets (for example, containing a specific term). Like Search API. |

# Architectural Evolution

We can create the following list of architectural observations by analyzing many resources from the Internet (linked in the last section). Their goal is not to provide a theoretical model for why Twitter engineers made those decisions. We can only **deduce the first principles** and **back them up with concrete examples**.

## Making Product Features More Important Than Architectural Perfection

Many engineers declared that the source code of Twitter is in a completely **unstable, but functioning state**. Among them are the ones fired after the [recent layoff](https://abcnews.go.com/Business/twitter-sends-email-employees-announcing-layoffs-friday/story?id=92635005). This state ensures the functioning of the application, but they accumulated too much technical debt.

It is not sure if this modus operandi continued after 2013. In his presentation at InfoQ, Raffi Krikorian confirmed the existence of a **dedicated architecture team**. Its purposes were designing a holistic architecture and maintaining a list of technical debts, which engineers wanted to fix.

These two examples depict a common theme in companies with explosive growth. Twitter prioritizes product features over architectural perfection. The decision may lead to scars in the form of debt, but the company’s purpose (to keep the users involved and satisfied) is accomplished.

## Migrating from Monoliths to SOA

In the same presentation from 2013, Raffi presented a diagram with the architecture. The **monolithic service**, named Monorail, covered three layers: routing, presentation, and logic. Its roots can be traced back to the old web stack that they used for their initial launch. He stated that its team's goal is to divide the service into smaller, isolated services. They also believed that this change would improve speed, reliability, and development speed.

![Monorail Architecture](/images/twitter-architecture-trends/monorail.jpg)

A 2013 presentation provides additional evidence of the continuous architectural progress. Jeremy Cloud, a team leader at Tweet Service, was the speaker.

Elon Musk tweeted a picture of two combined architectures on November 19, 2022: the current and the desired one (with dashed lines). We can see that the Monorail service has vanished, replaced by **smaller and more specialized services**.

![Elon's Architecture](/images/twitter-architecture-trends/elon-arch.jpg)

## Choosing the Best Technology for Their Needs

Besides its size, the **Ruby on Rails** monolith suffered from another disadvantage. The programming language is not optimized for concurrency. The latter is mandatory for scaling the service under the growth in usage.

In 2013, Jeremy Cloud stated that the presentation and logic layers contained JVM services running **Scala**. It indicates that engineers are not afraid to abandon one technology in favor of another to achieve greater scalability.

Another observed change reinforces the point. Before 2010, Twitter only used **MySQL** to store relevant data, such as user information and timelines. In 2010, they used an in-house framework called Gizzard to replicate MySQL databases across multiple servers. However, standard structured databases no longer met their requirements after that year, so they incorporated **advanced storage technologies** such as:

- Caching via Redis;
- Searching via Lucine;
- Data clustering via Hadoop; and
- Blob (e.g. users' images) databases via Blobstore, an in-house software.

## Obtaining  Physical Layer Independence

Before 2010, Twitter used a **third-party hosting provider**'s infrastructure. They decided to become more independent on the physical layer, so the first design of the on-premise network was born in the same year. In 2015, Twitter had **points of presence** on five continents and **data centers** housing hundreds of thousands of servers.

Partly Cloud was announced in 2018 as a collaboration with **Google Cloud**. It is a hybrid infrastructure for hosting Hadoop clusters and some components of the data platform, which ensured analytical capabilities.

![Partly Cloud](/images/twitter-architecture-trends/gcp.png)

## Making Changes Gradually

Developers adapted an **Agile approach** by deploying often and incrementally. Deploys consisted in:

1. Making small changes;
2. Verifying them in production with small batches of users;
3. Making adjustments in case of malfunctioning; and
4. Repeating.

Jeremy Cloud detailed other resilience techniques, such as a **dark mode** for each feature. It consists of the ability to disable the feature in critical conditions (e.g. service failure).

## Relying on Third-Parties for Specialized Software

Twitter builds a lot of in-house software. Some of it is publicly available on [their GitHub organization](https://github.com/twitter). However, there are times when engineers do not need to devote time to a specific problem. This is not because they cannot build the required software, but a lack of fit between the technical issues and the company's revenue streams.

An example is again the migration of the data platform to **Google Cloud**. GCP already has mature tools for data analysis and machine learning in its software-as-a-service suite:

- [BigQuery](https://cloud.google.com/bigquery/), an enterprise data warehouse with a SQL engine; and
- [Looker Studio](https://cloud.google.com/looker-studio) (known before December 2022 as Data Studio), a big data visualization tool.

2021 was the year of another migration to third-party software. Before, Twitter used an in-house solution, named Logles. The main issue was performance-related: only 10% of the submitted logs ended up being stored on disk, the rest being dropped due to rate limits.

They successfully migrated to **Splunk Enterprise**. The logging architecture consisted in:

- Host forwarders, installed on each server; and
- Rsyslog ones, that received logging messages from network equipment.

The changes offered them a 400% increase in the log processing power, better configurability, a robust API, and new advanced features (e.g. scheduled searches).

# Future Changes

It is unclear what will happen with Twitter’s architecture in the following years. The only thing that we, as outsiders, can do is to watch the last months' evolution and to (try to) predict the future.

After Elon’s arrival, Twitter added **many features**, the most notable being Twitter Blue, long-form tweets, and an edit feature for tweets. Some events contributed to altering the reputation of the platform:

- **[Outage** produced by changes in the backend architecture;](https://techcrunch.com/2022/12/28/twitter-down-outage/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAADFkh-uz1saLakfJaLIirvfw1Pgpes__g-AdGsII8SK4Hlp-E57iI2HB_1G7tXDszyQ80k81RNLohhlKa0LwI8oLb0jws0n3ro5WinMfTxRh0X0cA11BLvaxIS1ewvu4i2N_XN4mO5XPr1xUs9AaXNF01j-eBo2kqZI0MvmFUpoZ) and
- **[Information leaks**, where millions of users’ emails were stolen by black-hat hackers](https://www.reuters.com/technology/twitter-hacked-200-million-user-email-addresses-leaked-researcher-says-2023-01-05/).

But to orient the discussion to the future, an opinion to consider is Dave Troy’s. He states that Elon plan is to slow down the development of the current technology and to free the bird from the closed-source cage.

<a href="https://twitter.com/davetroy/status/1586166535592509440">
  <blockquote>
  🐦 Elon and Jack will work together to shut down the existing Twitter tech stack and move it to Bluesky. Anyone paying attention would know this. That’s why he’s freezing development on the existing platform. It will take a little time, but this is what they’re up to. Watch. - @davetroy
  </blockquote>
</a>

In this way, Twitter will presumably use Bluesky’s **The AT Protocol**, an open and decentralized standard for social media. Jack Dorsey announced Bluesky in 2019. Despite the 13 million dollar investment to continue its research, it is declared as independent of Twitter.

<a href="https://twitter.com/jack/status/1375126834958884865?s=20&t=5RjikqZJLI8JsERHdeNlSg">
  <blockquote>
  🐦 A decentralized open-source protocol for social media is our vision and work for the long term. We continue the cycle mentioned earlier of constantly improving our approach to content moderation in the short term. I hope our discussion today will focus on more enduring solutions. - @jack
  </blockquote>
</a>

<a href="https://twitter.com/jack/status/1518772756069773313?s=20&t=yE1fhXr-uDp9lON5eTfGag">
  <blockquote>
  🐦 In principle, I don’t believe anyone should own or run Twitter. It wants to be a public good at a protocol level, not a company. Solving for the problem of it being a company however, Elon is the singular solution I trust. I trust his mission to extend the light of consciousness. - @jack
  </blockquote>
</a>

# Conclusions

Deducing details about a private company's architecture can be fraught with assumptions. You can not tell whether the facts are black and white, but you can find evidence that things are one way or another.

Regarding Twitter, the precise architecture is still unknown, but we can now make an educated guess based on the information presented. In any case, the achieved scale, and the architectural principles used at the time are impressive.

---

# References

- 23 Oct 2012: [Real-Time Delivery Architecture at Twitter](https://www.infoq.com/presentations/Real-Time-Delivery-Twitter)
- 03 Jul 2013: [Decomposing Twitter: Adventures in Service-Oriented Architecture](https://www.infoq.com/presentations/twitter-soa/)
- 08 Jul 2013: [The Architecture Twitter Uses to Deal with 150M Active Users, 300K QPS, a 22 MB/S Firehose, and Send Tweets in Under 5 Seconds](http://highscalability.com/blog/2013/7/8/the-architecture-twitter-uses-to-deal-with-150m-active-users.html)
- 19 Jan 2017: [The Infrastructure Behind Twitter: Scale](https://blog.twitter.com/engineering/en_us/topics/infrastructure/2017/the-infrastructure-behind-twitter-scale)
- 3 May 2018: [A new collaboration with Google Cloud](https://blog.twitter.com/engineering/en_us/topics/infrastructure/2018/a-new-collaboration-with-google-cloud)
- 07 Apr 2019: [Twitter's GCP Architecture for Its Petabyte-Scale Data Storage in GCS](https://www.youtube.com/watch?v=rBNFwdVDlyo)
- 13 Aug 2021: [Logging at Twitter: Updated](https://blog.twitter.com/engineering/en_us/topics/infrastructure/2021/logging-at-twitter-updated)
- 16 Mar 2022: [33 Twitter Stats That Matter to Marketers in 2023](https://blog.hootsuite.com/twitter-statistics/)
- 08 Oct 2022: [How Twitter maximizes performance with BigQuery](https://www.youtube.com/watch?v=Pym8Evbf7Ak)
- 31 Oct 2022: [What is Bluesky, the potential Twitter alternative being tested by former CEO Jack Dorsey?](https://news.yahoo.com/bluesky-potential-twitter-alternative-being-111738532.html)
- 19 Nov 2022: [Twitter Architecture Explained](https://miro.com/app/board/uXjVPBnTJmM=/)
- 27 Nov 2022: [Leaked Twitter Architecture? Reaction and Analysis](https://www.youtube.com/watch?v=sxtqbUQqoNc)