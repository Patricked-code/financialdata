"""Regression gate for the pre-existing eleven-file canonical memory reading order.

The README is the original source of this documented order.  The factory is
additive and must never elevate its own files ahead of project governance.
"""
from pathlib import Path
import re
import unittest

from factory import entry

PROJECT = Path(__file__).resolve().parents[2]

DOCUMENT_SECTIONS = (
    ("README.md", "## Mémoire persistante — ordre de lecture obligatoire"),
    ("GOVERNANCE.md", "## 2. Mémoire persistante obligatoire"),
    ("AGENTS.md", "## Règle n°2 — Lire la mémoire persistante"),
    ("CLAUDE.md", "## Avant chaque travail"),
    ("factory/ARRIVAL.md", "## 2. Lecture canonique avant toute programmation"),
)


def read_order(path, section):
    content = (PROJECT / path).read_text(encoding="utf-8")
    if section not in content:
        raise AssertionError(f"Canonical section missing in {path}")
    body = content.split(section, 1)[1].split("\n## ", 1)[0]
    matches = re.findall(r"(?m)^\d+\.\s+.*?\x60([^\x60]+\.md)\x60", body)
    return tuple(matches)


class CanonicalMemoryReadOrderTests(unittest.TestCase):
    def test_all_eleven_canonical_files_are_present(self):
        expected = entry.CANONICAL_READ_ORDER
        self.assertEqual(len(expected), 11)
        self.assertEqual(len(set(expected)), 11)
        self.assertEqual(expected[0], "GOVERNANCE.md")
        self.assertEqual(expected[-1], "docs/ISSUER_DISCOVERY_MATRIX.md")
        self.assertTrue(all((PROJECT / path).is_file() for path in expected))

    def test_all_first_read_guides_agree_with_original_readme(self):
        original = read_order(*DOCUMENT_SECTIONS[0])
        self.assertEqual(original, entry.CANONICAL_READ_ORDER)
        for path, heading in DOCUMENT_SECTIONS[1:]:
            with self.subTest(path=path):
                self.assertEqual(read_order(path, heading), original)

    def test_financial_pipeline_is_unchanged_and_factory_is_transverse(self):
        architecture = (PROJECT / "ARCHITECTURE.md").read_text(encoding="utf-8")
        roadmap = (PROJECT / "ROADMAP.md").read_text(encoding="utf-8")
        self.assertIn(
            "0 SOURCE\n  ↓\n1 RAW\n  ↓\n2 MAPPED\n  ↓\n3 CANONICAL\n  ↓\n4 DERIVED\n  ↓\n5 ANALYTICS",
            architecture)
        self.assertIn("SOURCE → 1 RAW → 2 MAPPED → 3 CANONICAL → 4 DERIVED → 5 ANALYTICS", roadmap)
        self.assertIn("## 13. Usine de développement intégrée", architecture)
        self.assertIn("## 6. Raccordement de l'usine de développement", roadmap)
        self.assertIn("### P1-B — Manifeste machine-lisible", roadmap)
        self.assertIn("### P1-D — Périodes et attribution", roadmap)

    def test_factory_operational_documents_are_not_first_read(self):
        first_read = set(entry.CANONICAL_READ_ORDER)
        self.assertNotIn("factory/state.json", first_read)
        self.assertNotIn("factory/HANDOFF.json", first_read)
        self.assertNotIn("factory/CONTINUITY.md", first_read)
        arrival = (PROJECT / "factory/ARRIVAL.md").read_text(encoding="utf-8")
        self.assertIn("Deuxième passage", arrival)
        self.assertIn("factory/CONTINUITY.md", arrival)


if __name__ == "__main__":
    unittest.main()
