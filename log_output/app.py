import time
import uuid
from datetime import datetime, timezone

# 1. Generate random string on startup and store in memory
random_string = str(uuid.uuid4())

print(f"Application started. String for this session: {random_string}\n")

# 2. Loop forever
while True:
    # 3. Get timestamp in ISO 8601 format with milliseconds and 'Z'
    # This format matches your example exactly.
    timestamp = datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z')
    
    # 4. Output the string
    print(f"{timestamp}: {random_string}")
    
    # 5. Wait 5 seconds
    time.sleep(5)