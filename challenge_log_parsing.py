# elirazo96
import re
from datetime import datetime

# Sample log input from the user
log_sample = input("Enter the log sample: ")

# regex pattern
log_pattern = r'\[(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})\] \[([A-Z]+)\] \[(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\] \[([^\]]+)\] \[User: ([^\]]+)\] \[Resource: ([^\]]+)\]'

# Parse the log sample using regex
match = re.match(log_pattern, log_sample)

if match:
    timestamp, log_level, ip_address, event_id, user, resource = match.groups()
    
    # Convert the timestamp to a more readable format
    dt = datetime.fromisoformat(timestamp)
    formatted_timestamp = dt.strftime("%B %d, %Y, %I:%M:%S %p")
    
    # Print the parsed and formatted data
    print(f"Timestamp: {formatted_timestamp}")
    print(f"Log Level: {log_level}")
    print(f"IP Address: {ip_address}")
    print(f"Event ID: {event_id}")
    print(f"User: {user}")
    print(f"Resource: {resource}")
else:
    print("Log sample does not match the expected format.")
