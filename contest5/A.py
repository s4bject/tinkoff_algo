PRIME = 101
MOD = 1000000007

def compute_hashes(s):
    n = len(s)
    hashes = [0] * (n + 1)
    prime_pows = [1] * (n + 1)
    for i in range(n):
        hashes[i + 1] = (hashes[i] * PRIME + ord(s[i])) % MOD
        prime_pows[i + 1] = (prime_pows[i] * PRIME) % MOD
    return hashes, prime_pows

def get_hash(hashes, prime_pows, l, r):
    return (hashes[r] - hashes[l - 1] * prime_pows[r - l + 1]) % MOD

def check_two_subs(hashes, prime_pows, a, b, c, d):
    return get_hash(hashes, prime_pows, a, b) == get_hash(hashes, prime_pows, c, d)

s = input().strip()
m = int(input().strip())
hashes, prime_pows = compute_hashes(s)
for _ in range(m):
    a1, b1, a2, b2 = map(int, input().split())
    print("Yes" if check_two_subs(hashes, prime_pows, a1, b1, a2, b2) else "No")
