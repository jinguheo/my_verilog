# Review workflow

States:
- proposed
- triaged
- reviewed
- promoted
- rejected

Promotion policy:
- require evidence
- merge synonyms first
- prefer reusable labels
- prefer cross-project canonical labels when OpenTitan and Ibex express the same role differently

Recommended review pass order:
1. protocol labels
2. controller / memory / bridge roles
3. CPU-specific Ibex labels
4. taxonomy merge / synonym cleanup
