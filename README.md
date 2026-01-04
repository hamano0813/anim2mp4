# anim2mp4

`anim2mp4` is a small command-line tool that converts animated images  
(`.gif`, `.webp`) into `.mp4` videos.

It is designed to be used via **drag and drop**, with no command-line options.

---

## Usage

### Drag & Drop (Windows)

1. Download `anim2mp4.exe`
2. Drag one or more files or folders onto `anim2mp4.exe`
3. A console window will open and show the progress

No arguments or options are required.

---

## Behavior

### Only files are provided

All files are sorted by filename and merged into **one MP4**.

```text
a.webp
b.webp
c.webp
→ a.mp4
```

The output file name is based on the first image file.

### At least one folder is provided

Each image is converted into its own MP4, using the image filename.

```text
folder/
  a.webp → a.mp4
  b.webp → b.mp4
```

## Supported Formats

* .gif
* .webp

## Dependencies

* Python 3.14
* Pillow
* imageio
* imageio-ffmpeg

## License

* MIT
