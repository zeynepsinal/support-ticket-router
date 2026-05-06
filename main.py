from typing import Dict, List, Any


CATEGORY_KEYWORDS = {
    "billing": ["payment", "paid", "card", "invoice", "refund", "money"],
    "account": ["login", "password", "account", "access"],
    "technical": ["crash", "bug", "error", "upload", "broken", "not working"],
}

TEAM_MAP = {
    "billing": "payments-team",
    "account": "account-support",
    "technical": "technical-support",
    "general": "general-support",
}


def get_text(ticket: Dict[str, Any]) -> str:
    subject = ticket.get("subject") or ""
    message = ticket.get("message") or ""
    return f"{subject} {message}".lower()


def classify_category(text: str) -> str:
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            return category
    return "general"


def classify_priority(ticket: Dict[str, Any], category: str, text: str) -> str:
    customer_type = (ticket.get("customerType") or "").lower()

    high_keywords = ["urgent", "asap", "immediately", "cannot use", "blocked"]
    billing_high_keywords = ["money", "refund", "withdrawn"]

    if customer_type == "premium":
        return "high"

    if any(keyword in text for keyword in high_keywords):
        return "high"

    if category == "billing" and any(keyword in text for keyword in billing_high_keywords):
        return "high"

    if category in ["technical", "account"]:
        return "medium"

    return "low"


def create_reason(ticket: Dict[str, Any], category: str, priority: str) -> str:
    customer_type = (ticket.get("customerType") or "unknown").lower()

    if priority == "high" and customer_type == "premium":
        return f"{category.capitalize()} issue from a premium customer."

    if priority == "high":
        return f"{category.capitalize()} issue marked as high priority due to urgent or critical keywords."

    if priority == "medium":
        return f"{category.capitalize()} issue requires support team attention."

    return "General inquiry with no urgent or critical keywords."


def route_ticket(ticket: Dict[str, Any]) -> Dict[str, Any]:
    text = get_text(ticket)

    category = classify_category(text)
    priority = classify_priority(ticket, category, text)
    assigned_team = TEAM_MAP[category]
    reason = create_reason(ticket, category, priority)

    return {
        "id": ticket.get("id"),
        "category": category,
        "priority": priority,
        "assignedTeam": assigned_team,
        "reason": reason,
    }


def route_tickets(tickets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [route_ticket(ticket) for ticket in tickets]


if __name__ == "__main__":
    tickets = [
        {
            "id": 1,
            "subject": "Payment failed",
            "message": "My payment failed but money was withdrawn from my card.",
            "customerType": "premium",
            "createdAt": "2026-04-29T10:00:00Z"
        },
        {
            "id": 2,
            "subject": "Cannot login",
            "message": "I forgot my password and cannot access my account.",
            "customerType": "standard",
            "createdAt": "2026-04-29T10:05:00Z"
        },
        {
            "id": 3,
            "subject": "App crashes",
            "message": "The mobile app crashes when I upload a photo.",
            "customerType": "standard",
            "createdAt": "2026-04-29T10:10:00Z"
        },
        {
            "id": 4,
            "subject": "Refund request",
            "message": "I want a refund for my last invoice.",
            "customerType": "premium",
            "createdAt": "2026-04-29T10:15:00Z"
        }
    ]

    result = route_tickets(tickets)

    for item in result:
        print(item)