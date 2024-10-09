import time
import notify2

# Initialize the notifier
notify2.init("App Name")

# Create a notification object
n = notify2.Notification("Title", "Message")

# Set the urgency level (Low, Normal, Critical)
n.set_urgency(notify2.URGENCY_NORMAL)

# Set the timeout (in seconds)
n.set_timeout(5000)

# Show the notification
n.show()

# Wait for 5 seconds
time.sleep(5)

# Close the notification
n.close()