## 🛡️ Guardrails in OpenAI SDK 

Guardrails in OpenAI SDK are safety rules or checkers.

- **Input guardrails** check the user’s question first. If it’s safe, the agent continues.
- **Output guardrails** then check the agent’s reply. If something unsafe was missed, it will stop the agent from answering.
- These guardrails act like a safety block around the AI to stop anything unsafe or harmful.

➡️ Guardrails make sure both the question and the answer are safe **before anything is shown to the user**.

### ✅ Summary:
Guardrails work like filters.  
They watch both the question and the answer to make sure nothing unsafe is allowed.  
If anything looks harmful or restricted, the agent stops automatically.