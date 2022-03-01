
import ic

private_key_1 = """-----BEGIN PRIVATE KEY-----
MFMCAQEwBQYDK2VwBCIEIGQqNAZlORmn1k4QrYz1FvO4fOQowS3GXQMqRKDzmx9P
oSMDIQCrO5iGM5hnLWrHavywoXekAoXPpYRuB0Dr6DjZF6FZkg==
-----END PRIVATE KEY-----"""

private_key_2 = """-----BEGIN PRIVATE KEY-----
MFMCAQEwBQYDK2VwBCIEIGQqNAZlORmn1k4QrYz1FvO4fOQowS3GXQMqRKDzmx9P
-----END PRIVATE KEY-----"""

i1 = ic.identity.Identity.from_pem(private_key_1)
p = i1.sender()


print(i1.pubkey)
# i2 = ic.identity.Identity.from_pem(private_key_2)
