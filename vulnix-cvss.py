import json
import requests
import sys

# with open('vulnix.json', 'r') as f:
#    data = f.read()
#f.close()
data = sys.stdin.read()
d = json.loads(str(data))
with open('cache.json', 'r') as f:
    cache = f.read()
    f.close()
cache = json.loads(cache)
for k, issue in enumerate(d):
    hmap = {}
    for cve in issue['affected_by']:
        cache_key = "{}:{}".format(issue['name'], cve)
        if cache_key in cache:
            hmap[cve] = cache[cache_key]
        else:
            r = requests.get("http://cve.circl.lu/api/cve/{}".format(cve))
            j = r.json()
            hmap[cve] = j["cvss"]
            cache[cache_key] = j["cvss"]
    d[k]['affected_by'] = hmap
with open('cache.json', 'w') as f:
    f.write(json.dumps(cache))
    f.close()
print(json.dumps(d))
