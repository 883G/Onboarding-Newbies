def save_order_to_db(order_data: dict) -> bool:
    """
    Fake database function. 
    In a real app, this would save to Postgres/MongoDB.
    Takes 2 seconds to simulate network latency.
    """
    import time
    time.sleep(2)
    print(f"Order saved to DB: {order_data}")
    return True
