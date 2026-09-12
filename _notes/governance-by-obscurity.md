---
title: "Governance by obscurity"
date: 2026-09-09
tags: [data platform, ai]
---

*This is the third post on data platforms. Read <a class="internal-link" href="/the-org-chart-is-the-real-architecture">part 2</a> if you haven't already.*

Every data platform sits somewhere on a line between distributed flexibility and centralized control. Almost nobody picks a spot on that line on purpose. Usually they start at the flexible end, because that's what gets a platform launched: open access, self-service, minimal review. Governance shows up later, usually after something breaks in front of the wrong person, and it shows up as a reaction, not a decision.

For a long time, that worked well enough, but mess piled up under the surface. Almost nobody went looking for it. People stick to the datasets they already know: a new hire asks a colleague which table to use, gets the same three names everyone gets, and never wanders into the abandoned duplicate three schemas over. A platform can be full of ungoverned, half-documented tables nobody's touched in years, and it barely matters, because habit keeps most people out of them. **Call it governance by obscurity**. Nobody enforced a common standard, but nobody found the mess either, so it never got tested.

**That's the part that's ending nowadays**. An AI agent querying your platform doesn't have a habit. It doesn't ask a colleague which table everyone uses, it defaults to searching the whole thing at once, suddenly finding the table with a plausible-sounding name, and uses it with full confidence, whether or not anyone still stands behind it. This could be a stale niche dataset or some raw unmodelled data - nor being intended for general data consumers. The obscurity that used to protect you was never a safeguard. It was luck, and agents don't share the instincts that made the luck hold.

What matters now is the same thing that always mattered, just no longer optional to skip: whether a dataset has someone's name attached to it. Obscurity used to be a stand-in for that. It isn't anymore.

None of this resolves the trade-off. Flexibility still gets a platform running faster with data catered for the business requirements, and every ounce of governance still costs someone speed. What's changed is that you no longer get to leave that call unmade and let obscurity cover for you. 

The next post is about how to actually make it, dataset by dataset, with a framework instead of a shrug.