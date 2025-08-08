from rapidfuzz import process, fuzz
import json
import os
from django.conf import settings

def normalize(s: str) -> str:
    return s.strip().lower()

class GetBestMatch:
    def __init__(self, query: str, json_path: str, score_cutoff: int = 60):
        self.query = str(query).capitalize()
        self.score_cutoff = score_cutoff
        self.json_path = os.path.join(settings.BASE_DIR, json_path)
        self.data = self._load_json(self.json_path)

        self.alias_map = {}
        self.canonical_map = {}
        self.canonical_names = []

        for entry in self.data:
            canonical = entry.get("canonical", "")
            if not canonical:
                continue
            norm_canonical = normalize(canonical)
            self.canonical_map[norm_canonical] = entry
            self.canonical_names.append(canonical)
            for a in entry.get("aliases", []):
                self.alias_map[normalize(a)] = canonical

        self.result = self._resolve()

    def _load_json(self, path: str):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _resolve(self):
        nq = normalize(self.query)

        if nq in self.alias_map:
            canonical = self.alias_map[nq]
            entry = self.canonical_map.get(normalize(canonical))
            return {"entry": entry, "score": 100.0, "matched_on": "alias", "matched_string": canonical}

        fuzzy = process.extractOne(
            self.query,
            self.canonical_names,
            scorer=fuzz.WRatio,
            score_cutoff=self.score_cutoff,
        )
        if fuzzy:
            name, score, _ = fuzzy
            entry = self.canonical_map.get(normalize(name))
            return {"entry": entry, "score": score, "matched_on": "fuzzy", "matched_string": name}

        return {"entry": None, "score": None, "matched_on": None, "matched_string": None}

    def get(self):

        return self.result
