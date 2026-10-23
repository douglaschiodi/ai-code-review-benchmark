"""Deterministic review lab. Only built-in, original candidate functions run."""
import copy
import json

def intervals(values):
    merged = []
    for start, end in sorted(values):
        if start > end:
            raise ValueError("reversed interval")
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(end, merged[-1][1])
        else:
            merged.append([start, end])
    return merged

def events(values):
    seen, result = set(), []
    for event in values:
        key = (event["tenant"], event["id"])
        if key not in seen:
            seen.add(key)
            result.append(event)
    return result

def tenant_total(values, tenant):
    return sum(e["cents"] for e in values if e["tenant"] == tenant and e["status"] == "settled")

def wrong_intervals(values):
    result = []
    for start, end in sorted(values):
        if result and start < result[-1][1]:
            result[-1][1] = end
        else:
            result.append([start, end])
    return result

def wrong_events(values):
    return list({e["id"]: e for e in values}.values())

def wrong_total(values, tenant):
    return sum(e["cents"] for e in values if e["status"] == "settled")

CANDIDATES = {
    "reference": {"intervals": intervals, "events": events, "tenant_total": tenant_total},
    "plausible_but_wrong": {"intervals": wrong_intervals, "events": wrong_events, "tenant_total": wrong_total},
}
CASES = [
    ("intervals", "empty", ([],), [], 1),
    ("intervals", "disjoint", ([[4,5],[1,2]],), [[1,2],[4,5]], 1),
    ("intervals", "touching", ([[1,2],[2,4]],), [[1,4]], 2),
    ("intervals", "nested", ([[1,9],[2,3]],), [[1,9]], 2),
    ("intervals", "zero width", ([[0,0],[0,1]],), [[0,1]], 1),
    ("events", "empty", ([],), [], 1),
    ("events", "repeated", ([{"tenant":"a","id":"1"},{"tenant":"a","id":"1"}],), [{"tenant":"a","id":"1"}], 1),
    ("events", "tenant isolation", ([{"tenant":"a","id":"1"},{"tenant":"b","id":"1"}],), [{"tenant":"a","id":"1"},{"tenant":"b","id":"1"}], 3),
    ("events", "first arrival", ([{"tenant":"a","id":"1","v":1},{"tenant":"a","id":"1","v":2}],), [{"tenant":"a","id":"1","v":1}], 2),
    ("tenant_total", "empty", ([], "a"), 0, 1),
    ("tenant_total", "pending excluded", ([{"tenant":"a","status":"pending","cents":99}], "a"), 0, 1),
    ("tenant_total", "other tenant", ([{"tenant":"b","status":"settled","cents":500}], "a"), 0, 3),
    ("tenant_total", "refund signed", ([{"tenant":"a","status":"settled","cents":100},{"tenant":"a","status":"settled","cents":-30}], "a"), 70, 2),
]

def evaluate(name):
    if name not in CANDIDATES:
        raise ValueError("choose a built-in candidate")
    rows = []
    for task, label, args, expected, weight in CASES:
        try:
            passed = CANDIDATES[name][task](*copy.deepcopy(args)) == expected
            error = None
        except Exception as exc:
            passed, error = False, type(exc).__name__
        rows.append({"task": task, "case": label, "passed": passed, "weight": weight, "error": error})
    return {"candidate": name, "earned": sum(r["weight"] for r in rows if r["passed"]),
            "possible": sum(r["weight"] for r in rows), "cases": rows}

def report():
    return {"rubric_version": 1, "scope": "Synthetic fixtures; no external model ranking.",
            "results": [evaluate(name) for name in sorted(CANDIDATES)]}

if __name__ == "__main__":
    print(json.dumps(report(), indent=2))

