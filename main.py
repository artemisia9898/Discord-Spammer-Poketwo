from webserver import keep_alive
import requests

channelID = 1116394692372877384
headers = {
    "authorization":
    "MTExNjM3NDU4OTg4MzI4OTYxMA.G4a-KT.hT_ODkpgCeBu2fDzW-2pB5lXr7ik8CsD1DRtDQ"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
