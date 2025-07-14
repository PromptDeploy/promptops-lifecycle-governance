# LICENSE PACKAGE

This file describes how the PromptOps Lifecycle Governance artifact can be reused, integrated, or commercially licensed in SaaS SDK platforms.

## Permitted Uses (Default Open License)

Under the default MIT license, you are free to:

- Integrate components into internal workflows, SDKs, or CI pipelines
- Repackage prompt schemas or eval configs in your own repos
- Fork, extend, or modify for your own prompt governance needs
- Use in workshops, technical docs, or education programs

Please retain attribution to the original author (`Hou Chia`) in derived works, especially if distributed externally.

## Integration Use Cases

You may freely embed this artifact into:

- LLM-powered SaaS platforms (e.g., RAG, agent frameworks, orchestration layers)
- Internal LLM governance systems for versioning, testing, and rollback
- CI/CD pipelines enforcing prompt safety, drift, and evaluation gates
- Prompt lifecycle products used by customers or internal developers

## ⚠️ Limitations

This artifact is **not yet covered by a commercial support contract or service agreement**. If you are embedding this into a paid product or regulated environment, we recommend:

- Running your own legal review
- Logging changes to artifacts for auditability
- Contacting the author for a hardened, SLA-backed commercial version

**Commercial usage** — defined as embedding this artifact into a product offered for sale or customer use — requires a separate licensing agreement.

## OEM / Commercial Licensing

If you would like to:

- White-label this artifact inside your platform
- Offer it as a governance module to your customers
- Customize it with support for your stack (e.g. LangChain, Semantic Kernel, Anthropic SDKs)
- Receive enterprise-grade security reviews and CI plug-ins

→ **Contact the author for a commercial licensing package.**

Email: [Hou Chia](mailto:kappainnovationllc@gmail.com)

## Remix & Distribution Guidelines

You may remix this artifact across teams or business units **as long as you**:

- Maintain file-level attribution or reference to this repo
- Disclose usage upon request for attribution or licensing compliance
- Link back to: [https://github.com/PromptDeploy/promptops-lifecycle-governance](https://github.com/PromptDeploy/promptops-lifecycle-governance)
- Do not falsely represent the author as having reviewed or endorsed your fork

---

## Recommended Bundling Pattern

For internal reuse or remix:

- Fork this repo and preserve:

  - `schemas/`, `evals/`, `ci/`, `scripts/`, `logs/`
  - `README.md`, `LICENSE`, `LICENSE_PACKAGE.md`

- Customize under your org’s namespace and pipeline rules
- Document any divergence from upstream with clear changelogs

## Contact

For licensing, collaboration, or integration help:

**Hou Chia**
[kappainnovationllc@gmail.com](mailto:kappainnovationllc@gmail.com)
[https://linkedin.com/in/houchia](https://linkedin.com/in/houchia)

MIT License still applies unless explicitly overridden by a signed commercial agreement.
