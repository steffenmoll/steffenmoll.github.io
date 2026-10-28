---
title: "Where a dataset naturally fits"
date: 2026-10-27
tags: [data platform, data governance, ai]
---

*This is the fourth post on data platforms. Read <a class="internal-link" href="/governance-by-obscurity">part 3</a> if you haven't already.*

**You need a map of the terrain, and you need a way for people and agents to navigate it.** This post is about drawing the map, because you can't give anyone directions across ground nobody has surveyed.

A usable map has four axes, though only three of them grade anything.
- **Reach.** Who the data is for. One team, a business domain (eg. equities, fixed income, real assets in asset management), or the whole firm.
- **Category.** What the data is about, so related things sit together. This could be the difference of reference, operational, derived/analytical and alternative data. This one doesn't grade anything, it just files the dataset for search. Leave it out and tier and reach still tell you whether to trust a dataset, but not what it is or how to find it.
- **Expected quality.** What somebody has promised about the dataset, graded `tier A` to `tier C`.
- **Monitored quality.** What the evidence shows: uptime, freshness, failing tests, history range, how many people query it. And **metadata coverage**, at both object and column level, which is the one most platforms skip and the one an agent leans on hardest when it picks a table. The tier is a claim, and this is what tests it.

None of this is new territory. The Open Data Contract Standard[^1] defines schema, ownership and measured quality checks in machine-readable form, and Apache Ossie[^2] does the same for semantic models shared between BI tools. Neither one defines how broadly a dataset is meant to be relied on, or groups it by what it's about: reach and category are left to whoever adopts the standard. Medallion's[^3] bronze, silver, gold comes closer to a tier, but it's answering a different question, how refined data is rather than the business quality of the data itself, and in practice those two concerns don't sit on the same scale.

The three tiers are worth spelling out before the grid, since every cell in it carries one.
- `tier A` - **Certified**: someone has signed something. Data contract, named owner, defined coverage, and an SLA that gets honoured at three in the morning.
- `tier B` - **Supported**: someone is watching. Tests run and monitoring exists, but nobody has promised it will be there on Monday.
- `tier C` - **Best effort**: nothing has been promised at all. Sandbox, ad hoc, use at your own risk.

Two axes carry most of the weight once you put them on a grid. Expected quality down the side, reach across the top, and every dataset you own lands in exactly one cell.

| | Org-wide | Business domain | One team |
|---|---|---|---|
| `tier A` | **official positions, firm reporting** | domain benchmarks, risk inputs | rare, and usually over-built |
| `tier B` | widely used, never promised | **most modelled marts** | a team's monitored working set |
| `tier C` | ungoverned, and everyone is using it | exploratory work on a strategy | **scratch models, ad hoc** |

Most data should sit on the diagonal, and most of it does. A scratch model one analyst uses doesn't need an SLA. The official position data the whole firm reports on can't be a sandbox table. Expected quality rises with reach because the cost of being wrong rises with reach, and that correlation is what makes the map readable at a glance.

**The interesting datasets are the ones off the diagonal.**

Towards the top right you have over-built. A team-local dataset with a data contract and a pager rotation is governance spent where very little was at risk. That's wasteful rather than dangerous, and it usually means somebody got enthusiastic.

Towards the bottom left is where the damage lives. A dataset the whole firm leans on, sitting at `tier C`, with nobody's name on it and no monitoring. Part 3 called this governance by obscurity. It survives because nobody has gone looking, not because it works.

A few rules keep the map honest. The declared cadence is the cheapest of them: a dataset that says "expected daily" and last updated in March needs no SLA and no governance forum to tell you something is wrong. Monitoring isn't optional above `tier C` either, because with no instrumentation there's no evidence, so an uninstrumented dataset can't hold `tier B` or `tier A` however well built it is. New datasets start at `tier C`, which is accurate. Nobody has promised anything about them yet.

The owning team proposes where its dataset sits. Only `tier A` needs sign-off, from a data ops team, because it's the only tier that comes with a promise somebody has to answer for. When the monitoring contradicts the claim for longer than the dataset's own update cadence, the dataset gets proposed for a move, in either direction.

The bottom left corner isn't hypothetical.

Somewhere I worked before, there was a dataset the business treated as critical. It fed reporting that people made decisions on. It had been deprecated some time earlier and had stopped updating, and it still looked completely fine, because stale data loads perfectly well and the row count doesn't drop when nothing new arrives. Nobody had ever written down what the dataset was for, or how often it should refresh.

> Nobody had written down what it promised, so there was nothing for reality to contradict.

Drawing the map is what surfaced it. No new tool was involved. Somebody had to sit down and write what the dataset claimed, and then the claim and the evidence disagreed immediately.

One more reason to bother. A map like this does very little as a wiki page, because the people who would benefit from it don't read wikis. Read by an agent at query time it is worth a great deal. It says which table to trust and, more usefully, which ones to leave alone. An agent choosing between four plausible tables answers worse than one choosing between two, and the map cuts the set down. So write it for the AI first. It will actually read it. The human rarely will.

Also, removing redundant or duplicate datasets is the cheapest way to make the right data easy to find, and it costs almost nothing.

**The grid isn't the asset. The three questions behind it are: who the data is for, what's been promised, what's actually been delivered.** Ask those of every dataset and the wrong cells stop hiding on their own.

[^1]: Open Data Contract Standard, maintained by the Bitol project under the Linux Foundation. [bitol-io.github.io](https://bitol-io.github.io/open-data-contract-standard/)
[^2]: Apache Ossie (incubating), formerly the Open Semantic Interchange. [ossie.apache.org](https://ossie.apache.org/)
[^3]: Medallion architecture (bronze, silver, gold), as described by Databricks. [databricks.com/blog](https://www.databricks.com/blog/what-is-medallion-architecture)
