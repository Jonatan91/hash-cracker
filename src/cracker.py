import hashlib
from typing import Optional, Callable

# Map simple algo names to hashlib constructors
SUPPORTED = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    # Optional: allow stronger algos to show the difference
    "sha256": hashlib.sha256,
}

def get_hasher(algo: str) -> Callable[[], "hashlib._Hash"]:
    """
    Return a hashlib constructor for the given algo name.
    Raises ValueError if the algorithm is not supported.
    """
    key = algo.lower()
    if key not in SUPPORTED:
        raise ValueError(f"Unsupported algorithm: {algo}. Supported: {', '.join(SUPPORTED.keys())}")
    return SUPPORTED[key]

def normalize_hex(h: str) -> str:
    """
    Normalize a hex digest: strip spaces, lowercase.
    """
    return h.strip().lower()

def crack_hash(target_hex: str, algo: str, wordlist_path: str, max_lines: Optional[int] = None) -> Optional[str]:
    """
    Try to recover the original password for a given hex digest using
    a dictionary (wordlist) attack. Returns the matching plaintext
    if found, otherwise None.

    - target_hex: hex digest to crack, e.g., MD5('password') = 5f4dcc3b...
    - algo: 'md5', 'sha1' (or 'sha256' optionally)
    - wordlist_path: file with candidate passwords (one per line)
    - max_lines: optional cap to stop early for safety
    """
    target_hex = normalize_hex(target_hex)
    hasher_ctor = get_hasher(algo)

    count = 0
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if max_lines is not None and count >= max_lines:
                break
            pwd = line.rstrip("\r\n")
            if not pwd:
                continue

            # Compute digest for this candidate
            h = hasher_ctor()
            h.update(pwd.encode("utf-8", errors="ignore"))
            digest = h.hexdigest()

            if digest == target_hex:
                return pwd

            count += 1

    return None
