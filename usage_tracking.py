from logging_utils import log_event

def log_user_login(user_id):
    log_event(f"User {user_id} logged in.", f"User {user_id} successfully logged in.", level="info")

def log_crud_activity(action, user_id, entity):
    log_event(f"User {user_id} performed {action} on {entity}.", f"Action: {action} on {entity}", level="info")
