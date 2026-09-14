

# if log is a file, read and parse each line and convert each line to a string
# consider that line as below
log_line = "2026-09-14 10:15:30 [INFO] UserID:10294 Action:PURCHASE Amount:250.50"



def parse_log_line(log_line):
    # Split the log line into a list separaed by spaces as each item
    parts = log_line.split(" ")
    
    # Extract the timestamp
    timestamp = parts[0] + " " + parts[1]
    
    # Extract the log level , trims the leading and trailing brackets
    log_level = parts[2].strip("[]")
    
    # Extract the user ID value 
    user_id = parts[3].split(":")[1]
    
    # Extract the action value
    action = parts[4].split(":")[1]
    
    # Extract the amount value
    amount = float(parts[5].split(":")[1])
    
    return {
        "timestamp": timestamp,
        "log_level": log_level,
        "user_id": user_id,
        "action": action,
        "amount": amount
    }
  