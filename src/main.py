import argparse
import time
from cracker import crack_hash, SUPPORTED

def parse_args():
    """
    Command-line interface to crack a hash using a wordlist.
    """
    parser = argparse.ArgumentParser(description="Dictionary-based hash cracker (educational).")
    parser.add_argument("--hash", required=True, help="Target hex digest to crack")
    parser.add_argument("--algo", choices=list(SUPPORTED.keys()), default="md5",
                        help="Hash algorithm (default: md5)")
    parser.add_argument("--wordlist", required=True, help="Path to wordlist file")
    parser.add_argument("--max-lines", type=int, default=None,
                        help="Optional limit of lines to try from the wordlist")
    parser.add_argument("--quiet", action="store_true",
                        help="Do not print status; only final result")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    start = time.time()
    pwd = crack_hash(args.hash, args.algo, args.wordlist, args.max_lines)
    elapsed = time.time() - start

    if not args.quiet:
        print(f"[*] Algo       : {args.algo}")
        print(f"[*] Wordlist   : {args.wordlist}")
        print(f"[*] Max lines  : {args.max_lines if args.max_lines is not None else 'all'}")

    if pwd is not None:
        print(f"[+] Match found! Password = {pwd}")
    else:
        print("[!] No match found in the provided wordlist.")

    if not args.quiet:
        print(f"[*] Elapsed    : {elapsed:.2f}s")
