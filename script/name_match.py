import re
import sys
import json

class NameMatchService:

    def match_names(self, name1: str, name2: str, expected_score: float) -> dict:
        try:
            valid1, msg1 = self.validate_name(name1)
            valid2, msg2 = self.validate_name(name2)

            if not valid1 or not valid2:
                return {
                    "match": False,
                    "validation_pass": False,
                    "validation_msg": f"Name1: {msg1}, Name2: {msg2}"
                }

            original_name1 = name1
            original_name2 = name2

            name1 = self.preprocess_name(name1)
            name2 = self.preprocess_name(name2)

            tokens1 = name1.split()
            tokens2 = name2.split()

            if len(tokens1) < len(tokens2):
                tokens1, tokens2 = tokens2, tokens1

            max_tokens = max(len(tokens1), len(tokens2))

            if max_tokens == 2:
                weights = [0.6, 0.4]
            elif max_tokens == 3:
                weights = [0.4, 0.3, 0.3]
            elif max_tokens >= 4:
                weights = [0.3, 0.3, 0.2, 0.2]
            else:
                weights = [0.5] * max_tokens

            adjusted_weights = [
                weights[i] if i < len(weights) else 0.1
                for i in range(len(tokens1))
            ]

            reversed_bonus = 0.1 if tokens1 == list(reversed(tokens2)) else 0.0

            scores = []
            for i, t1 in enumerate(tokens1):
                best = 0
                for t2 in tokens2:
                    score = self.jaro_winkler(t1, t2)
                    if len(t1) == 1 and t2.startswith(t1):
                        score = max(score, 0.9)
                    best = max(best, score)
                scores.append(best * adjusted_weights[i])

            set1, set2 = set(tokens1), set(tokens2)
            intersection = set1 & set2
            union = set1 | set2

            token_overlap = len(intersection) / len(union) if union else 0

            fuzzy_scores = [
                max(self.jaro_winkler(t1, t2) for t2 in set2)
                for t1 in set1
            ]

            fuzzy_similarity = sum(fuzzy_scores) / len(fuzzy_scores) if fuzzy_scores else 0

            sum_scores = sum(scores)

            final_score = (
                0.4 * sum_scores +
                0.3 * token_overlap +
                0.3 * fuzzy_similarity +
                reversed_bonus
            )

            fallback_used = False
            if token_overlap == 0:
                full = self.jaro_winkler(
                    name1.replace(" ", ""),
                    name2.replace(" ", "")
                )
                if full > final_score:
                    final_score = full
                    fallback_used = True

            return {
                "match": final_score >= expected_score,
                "name1": original_name1,
                "name2": original_name2,
                "final_score": round(final_score, 2),
                "reversed_bonus": round(reversed_bonus, 2),
                "sum_scores": round(sum_scores, 2),
                "token_overlap": round(token_overlap, 2),
                "fuzzy_similarity": round(fuzzy_similarity, 2),
                "fallback_used": fallback_used,
                "validation_pass": True,
                "validation_msg": "Both input name fields are valid"
            }

        except Exception as e:
            return {"match": False, "error": str(e)}

    # ---------------- HELPERS ---------------- #

    def preprocess_name(self, name: str) -> str:
        name = name.lower().strip()
        titles = ["mr", "mrs", "ms", "dr", "prof", "late", "smt", "shri", "shree", "sree", "sri"]
        for t in titles:
            name = re.sub(rf"^{t}\.?\s+", "", name)
        name = re.sub(r"[^a-z\s'/]", "", name)
        name = re.sub(r"\s+", " ", name)
        return name.strip()

    def validate_name(self, name: str):
        processed = self.preprocess_name(name)
        if not processed:
            return False, "Name is empty or missing"
        if len(processed) > 100:
            return False, "Name exceeds 100 characters"
        if not re.search(r"[a-z]", processed):
            return False, "Name contains invalid characters"
        return True, "Name is valid"

    def jaro_winkler(self, s1: str, s2: str) -> float:
        if not s1 and not s2:
            return 1.0
        if not s1 or not s2:
            return 0.0

        len1, len2 = len(s1), len(s2)
        match_window = max(len1, len2) // 2 - 1

        s1_matches = [False] * len1
        s2_matches = [False] * len2

        matches = 0
        for i in range(len1):
            start = max(0, i - match_window)
            end = min(i + match_window + 1, len2)
            for j in range(start, end):
                if s2_matches[j]:
                    continue
                if s1[i] == s2[j]:
                    s1_matches[i] = True
                    s2_matches[j] = True
                    matches += 1
                    break

        if matches == 0:
            return 0.0

        t = 0
        k = 0
        for i in range(len1):
            if not s1_matches[i]:
                continue
            while not s2_matches[k]:
                k += 1
            if s1[i] != s2[k]:
                t += 1
            k += 1

        jaro = (
            matches / len1 +
            matches / len2 +
            (matches - t / 2) / matches
        ) / 3

        prefix = 0
        for i in range(min(4, len1, len2)):
            if s1[i] == s2[i]:
                prefix += 1
            else:
                break

        return jaro + prefix * 0.1 * (1 - jaro)


# ---------------- CLI ENTRY ---------------- #

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage:")
        print("  python name_match.py \"Name One\" \"Name Two\" expectedScore")
        print("Example:")
        print("  python name_match.py \"vaishali sagar raval\" \"vaishali ben\" 0.75")
        sys.exit(1)

    name1 = sys.argv[1]
    name2 = sys.argv[2]
    expected_score = float(sys.argv[3])

    service = NameMatchService()
    result = service.match_names(name1, name2, expected_score)
    print(json.dumps(result, indent=2))
