from pathlib import Path

from extract import extract_frames, SUPPORTED


def collect_jobs(paths: list[Path]):
    """
    collect encoding jobs from given paths.

    :param paths: list of file or directory paths
    :type paths: list[Path]
    :return: list of (output_path, list of (frames, durations))
    :rtype: list[tuple[Path, list[tuple[list[Image.Image], list[int]]]]]
    """

    has_dir = any(p.is_dir() for p in paths)
    jobs = []

    if not has_dir:
        print("combining mode")
        files = sorted(
            [p for p in paths if p.is_file() and p.suffix.lower() in SUPPORTED],
            key=lambda x: x.name,
        )
        if not files:
            return []

        seqs = [extract_frames(p) for p in files]
        output = files[0].with_suffix(".mp4")
        jobs.append((output, seqs))
        return jobs

    print(f"single mode")
    for p in paths:
        if p.is_dir():
            for f in sorted(p.iterdir(), key=lambda x: x.name):
                if f.is_file() and f.suffix.lower() in SUPPORTED:
                    jobs.append((f.with_suffix(".mp4"), [extract_frames(f)]))
        elif p.is_file() and p.suffix.lower() in SUPPORTED:
            jobs.append((p.with_suffix(".mp4"), [extract_frames(p)]))

    return jobs
