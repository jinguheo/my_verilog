# Spec-Code KG Late Binding Evaluation

## Architecture Decision

- Keep the custom code KG as the primary retrieval engine.
- Keep Graphify as a broad code/architecture navigation graph.
- Keep OpenKB as a separate spec-document wiki/KG.
- Integrate at query time using shared keys: `module_name`, `ip_block`, `spec_section`, `doc_anchor`, and `approved_label`.

## Link Coverage

- Spec docs scanned: 986
- Docs with any late-binding key: 925 (93.81%)
- RTL/spec-like docs linked: 422/426 (99.06%)
- Module exact-name doc links: 806
- IP/path doc links: 885
- Approved-label doc links: 782

## Code Coverage

- Code modules scanned: 1383
- Modules with any doc link: 1325 (95.81%)
- Modules with exact module-name doc link: 286
- Modules with IP-level doc link: 1312
- IP blocks with docs: 56/56 (100.00%)

## Top IP Blocks by Spec Doc Count

- ibex: 194 docs
- lc_ctrl: 131 docs
- tlul: 128 docs
- rstmgr: 106 docs
- pwrmgr: 104 docs
- ast: 91 docs
- edn: 90 docs
- pinmux: 90 docs
- aes: 88 docs
- kmac: 84 docs
- otbn: 82 docs
- clkmgr: 76 docs
- csrng: 74 docs
- keymgr: 74 docs
- uart: 74 docs

## Assessment

Late binding is feasible and preferable to physical graph merge. The strongest reliable key is `ip_block` from paths and HJSON/doc layout. Exact `module_name` links exist, but are too sparse to be the only integration bridge. `approved_label` is useful as a weak recall signal.

Recommended query-time flow:

1. Resolve code query against the custom code KG.
2. Expand result modules to `ip_block` and `approved_label` keys.
3. Fetch OpenKB doc anchors matching those keys.
4. Add Graphify community/context only for architecture questions.
5. Return merged answer with provenance from each store instead of merging graph storage.
