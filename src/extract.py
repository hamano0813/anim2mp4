from pathlib import Path

from PIL import Image, ImageSequence

SUPPORTED = {".gif", ".webp"}


def extract_frames(path: Path) -> tuple[list[Image.Image], list[int]]:
    """
    extract frames and their durations from an image file.

    :param path: image file path
    :type path: Path
    :return: (frames, durations)
    :rtype: tuple[list[Image.Image], list[int]]
    """
    if path.suffix.lower() not in SUPPORTED:
        raise ValueError(f"Unsupported format: {path.suffix}")

    print(f"extracting frames from {path.name}")
    frames = []
    durations = []

    with Image.open(path) as img:
        for frame in ImageSequence.Iterator(img):
            frames.append(frame.convert("RGB").copy())
            durations.append(frame.info.get("duration", 100))

    return frames, durations
