muppets = [
    {"name": "Kermit the Frog", "location": "The swamp. I'm a frog."},
    {"name": "Miss Piggy", "location": "The green room. Where's my champagne?"},
    {"name": "Fozzie Bear", "location": "The Comedy Store - tonight at 8!"},
    {"name": "Gonzo the Great", "location": "Waiting to be shot out of a cannon."},
]

for muppet in muppets:
    for key, value in muppet.items():
        print(key, value)
