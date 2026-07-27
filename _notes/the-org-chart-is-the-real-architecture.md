---
title: "The org chart is the real architecture - usually"
date: 2026-07-27
tags: [data-platforms, organization]
---

*This is the second post on data platforms. If you haven't, <a class="internal-link" href="/one-platform-does-not-solve-your-data-problem">read part 1</a> first.*

Making a data platform functional was never a technical problem. It's an organizational one, and it gets harder as your org grows, not as your data does.

> A data platform for 50 users vs. 500 users are totally different.

In a five-person team, everyone knows the handful of datasets that exist and who built them. At fifty people, nobody holds that map anymore. Teams stick to their own corner, don't know what already exists next door, and quietly rebuild it: same numbers, slightly different logic, different name. Not because anyone wanted three versions of "active customers." Because finding the existing one was harder than writing a new fitting query.

"Functional" moves too. For one team, functional means: ask Sarah, she built it. Across ten teams, that stops working the moment Sarah changes roles, and nobody agrees on who inherited what she built.

Reorgs make this visible fast. Boundaries move overnight; the data doesn't move with them. A dataset's owning team gets merged or split, and the dataset just sits there, kept alive by whoever still has write access, while the new domains around the new chart get all the attention. Nobody decided to abandon it. It just stopped being anyone's problem the day the boxes moved. Whoever officially inherits it later usually doesn't want it: owning code you didn't write and can't explain isn't a promotion, (traditionally) it's been debt with your name on the pager (more on this in a coming post).

Distributing ownership to the teams closest to the data only works if those teams can actually hold onto it, through growth and through reorgs. Most companies aren't there yet, which is how "we're doing mesh" turns into the mess from part 1.

The version that survives contact with an org chart: **build data domains, not just datasets**. A domain is a bounded, durable unit of data, with an intention of lasting presence. This could be properly defined database, schema, or dbt project for that matter, that one unit owns end to end. 

Often in smaller organisations, one domain would naturally be owned by one team - which is already a well-defined group with shared responsibilities and incentives. It can be ideal, but in the long term it might not, especially in larger organisations.

For us in the **investment industry, equities would be a natural example regardless of embedded teams within**, certain data products should last despite changing strategic focus or investment philosophies.

The unit should strive for data consistency regardless of the who is part of the owners. This could mean that it exist of one person from various teams, naturally by roles or responsibilities, but preferably defined upon the business functions. The fence isn't the point. Survivability and durability is: when the reorg hits, the data domain still lives on with minimal impact.

Defining and building data domains based upon a well-defined unit improves the durability of a data, making the ownership and survivorship better and easier, consequently improving long-term insights. 

