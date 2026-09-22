# Closing Card & Directive Prompt Templates

Per SKILL.md Rules 20–21: every study ends with a directive closing question (a real Question, tagged) followed by a warm thank-you card (display-only, NOT a Question).

## Directive closing prompt (Question, VERBAL RESPONSE)

Never generic ("Any final thoughts?"). Ask 2–3 specific things. ~60 sec budget.

**Default:**
```
### Question Q[N] — VERBAL RESPONSE

**Verbal response:**
What could we improve about this experience? What would make this process easier for you? Was there anything you didn't like, or any features you wished worked differently? (~60 sec)

Please give a verbal response.

> **USERTESTING QUESTION TYPE: VERBAL RESPONSE** (NOT Written response).
```

**Alternate — feature/signal-specific study (e.g., a badge, label, or warning under test):**
```
What could we improve about how [the feature] works? What would make it easier to trust or understand? Was there anything about the wording or placement you didn't like, or wish worked differently? (~60 sec)
```

**Alternate — comparison study (participant saw 2+ variants):**
```
Thinking across everything you just saw, what would you change first? What's the one thing that would make the biggest difference for you? (~60 sec)
```

Pick one; don't stack multiple directive closings in the same study — one directive question is enough signal and avoids fatigue at the point where attention is lowest.

## Warm thank-you closing card (display-only)

**Default:**
```
Thank you so much for taking the time to share your thoughts with us today. Your feedback is incredibly helpful and will directly shape how we improve this experience. We really appreciate you.
```

**Alternate — shorter, for a tightly-timed unmoderated study:**
```
Thanks so much for your time today — this was genuinely helpful and will shape what we build next. We appreciate you.
```

**Alternate — panel/repeat-participant studies (signals continuity):**
```
Thank you for taking the time to share your thoughts with us today. Feedback like yours directly shapes what we build — we really appreciate you, and hope to have you back for future studies.
```

❌ Never: "Thank you for completing this study." (reads as a form-completion receipt, not a thank-you)

Mark the closing card display-only in the Output structure — it is never tagged as a Question (Rule 4).
