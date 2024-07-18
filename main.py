from datetime import datetime

# Get current date and time
current_datetime = datetime.now()

# Format the current datetime as desired
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

# Print the formatted datetime
print("Current Date and Time:", formatted_datetime)