import requests
from windows_toasts import Toast, WindowsToaster
from time import sleep

users = []
oldBodies = {}
newBodies = {}

toaster = WindowsToaster('hjonk')
toast = Toast()

cycle = 1
url = "https://hjonk.me"

with open('users.txt', 'r') as file:
    for line in file:
        users.append(line.strip())
while True:
    for user in users:
        post = requests.get(f"{url}/api/v1.0/posts/{user}?lim=1&page=1")
        for item in post.json():
            if cycle == 1:
                newBodies[user] = item["body"]
                oldBodies[user] = newBodies[user]
            else:
                oldBodies[user] = newBodies[user]
                newBodies[user] = item["body"]
            toast.text_fields = [f"@{user}", newBodies[user]]
            toast.launch_action = f"{url}/@{user}"
            if newBodies[user] != oldBodies[user] or cycle == 1:
                toaster.show_toast(toast)
        print(f"@{user}: {oldBodies[user]}")

    cycle = cycle + 1
    sleep(300)