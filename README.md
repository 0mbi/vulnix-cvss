# vulnix-cvss

vulnix-cvss is a small POC for adding a severity score to 
the CVEs that come out of vulnix.

vulnix-cvss reads the CVEs from STDIN and writes
the affected CVEs together with its CVSS to STDOUT: 
Example:

Output of vulnix before:
```
 {
    "name": "some-package-9.9",
    "pname": "some-package",
    "version": "9.9",
    "derivation": "/nix/store/somehash91rhf-some-package-9.9.drv",
    "affected_by": [
      "CVE-1900-08157"
    ],
    "whitelisted": []
  },
```

After piping it into vulnix-cvss:
```
vulnix -j /nix/var/nix/profiles/system | python3 vulnix-cvss.py
```

```
  {
    "name": "some-package-9.9",
    "pname": "some-package",
    "version": "9.9",
    "derivation": "/nix/store/somehash91rhf-some-package-9.9.drv",
    "affected_by": {
      "CVE-1900-08157": 7.5
    },
    "whitelisted": []
  },

```

