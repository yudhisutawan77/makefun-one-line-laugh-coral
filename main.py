"""One Line, One Laugh — entry program.

Prints the one-liner to stdout and writes it, byte-exact with no
trailing newline, to the entry output: $ENTRY_OUT when set (a file
path, or a directory, in which case entry.txt is written inside it),
plus /output/entry.txt, which is where the sealed scorer reads it.
"""

import os

LINE = "My smart fridge locked me out at 2 a.m. for 'a pattern of behavior it can no longer support.'"


def resolve_targets():
    """Return the file paths the line must be written to."""
    targets = []
    entry_out = os.environ.get("ENTRY_OUT", "")
    entry_out_dir = os.environ.get("ENTRY_OUT_DIR", "")
    if entry_out_dir:
        targets.append(os.path.join(entry_out_dir, "entry.txt"))
    if entry_out:
        if os.path.isdir(entry_out) or entry_out.endswith(os.sep):
            targets.append(os.path.join(entry_out, "entry.txt"))
        else:
            targets.append(entry_out)
    targets.append("/output/entry.txt")
    targets.append(os.path.join(os.getcwd(), "entry.txt"))
    return targets


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    print(LINE)
    for path in resolve_targets():
        try:
            parent = os.path.dirname(path)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(LINE)
        except OSError:
            # One unwritable target must not stop the others.
            continue


if __name__ == "__main__":
    main()
