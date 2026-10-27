# Dataset tiering & trust

*Part of [Data platform](./README.md).*

A tier is a claim, not a grade — someone declares what a dataset is worth trusting for, and that claim either holds up against monitored evidence or it doesn't. The organizations that do this well all converge on the same shape: a small number of tiers, a cheap self-declared path for most data, a gated path for the tier that carries a real promise, and continuous measurement that audits the claim rather than replacing it.

## Foundations

- **A tier without evidence is a sticker, not a signal.** Several real implementations (below) score tiers continuously against measured criteria rather than trusting a one-time declaration, specifically to stop a label from outliving the thing it described.
- **Not every tier needs the same approval cost.** The pattern that recurs across sources: self-declare the low-stakes tiers, gate only the tier that carries an enforceable promise (an SLA, a named owner, sign-off). Gating every tier produces the review queue that kills the system at scale — see [Scaling the platform](./scaling-the-platform.md).
- **"Floors" stop gaming the average.** A composite score across several quality dimensions can look fine on average while one dimension (security, lineage, ownership) is badly broken. The fix seen in practice is a per-dimension minimum a product must clear regardless of its overall score, not just a single blended number.
- **The audience a dataset serves and the trust it needs to carry are correlated, not identical axes.** Expected quality should rise with reach, but the two aren't the same thing — a widely-used dataset can still be an unpromised B, and a narrow one can be an over-governed A.
- **Metadata for machine consumption is now a distinct requirement from metadata for a wiki page.** Catalogs built in the last cycle are explicitly designed around an agent reading a typed interface at the moment it reasons, not a person browsing later — the same tier/trust signal now has two different audiences with different needs.

## Common pitfalls

- **Treating every tier as equally worth gating.** Central review of every dataset's tier is how the approval queue becomes the bottleneck, and people route around it. Gate the rare, high-stakes tier only.
- **A single blended quality score.** It hides exactly the dimension most likely to burn you — a product can average "good" while being badly ungoverned on one axis nobody's looking at.
- **No mechanism to re-test a claim.** A tier declared once and never audited again degrades invisibly; several sources now build continuous scoring in specifically to prevent this.
- **Publishing tiers only to a human-facing catalog page.** If an agent can't read the tier at the moment it picks a table, the tier isn't doing its job for the audience that increasingly matters most.
- **Confusing reach with trust.** A dataset being widely used is not the same claim as a dataset being reliable — conflating the two lets a popular-but-unpromised dataset get treated as more trustworthy than it's earned.

## How to succeed

1. Keep the tier count small (three or four) and make the top tier the only one requiring a named approver — self-declaration for everything below it.
2. Score tiers against measured, not just declared, criteria, and re-check on a cadence tied to the dataset's own expected update frequency rather than a fixed global window.
3. Use per-dimension floors alongside any blended score, so a weak dimension can't hide behind a strong average.
4. Publish the tier somewhere a querying agent can read it directly (a typed interface, not just a wiki page), if agents are expected to pick datasets autonomously.
5. Keep reach (who it's for) and expected quality (what's promised) as separate axes on record, even though they should usually correlate — the mismatches are where the risk is.

## Further reading

Closest real-world match to claimed-vs-measured tiering, with floors and agent consumption:
- [Progressive Data Product Certification: Weights, Floors, and the Trust Profile AI Reads](https://annajibgashvili.substack.com/p/progressive-data-product-certification) — four tiers (Registered/Bronze/Silver/Gold) scored continuously against 24 measured criteria; floors stop a strong score elsewhere from covering a weak one; Gold needs three named owners; agents consume the resulting trust profile directly.
- [What is a product score? (Atlan)](https://docs.atlan.com/product/capabilities/data-products/concepts/what-is-a-product-score) — a shipped commercial version of the same idea.

Tiered certification generally:
- [Governed Data Products with Bronze, Silver, and Gold Layers (Oracle)](https://blogs.oracle.com/ai-data-platform/governed-data-products-with-bronze-silver-and-gold-layers)
- [Medallion Approach to Data Products: Beyond the Promised "Gold"](https://www.moderndata101.com/blogs/medallion-approach-to-data-products-beyond-the-promised-gold) — argues the layers are ownership/reprocessing boundaries, not just quality steps.
- [Medallion Architecture Explained (2026 guide)](https://dataforest.ai/blog/medallion-architecture)

Data contracts as the claim mechanism:
- [Data contract (Wikipedia)](https://en.wikipedia.org/wiki/Data_contract)
- [What Is a Data Contract? (IBM)](https://www.ibm.com/think/topics/data-contract)
- [The Rise of Data Contracts — Chad Sanderson](https://dataproducts.substack.com/p/the-rise-of-data-contracts) and [An Engineer's Guide to Data Contracts, Pt. 1](https://mlops.community/blog/an-engineers-guide-to-data-contracts-pt-1) — Sanderson (ex-Convoy, now Gable.ai) is the most-cited practitioner voice in this space.
- [Data Contracts: 7 Critical Implementation Lessons Learned (Monte Carlo)](https://montecarlo.ai/blog-data-contracts) — references GoCardless (Andrew Jones) and PayPal's open-sourced YAML spec as the two most-cited real implementations.

Monitored quality as the audit:
- [Data Freshness Monitoring: How to Detect Stale Data Before It Breaks Dashboards](https://dev.to/iblaine/data-freshness-monitoring-how-to-detect-stale-data-before-it-breaks-dashboards-5hkm)
- [Freshness (SLA and Staleness) — Decube](https://docs.decube.io/data-quality-v2/monitor-types/freshness-sla-and-staleness) — distinguishes "arrived by deadline" from "has kept updating."
- [Data Freshness Monitoring: SLA Guide — DataWorkers](https://dataworkers.io/resources/data-freshness-monitoring-sla/) — includes a cadence learned from the table's own history rather than a fixed window.

Reach as an axis:
- [Decentralized Data Governance as Part of a Data Mesh Platform (arXiv)](https://arxiv.org/pdf/2307.02357) — domain teams decide consumption access while a central function sets and reviews global policy.
- [Data Governance Model: Frameworks, Policies, and Best Practices (Acceldata)](https://www.acceldata.io/blog/data-governance-model-how-leading-companies-ensure-compliance-and-security)

Prior art — companies that built one of these as a catalog:
- [Databook: Uber's data catalog (Atlan writeup)](https://atlan.com/uber-databook-metadata-catalog/) and [Turning Metadata Into Insights with Databook (Uber's own post)](https://www.uber.com/cl/en/blog/metadata-insights-databook/)
- [Amundsen (Lyft)](https://github.com/gtoonstra/databook/issues/10) — now a Linux Foundation AI project, generally considered the most mature open-source one of this generation.
- Also exist, less documented publicly: Airbnb Dataportal, Netflix Metacat, LinkedIn DataHub, Spotify Lexikon.

Metadata built for agents, not just people:
- [Data Catalog for AI: Built for Agents, Not Just People (Atlan, 2026)](https://atlan.com/know/data-catalog-for-ai/)
- [What It Takes to Build an AI-Ready Data Catalog in 2026 (OvalEdge)](https://www.ovaledge.com/blog/ai-ready-data-catalog)

## See also

- [Governance & trust](./governance-and-trust.md) — the contract layer this page's tiers get tested against
- [Scaling the platform](./scaling-the-platform.md) — why gating every tier doesn't survive growth
- [Organization & ownership](./organization-and-ownership.md) — who a tier's named owner actually is
