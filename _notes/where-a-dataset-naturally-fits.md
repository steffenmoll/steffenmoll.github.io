---
title: "Where a dataset naturally fits"
date: 2026-10-27
tags: [data platform, data quality, ai]
---

*This is the fourth post on data platforms. Read <a class="internal-link" href="/governance-by-obscurity">part 3</a> if you haven't already.*

Part 3 left a trade-off open: how much governance, and where to spend it. Making that call dataset by dataset takes two things. You need a map of the terrain, and you need a way for people and agents to navigate it. This post is about drawing the map, because you can't give anyone directions across ground nobody has surveyed.

A usable map has four axes.
- **Reach.** Who the data is for. One team, a business capability (eg. like equities, fixed income), or the whole firm.
- **Subject matter.** What the data is about, so related things sit together. This could be the difference of reference, operational, derived/analytical and alternative. This one is filing rather than grading, and it does less work than the other three, but a map without it is hard to read.
- **Expected quality.** What somebody has promised about the dataset. Three tiers is enough:
  - `tier A`: someone has signed something. Data contract, named owner, defined coverage, and an SLA that gets honoured at three in the morning.
  - `tier B`: someone is watching. Tests run and monitoring exists, but nobody has promised it will be there on Monday.
  - `tier C`: nothing has been promised at all. Sandbox, ad hoc, use at your own risk.
- **Monitored quality.** What the evidence shows: uptime, freshness, failing tests, history range, how many people query it. And **metadata coverage**, at both object and column level, which is the one most platforms skip and the one an agent leans on hardest when it picks a table. The tier is a claim, and this is what tests it.


Two of those axes carry most of the weight once you put them on a grid. Expected quality down the side, reach across the top, and every dataset you own lands in exactly one cell.

| | Org-wide | Business capability | One team |
|---|---|---|---|
| `tier A` | **official positions, firm reporting** | capability benchmarks, risk inputs | rare, and usually over-built |
| `tier B` | widely used, never promised | **most modelled marts** | a team's monitored working set |
| `tier C` | ungoverned, and everyone is using it | exploratory work on a strategy | **scratch models, ad hoc** |

Most data should sit on the diagonal, and most of it does. A scratch model one analyst uses doesn't need an SLA. The official position data the whole firm reports on can't be a sandbox table. Expected quality rises with reach because the cost of being wrong rises with reach, and that correlation is what makes the map readable at a glance.

The interesting datasets are the ones off the diagonal.

Towards the top right you have over-built. A team-local dataset with a data contract and a pager rotation is governance spent where very little was at risk. That's wasteful rather than dangerous, and it usually means somebody got enthusiastic.

Towards the bottom left is where the damage lives. A dataset the whole firm leans on, sitting at `tier C`, with nobody's name on it and no monitoring. Part 3 called this governance by obscurity. It survives because nobody has gone looking, not because it works.

A few rules keep the map honest. The declared cadence is the cheapest of them: a dataset that says "expected daily" and last updated in March needs no SLA and no governance forum to tell you something is wrong. Monitoring isn't optional above `tier C` either, because with no instrumentation there's no evidence, so an uninstrumented dataset can't hold `tier B` or `tier A` however well built it is. New datasets start at `tier C`, which is accurate. Nobody has promised anything about them yet.

The owning team proposes where its dataset sits. Only `tier A` needs sign-off, from a data ops team, because it's the only tier that comes with a promise somebody has to answer for. When the monitoring contradicts the claim for longer than the dataset's own update cadence, the dataset gets proposed for a move, in either direction.

The bottom left corner isn't hypothetical.

Somewhere I worked before, there was a dataset the business treated as critical. It fed reporting that people made decisions on. It had been deprecated some time earlier and had stopped updating, and it still looked completely fine, because stale data loads perfectly well and the row count doesn't drop when nothing new arrives. Nobody had ever written down what the dataset was for, or how often it should refresh.

> Nobody had written down what it promised, so there was nothing for reality to contradict.

Drawing the map is what surfaced it. No new tool was involved. Somebody had to sit down and write what the dataset claimed, and then the claim and the evidence disagreed immediately.

One more reason to bother. A map like this does very little as a wiki page, because the people who would benefit from it don't read wikis. Read by an agent at query time it is worth a great deal. It says which table to trust and, more usefully, which ones to leave alone. An agent choosing between four plausible tables answers worse than one choosing between two, and the map is what cuts the set down. So write it for the AI first. It will actually read it. The human rarely will.

Once the map exists you can see which datasets are sitting in the wrong cell. That list is usually short, and it is where the work is.
