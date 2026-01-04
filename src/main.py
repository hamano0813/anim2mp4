import sys
from pathlib import Path
from collect import collect_jobs
from encode import encode_mp4


def main():
    if len(sys.argv) < 2:
        print("usage: python main.py <file_or_directory> [<file_or_directory> ...]")
        return

    paths = [Path(p) for p in sys.argv[1:]]
    jobs = collect_jobs(paths)

    if not jobs:
        print("no jobs to process")
        return

    for idx, (output, seqs) in enumerate(jobs, 1):
        print(f"[{idx}/{len(jobs)}] generating {output.name}")
        encode_mp4(seqs, output)


if __name__ == "__main__":
    main()
    input("finish! press Enter to exit...")
