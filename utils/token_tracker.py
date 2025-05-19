# token_tracker.py
# Tracks TOL token rewards per contributor or user ID

rewards = {}

def reward_user(user_id: str, amount: float):
    rewards[user_id] = rewards.get(user_id, 0.0) + amount
    return rewards[user_id]

def get_user_total(user_id: str) -> float:
    return rewards.get(user_id, 0.0)
