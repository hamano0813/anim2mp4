from pathlib import Path

import imageio.v3 as iio


def encode_mp4(seqs, output: Path):
    frames = []
    durations = []

    for f, d in seqs:
        frames.extend(f)
        durations.extend(d)

    if not frames:
        raise ValueError("No frames to encode")

    avg = sum(durations) / len(durations)
    fps = max(1, round(1000 / avg))

    iio.imwrite(
        output,
        frames,
        fps=fps,
        codec="libx264",
        quality=10,
        pixelformat="yuv420p",
        macro_block_size=1,
        ffmpeg_params=[
            "-preset",
            "slow",
            "-crf",
            "18",
            "-profile:v",
            "high",
            "-level",
            "5.1",
            "-movflags",
            "+faststart",
            "-x264opts",
            "ref=3:mixed-refs=1:analyse=all:me=umh:no-fast-pskip=1",
        ],
    )
