import os
import platform

print("🐧 Welcome to my first Linux project!")
print(f"Current User: {os.getlogin()}")
print(f"System: {platform.system()} {platform.release()}")
