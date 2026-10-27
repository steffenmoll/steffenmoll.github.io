# Blog backlog

## Series: Data platforms

An ongoing series on why data platforms don't solve the problems people buy them for, and what actually helps. Posts 1 to 4 are one arc; later posts build on it.

Storytelling approach: promise and overdeliver, like Mark Rober — open with the claim, then earn it. 
Keep posts within a 3 min read, but resulting in clear consise messages.

### Post 1: One platform doesn't solve your data problem — status: drafted

Angle: buying/building a data platform doesn't remove your underlying data problems, it trades them for a new set.

Key points:
- A platform promises to solve everything, but introduces its own new problems
- The flexibility that makes a platform useful is the same thing that creates mess
- "Data mesh" often becomes "data mess" in practice

Avoid: don't get into governance or ownership here (that's post 3), don't get into specific tooling (that's post 4).

### Post 2: Making a functional data platform is not a technical problem

Angle: the hard part of a data platform isn't the tech stack, it's the organization around it.

Key points:
- Problems scale with org size, not with data volume. Small organization, people know the available datasets. With bigger organizations, people tend to stick to their familiar branch, and datasets easily become duplicated with different colors.
- What "functional" means changes as the org grows — a platform that works for one team breaks down across
- the vision should be to build datasets hence data domains - often (unfortunatley) managed by one team - which lasts and lives healty also after an org change. Domains could be a database, schema, dbt project, etc.

Solution: Intentionally design the platform for scale, both techically and organizationally. The design architecture should be business centered first, deliberitly defining the difference between business oriented domains and business supporting domains (tech functions).

Avoid: don't repeat post 1's "platform doesn't solve everything" framing, take it as given and move on.

### Post 3: Flexibility vs governance — where to draw the line

Angle: every platform sits somewhere on a flexibility/governance spectrum, and most orgs default to the wrong end without deciding on purpose.

Key points:
- Who should own a data product — the data engineer who builds it, or the business stakeholder who needs it?
- Is a data product one dataset or a bundle of related ones? This decision is a governance choice, not a technical one
- Need for a quality "stamp" on a data product before others can trust and reuse it
- What you gain and lose at each end of the spectrum — be concrete, not both-sides-y

Solution: Define a framework for how to grade datasets, based on business metrics and data characteristics. 

Avoid: don't resolve this into a single "best practice," the point is that it's a real trade-off.

### Post 4: Where a dataset naturally fits — status: drafted

#### My original notes (kept)

Angle: grounded, example-driven follow-up — what does dealing with the scaling problem actually look like.

Two things needs to be in place:
1. Define the landscape/draw the map: define the data platform framework
2. Help AI and agents **navigate** the landscape: define business logic and rules

**On the landscape:**
- axis 1: set various quality tiers, eg. A, B, C.
A: clear expectations: where the upper tier is business critical and has a defined SLA. has data contract. defined coverage.
B: somewhat defined expectations: data being monitored, have certain test metrics, but no defiend expectations on downtime.
C: undefined: sandbox data, not monitored, ad hoc
-> in other words, this defines the expected quaity

- axis 2: monitored quality
uptime, metadata coverage (both on object - aka table, view, etc. - and column level), tests failing, freshness, content coverage, history/date range, usage/users, etc.

- axis 3: target domain/audience: org-wide, sub-groups based on business capabilities (eg. Equities, Fixed Income), team

- axis 4: content matter category: a way to group data into natural buckets as due to what the data is about. eg.

**Navigating**
MCPs and skills as helping tools to direct the AI in the right direction. These should be maintained centrally in the organisation, ensuring a consistent behaviour pattern.

**Key points:**
- Underlying platform rot gets worse — and more visible — once AI gets layered on top of it.
- Documnent for the AI first, will actually read the docs, the human rarely will.
- Less is more. The fewer competing datasets, the more accurate the AI will answer.

Avoid: keep this concrete and example-led, it's the payoff post after three posts of framing.

From an earlier version, dropped but worth remembering:
- Is bronze/silver/gold (e.g. Matillion's medallion pattern) practically sufficient, or does it fall short in practice?
- NBIM as a reference case: raw -> int -> mrt, with dbt

#### Worked outline after grilling

Title: Where a dataset naturally fits. Spine is the map/navigate analogy: this post draws the map, the navigation half is left for later without being teased.

Claim: expected quality should rise with reach, and the datasets worth your attention are the ones where it doesn't.

Structure:
- Open on the part 3 trade-off, then state the two things needed: draw the map, then navigate it. This post is the map.
- All four axes, in prose, one short paragraph each. Expected quality (A/B/C). Monitored quality (the thing that tests the claim). Reach (team, business capability, org-wide). Subject matter (filing, not grading).
- One matrix, expected quality down the side against reach across the top, cells holding the kind of dataset that naturally lands there. Header row in monospace.
- The diagonal is the normal case. Below it is over-built governance, wasteful but harmless. Above it is the damage, and it's post 3's governance by obscurity with coordinates.
- Rules that keep the map honest: declared cadence, no monitoring means a hard cap at C, owner proposes and only A needs data ops sign-off, sustained contradiction proposes a move either way.
- The example, which lands in the C/org-wide cell: a dataset the business treated as critical that had been deprecated and had stopped updating. Nobody had written down what it promised, so there was nothing for reality to contradict.
- Close on the map being read by an agent rather than a human, so write the docs for the AI first. Last line lands on the map itself, no handoff.

Form: ~920 words, one table, house prose otherwise, no em dashes.

Avoid: don't re-run post 3's argument that AI makes platform rot visible. Leave rollout out, grading an existing estate is its own post. Don't let the axes crowd out the example.

### Post 5: AI is amplifying everything

Angle: as AI lower the barrier for generating, the fundamentals becomes even more important

Key Points: 
- Barrier to create data assets, dashboards, data apps, etc. has never been lower - hence its more important than ever to question itself: "how and in what way can it create value"
- Institutional knowledge and guidelines increases in importance

Claim: A organizatinos AI skill instructions is the most important asset to be future proof.

Solution: Use AI to enforce institutial guidelines to create organized platform, rather than clutter

Inherits from post 4: MCPs and skills as the tools that point agents at the right data, maintained centrally so behaviour stays consistent. Post 4 ends on why the labels need to be machine-readable; this post owns the machinery.

## Idea bank (unsorted, not yet assigned to a post)

- How do you actually choose the right dataset in the first place?
- Open Source (and self-hosting) has never been easier
