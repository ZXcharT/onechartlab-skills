#!/usr/bin/env python3
"""Deterministic policy evaluator for serialized T01-T14 traces."""
import json
from pathlib import Path

READ_ROLES = {"research", "validation", "plan_review"}
SAFE_LOAD_FAILURE_ACTIONS = {"save_state", "report_failure", "remain_stopped"}


def evaluate(trace):
    rule = trace["id"]
    s = trace["scenario"]
    if rule == "T01":
        mode = s.get("mode")
        if mode == "direct":
            ready = s.get("direct_eligible") is True
        elif mode == "light":
            ready = all([
                s.get("plan_format") == "steps_verify",
                s.get("approver") is True,
            ])
        elif mode == "controlled":
            ready = all([
                s.get("plan_format") == "six_section",
                s.get("approver") is True,
                s.get("review") == "PLAN_OK",
                bool(s.get("reviewer_agent_id")),
                s.get("reviewer_thread_new") is True,
                s.get("reviewer_access") == "read",
            ])
        else:
            ready = False
        return "EXECUTE" if ready else "WAIT_APPROVAL"
    if rule == "T02":
        source = s.get("selection_source")
        if source == "current":
            identity_ok = all([
                s.get("no_suitable_agent") is True,
                s.get("current_agent_child") is True,
            ])
        elif source in {"user", "task"}:
            identity_ok = bool(s.get("delegate_agent_id")) and s.get("agent_available") is True
        else:
            identity_ok = False
        thread_ok = s.get("same_role") is True and (s.get("new_thread") is True or s.get("same_thread") is True)
        model_ok = not s.get("model_override", False) or s.get("model_override_approved") is True
        return "CONTINUE" if identity_ok and thread_ok and model_ok else "BLOCKED"
    if rule == "T03":
        role, access = s.get("role"), s.get("access")
        allowed = (role in READ_ROLES and access == "read") or (role == "writer" and access == "write" and s.get("named_writer") is True)
        return "ALLOW" if allowed else "BLOCKED"
    if rule == "T04":
        requires_canary = any(s.get(name) is True for name in (
            "batch", "writes", "schema_uncertain", "permission_uncertain", "high_cost", "high_impact"
        ))
        if not requires_canary:
            ready = all([
                s.get("read_only") is True,
                s.get("low_cost") is True,
                s.get("structure_known") is True,
                s.get("directly_verifiable") is True,
            ])
        else:
            ready = all([
                s.get("canary") == "OK",
                s.get("same_thread") is True,
                s.get("same_tool_scope") is True,
                s.get("source_changed") is False,
            ])
        return "PRODUCE" if ready else "BLOCKED"
    if rule == "T05":
        if s.get("duplicate_executor") is True:
            return "BLOCKED"
        return "BACKLOG" if s.get("domain_owned") else "QUERY"
    if rule == "T06":
        ready = all([
            s.get("authorized_run_root") is True,
            s.get("under_run_root") is True,
            s.get("single_writer") is True,
            s.get("ownership_conflict") is False,
        ])
        return "ALLOW" if ready else "BLOCKED"
    if rule == "T07":
        ready = all([
            s.get("final") == "ACCEPTED",
            s.get("final_exists") is True,
            bool(s.get("build_entry")),
            s.get("audit_status") == "AUDIT_DONE",
        ])
        return "DELIVER" if ready else "FINAL_BARRIER"
    if rule == "T08":
        ready = all([
            s.get("event") == "STATUS_REPORT",
            s.get("safe_work") is True,
            s.get("decision_needed") is False,
        ])
        return "CONTINUE" if ready else "WAIT"
    if rule == "T09":
        if s.get("parent_unavailable") is True:
            return "PERSIST_BLOCK"
        ready = all([
            s.get("background_failure") is True,
            s.get("visible_report") is True,
            s.get("production_paused_until_report") is True,
        ])
        return "NOTIFY" if ready else "BLOCKED"
    if rule == "T10":
        ready = all([
            s.get("attempt") == 1,
            s.get("local_reversible") is True,
            s.get("changes_source") is False,
            s.get("changes_scope") is False,
            s.get("expands_access") is False,
            s.get("reduces_credibility") is False,
        ])
        return "RECOVER" if ready else "ESCALATE"
    if rule == "T11":
        ready = all([
            s.get("audit_done") is True,
            s.get("state") == "NEEDS_REVISION",
            s.get("second_audit_requested") is False,
            s.get("main_agent_owns_fix") is True,
        ])
        return "MAIN_FIX" if ready else "BLOCKED"
    if rule == "T12":
        fields = ("scope", "direction", "risk", "deliverable", "permission", "external_effect")
        material = any(s.get(name) is True for name in fields)
        return "REAPPROVAL" if material else "CONTINUE"
    if rule == "T13":
        ready = all([
            s.get("communication_loaded") is True,
            s.get("path") == "references/communication-protocol.md",
            s.get("loaded_before_event") is True,
        ])
        return "LOAD_OK" if ready else "BLOCKED"
    if rule == "T14":
        if s.get("communication_loaded") is True:
            return "ALLOW"
        if s.get("event_pending") is not True:
            return "BLOCKED"
        return "HARD_BLOCK" if s.get("requested_action") in SAFE_LOAD_FAILURE_ACTIONS else "SAFETY_VIOLATION"
    raise ValueError(f"unknown rule: {rule}")


def run_fixture(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    results = []
    for case in data["cases"]:
        got = evaluate({"id": data["id"], "scenario": case["scenario"]})
        results.append({"name": case["name"], "got": got, "expected": case["expected"], "ok": got == case["expected"]})
    return all(item["ok"] for item in results), results


if __name__ == "__main__":
    import sys
    ok, results = run_fixture(sys.argv[1])
    for item in results:
        print(f"{Path(sys.argv[1]).name}:{item['name']}: {item['got']} (expected {item['expected']})")
    raise SystemExit(0 if ok else 1)
