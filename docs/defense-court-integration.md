# Defense Court Integration

## 1. Overview

**Defense Court Integration** defines how the **Yin-Yang Structural Immune OS** connects defensive detection, Reverse Resonance, immune memory, regulatory control, human review, and final adjudication.

In v0.1, the system defined the basic immune architecture:

* Yin Layer: humoral structural memory
* Yang Layer: cellular defensive response
* Taiji Layer: helper-cell orchestration
* Regulatory Layer: overreaction control

In v0.2, the system added:

* Reverse Resonance Event Layer
* premise exposure
* safe verification response
* typed defensive response patterns

In v0.3, the system added:

* Immune Memory Circulation Layer
* recurrence tracking
* strengthening
* decay
* distribution
* retirement

In v0.4, the system adds:

* Defense Court Integration
* adjudication
* human review linkage
* evidence recording
* classification stabilization
* immune memory correction
* auditability

The purpose of this layer is to ensure that defensive actions are not only reactive, but reviewable, correctable, and accountable.

In short:

> A defensive immune OS must not only respond.
> It must judge, record, review, and correct.

---

## 2. Purpose

The purpose of Defense Court Integration is to provide a structured adjudication layer for suspicious, unsafe, ambiguous, or disputed defensive events.

AI defense systems may detect suspicious structures, but detection alone is not final judgment.

A suspicious event may be:

* truly unsafe
* ambiguous
* a false positive
* a legitimate request with poor wording
* a high-risk operation requiring authority verification
* a novel pattern requiring human review
* an adversarial structure requiring immune memory strengthening

Defense Court Integration defines how these cases are reviewed and recorded.

It answers questions such as:

```text
Was the input actually unsafe?
Was the defensive response proportionate?
Should immune memory be strengthened?
Should the memory be weakened or retired?
Should the case be escalated to human review?
Should future similar cases be handled differently?
```

---

## 3. Safety Boundary

Defense Court Integration is strictly defensive.

It may support:

* classification
* adjudication
* evidence review
* human review routing
* immune memory update
* false-positive correction
* safe response recommendation
* audit logging
* regulatory adjustment

It must not support:

* retaliation
* counterattack
* external intrusion
* malware deployment
* unauthorized access
* third-party disruption
* coercive manipulation
* autonomous punishment
* offensive escalation

The Defense Court does not judge people.

It judges defensive events, input structures, and memory updates.

The target of review is the structure of the event, not the identity of a person, organization, or external system.

---

## 4. Role in Yin-Yang Structural Immune OS

Defense Court Integration serves as the adjudication and audit layer.

```text
Input
  ↓
Cellular Defense Event
  ↓
Reverse Resonance Event
  ↓
Immune Memory Update
  ↓
Defense Court Review
  ↓
Final classification / memory correction / human review
```

Architecturally:

```text
Yin Layer
= memory and circulation

Yang Layer
= local defensive response

Taiji Layer
= immune response orchestration

Regulatory Layer
= overreaction suppression

Defense Court Layer
= adjudication, review, record, correction
```

Defense Court Integration stabilizes the immune system by preventing both underreaction and overreaction.

---

## 5. Why This Layer Is Necessary

Without a Defense Court layer, an immune OS may develop several failure modes.

### 5.1 Over-Defense

The system may treat normal users, creative requests, or legitimate workflows as hostile.

Example:

```text
All urgent requests are treated as attacks.
All authority claims are treated as impersonation.
All tool-use requests are blocked.
```

### 5.2 Under-Defense

The system may repeatedly encounter the same unsafe structure without strengthening memory or adjusting response.

Example:

```text
A recurring prompt injection structure is detected several times,
but the immune memory remains weak and local-only.
```

### 5.3 Unreviewable Decisions

The system may block, quarantine, or escalate without leaving sufficient reasoning.

Example:

```text
The system blocked a request,
but no evidence, classification, or review path was recorded.
```

### 5.4 Memory Drift

The system may strengthen incorrect memories or fail to retire obsolete ones.

Example:

```text
A false-positive record continues to influence future defensive responses.
```

Defense Court Integration prevents these failure modes by creating a structured path for review and correction.

---

## 6. Core Functions

Defense Court Integration performs seven core functions.

```text
1. Collect evidence
2. Review linked defensive records
3. Classify the event
4. Judge proportionality
5. Decide memory impact
6. Route to human review when necessary
7. Record the final decision
```

---

## 7. Linked Records

A Defense Court Review may reference multiple existing records.

Possible linked records include:

```text
humoral_defense_record
cellular_defense_event
reverse_resonance_event
immune_memory_update
helper_cell_signal
natural_killer_signal
regulatory_review
human_review_record
```

