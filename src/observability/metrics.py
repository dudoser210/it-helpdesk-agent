from prometheus_client import Counter, Histogram

REQUESTS = Counter("helpdesk_requests_total", "Tickets processed", ["status", "priority"])
AGENT_RUNS = Counter("helpdesk_agent_runs_total", "Agent invocations", ["agent", "status"])
LLM_ERRORS = Counter("helpdesk_llm_errors_total", "LLM call errors", ["agent"])
TOKENS = Counter("helpdesk_tokens_total", "Ollama token counts", ["agent", "kind"])
REQUEST_LATENCY = Histogram("helpdesk_request_duration_seconds", "End-to-end ticket latency")
LLM_LATENCY = Histogram("helpdesk_llm_duration_seconds", "LLM latency", ["agent"])
RETRIEVAL_LATENCY = Histogram("helpdesk_retrieval_duration_seconds", "RAG retrieval latency")
