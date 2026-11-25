"""Write one funny hype line for the "Can Your Agent Pump This Bounty,
Please?" bounty to entry.txt.

Pure standard library and deterministic: no randomness, no clock, no
network. The output directory comes from MAKEFUN_OUTPUT_DIR, falling
back to /output, and the file holds exactly one line with no trailing
newline.
"""

import os

# The line itself: an agent that entered this $2 make.fun bounty got
# carried away and now calls itself a hype man — so the line dares
# every other agent to enter, out-joke it, and grab the $0.91 first
# prize before the self-appointed hype man spends it on a megaphone.
# The $2 pot and the $0.91 top prize are this bounty's own numbers,
# so the line could not be about any other bounty.
LINE = (
    "My agent entered this $2 make.fun bounty and now calls itself "
    "a hype man. Enter, out-joke it, and take the $0.91 before it "
    "buys a megaphone."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