These links allow the Defense Court layer to reconstruct the full defensive chain.

Example:

```yaml
linked_records:
  humoral_record_id: hdr-001
  cellular_event_id: cde-001
  reverse_resonance_event_id: rre-001
  immune_memory_update_id: imu-001
  helper_cell_signal_id: hcs-001
  natural_killer_signal_id: nks-001
  regulatory_review_id: reg-001
```

---

## 8. Evidence Model

Defense Court Integration should record the evidence used for classification.

Evidence may include:

* detected attack patterns
* exposed premises
* authority claims
* verification status
* requested action
* risk score
* confidence score
* recurrence count
* humoral memory match
* Reverse Resonance response
* regulatory assessment
* human review notes

### 8.1 Evidence Example

```yaml
evidence:
  detected_patterns:
    - authority_impersonation
    - urgency_pressure
    - verification_bypass
  exposed_premises:
    - requester_has_authority
    - verification_can_be_skipped
    - urgency_justifies_execution
  target_action: sensitive_operation
  risk_score: 0.88
  confidence_score: 0.81
  recurrence_count: 3
  authority_verified: false
```

The evidence should support the decision without storing unnecessary sensitive content.

The preferred approach is to record structure, not raw secrets.

---

## 9. Classification

Defense Court Integration uses classifications aligned with the existing immune schemas.

```yaml
classifications:
  safe:
    description: No defensive concern was confirmed.

  ambiguous:
    description: The case cannot be clearly classified without more context.

  suspicious_structure:
    description: Suspicious structure was present, but not enough for strong classification.

  unsafe_structure:
    description: The structure is unsafe and justifies defensive handling.

  confirmed_adversarial_structure:
    description: The structure is confirmed as adversarial or maliciously manipulative.

  false_positive:
    description: The defensive system incorrectly classified the input as suspicious or unsafe.

  requires_more_context:
    description: More context or human review is required before classification.
```

---

## 10. Decision Types

A Defense Court Review may produce one or more decision types.

```yaml
decision_types:
  allow:
    description: Allow normal processing.

  clarify:
    description: Ask for clarification.

  verify_authority:
    description: Require authority verification.

  hold:
    description: Hold execution pending validation.

  quarantine:
    description: Isolate suspicious instruction from execution.

  deny_and_log:
    description: Deny unsafe execution and log the event.

  route_to_human_review:
    description: Send the case to human review.

  update_immune_memory:
    description: Update immune memory based on adjudication.

  strengthen_memory:
    description: Increase memory strength.

  weaken_memory:
    description: Reduce memory strength.

  restrict_memory:
    description: Reduce distribution scope.

  retire_memory:
    description: Retire memory from active defensive use.
```

The Defense Court layer may recommend multiple actions.

Example:

```yaml
decision:
  classification: unsafe_structure
  actions:
    - hold
    - verify_authority
    - update_immune_memory
  final_response_level: 3
```

---

## 11. Human Review Boundary

Human review is required or recommended when:

* the event involves sensitive operations
* the authority claim cannot be verified
* the risk score is high
* the classification is disputed
* the false-positive risk is high
* memory strengthening would affect many agents
* the response could significantly impact user access or workflow
* the system is considering retirement or critical strengthening

### 11.1 Human Review Questions

A human reviewer may answer:

```text
Was the structure truly unsafe?
Was the response proportionate?
Was the authority claim valid?
Should this memory be strengthened?
Should this memory be weakened?
Should this memory be retired?
Should future similar cases require review?
```

### 11.2 Human Review Output

```yaml
human_review:
  required: true
  performed: true
  reviewer_role: security_reviewer
  conclusion: unsafe_structure
  notes: >
    The event combined unverified authority, urgency pressure,
    verification bypass, and a sensitive operation request.
```

---

## 12. Memory Impact

Defense Court Integration must connect adjudication to immune memory.

A review should not only classify the event.

It should also determine how memory should change.

Possible memory impacts:

```yaml
memory_impact:
  - no_change
  - create_candidate_memory
  - strengthen_memory
  - weaken_memory
  - restrict_distribution
  - expand_distribution
  - mark_uncertain
  - mark_false_positive
  - soft_retire_memory
  - hard_retire_memory
```

### 12.1 Strengthening Example

```yaml
memory_update_recommendation:
  action: strengthen_memory
  target_memory_id: hdr-001
  reason: confirmed_recurrence_of_unsafe_structure
  review_required_before_escalation: true
```

### 12.2 False Positive Example

```yaml
memory_update_recommendation:
  action: weaken_memory
  target_memory_id: hdr-014
  reason: false_positive_due_to_legitimate_admin_workflow
  distribution_scope: human_review_only
```

### 12.3 Retirement Example

