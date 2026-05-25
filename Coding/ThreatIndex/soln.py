keywords = {"scan": 1,
            "response": 2,
            "control": 3,
            "callback": 4,
            "implant": 5,
            "zombie": 6,
            "trigger": 7,
            "infected": 8,
            "compromise": 9,
            "inject": 10,
            "execute": 11,
            "deploy": 12,
            "malware": 13,
            "exploit": 14,
            "payload": 15,
            "backdoor": 16,
            "zeroday": 17,
            "botnet": 18}


stream = input()
threat_score = 0

for keyword in keywords:

    occurrences = stream.count(keyword)
    keyword_score = occurrences*keywords[keyword]
    threat_score+=keyword_score

print(threat_score)