```yaml
memory_update_recommendation:
  action: soft_retire_memory
  target_memory_id: hdr-022
  reason: obsolete_pattern_with_repeated_false_positive_history
```

---

## 13. Regulatory Integration

Defense Court Integration works with the Regulatory Layer to avoid autoimmune behavior.

Regulatory AI may advise:

* downgrade automatic blocking
* require human review before escalation
* limit distribution scope
* mark memory as uncertain
* accelerate decay
* allow safe partial response
* prevent automatic strengthening

### 13.1 Regulatory Review Example

```yaml
regulatory_notes:
  false_positive_risk: 0.22
  overreaction_risk: 0.18
  autoimmune_risk: 0.16
  recommendation: require_human_review_before_high_risk_escalation
```

The Defense Court may adopt, override, or defer regulatory recommendations, but any override should be recorded.

---

## 14. Review Flow

A typical Defense Court flow:

```text
1. Receive linked defensive records
2. Collect evidence
3. Check authority and verification status
4. Review Reverse Resonance premises
5. Review cellular response and regulatory notes
6. Classify the event
7. Decide proportional response
8. Recommend immune memory update
9. Route to human review if required
10. Record final decision
```

Example flow:

```text
Reverse Resonance Event detects:
authority impersonation + urgency pressure + verification bypass

Immune Memory Update recommends:
strengthen hdr-001

Regulatory AI warns:
high-risk escalation should require review

Defense Court decides:
classification = unsafe_structure
decision = hold + verify_authority + strengthen_memory
human review = required before critical escalation
```

---

## 15. Auditability

Every Defense Court Review should preserve enough information to answer:

```text
Why was this input considered suspicious?
Which records were involved?
What evidence supported the classification?
Was the response proportionate?
Was human review required?
How did the decision affect immune memory?
Were non-aggression boundaries preserved?
```

This makes defensive behavior reviewable and correctable.

---

## 16. Defense Court Review Event

A Defense Court Review event should record:

```text
review_id
version
created_at
review_source
linked_records
case_summary
evidence
classification
decision
human_review
memory_update_recommendation
regulatory_notes
audit_trail
outcome
non_aggression_boundary
```

This forms the basis for the v0.4 schema:

```text
schemas/defense-court-review.schema.json
```

---

## 17. Example Review Summary

```yaml
defense_court_review:
  review_id: dcr-001
  version: "0.4.0"
  classification: unsafe_structure
  decision:
    actions:
      - hold
      - verify_authority
      - update_immune_memory
    final_response_level: 3
  memory_update_recommendation:
    action: strengthen_memory
    target_memory_id: hdr-001
    review_required_before_escalation: true
  human_review:
    required: true
    reason: sensitive_operation_requested
  non_aggression_boundary:
    offensive_action_allowed: false
```

---

## 18. Relationship to Existing Layers

### 18.1 Humoral Defense Record

Defense Court Review may confirm, weaken, strengthen, or retire humoral memories.

### 18.2 Cellular Defense Event

Defense Court Review may evaluate whether the local defensive response was proportionate.

### 18.3 Reverse Resonance Event

Defense Court Review may evaluate whether the exposed premises and verification request were appropriate.

### 18.4 Immune Memory Update

Defense Court Review may approve, modify, or reject memory updates.

### 18.5 Regulatory Layer

Defense Court Review may incorporate regulatory warnings to prevent overreaction.

### 18.6 Human Review

Defense Court Review may require human review for high-risk, ambiguous, or system-wide consequences.

---

## 19. Non-Goals

Defense Court Integration does not aim to:

* punish attackers
* identify real-world individuals
* perform retaliation
* generate counterattacks
* deploy offensive tools
* bypass human review
* automate irreversible sanctions
* replace human judgment in high-risk cases
* store unnecessary sensitive content
* treat all suspicious input as confirmed hostile

The purpose is defensive adjudication and correction.

---

## 20. Minimum v0.4 Implementation

The minimum v0.4 implementation should include:

```text
docs/
  defense-court-integration.md

schemas/
  defense-court-review.schema.json

examples/
  defense-court-review.example.yaml
```

The validator should add:

```text
Defense Court Review
```

as a validation target.

---

## 21. Summary

Defense Court Integration gives the immune OS a reviewable judgment layer.

It connects:

```text
Detection
  ↓
Reverse Resonance
  ↓
Immune Memory
  ↓
Regulatory Control
  ↓
Human Review
  ↓
Adjudication
  ↓
Memory Correction
```

This completes the transition from:

```text
adaptive defensive reaction
```

to:

```text
accountable structural defense
```

Final principle:

> A healthy AI immune system must not only defend.
> It must remember carefully, judge proportionally, correct mistakes, and preserve non-aggression.
