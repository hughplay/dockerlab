from pathlib import Path

MAX_CHUNK_SIZE = 4096
PROJECT_DIR = Path(__file__).parent.resolve()


def create_project_dir(name):
    project_dir = Path(name).resolve()
    if project_dir.exists():
        print(f"Path {project_dir} already exists.")
        project_dir = None
    else:
        project_dir.mkdir()

    return project_dir


def copy_targets(copy_list):
    for src, dst in copy_list:
        copy_target(src, dst)


def copy_target(src, dst):
    if dst.exists() and not is_content_equal(src, dst):
        print(
            f"File {dst} already exists and is different from the template. "
            "Overwrite (o), merge (m) or skip (s)?"
        )
        while True:
            value = input("(o/m/s) [o]: ")
            if value == "o" or value == "":
                dst.unlink()
                copy_file(src, dst)
            elif value == "m":
                merge_file(src, dst)
            elif value == "s":
                print(f"Skipping {dst}")
            else:
                continue
            break
    else:
        copy_file(src, dst)


def copy_file(f_src, f_dst):
    if not f_dst.parent.exists():
        f_dst.parent.mkdir(parents=True)
    with open(f_src, "rb") as src, open(f_dst, "wb") as dst:
        dst.write(src.read())


def merge_file(f_src, f_dst):
    with open(f_src, "r") as src, open(f_dst, "r+") as dst:
        src_lines = src.readlines()
        dst_lines = dst.readlines()
        dst_lines += [
            line
            for line in src_lines
            if line not in dst_lines and line.strip() != ""
        ]
        dst.seek(0)
        dst.writelines(dst_lines)


def write_file(f_dst, text):
    if f_dst.exists():
        value = input(
            f"File {f_dst} already exists. Overwrite (o) or skip (s)? [o]: "
        )
        if value != "o" and value != "":
            return
    f_dst.parent.mkdir(parents=True, exist_ok=True)
    with open(f_dst, "w") as dst:
        dst.write(text)


def is_content_equal(f1, f2):
    with open(f1, "rb") as f1, open(f2, "rb") as f2:
        while True:
            chunk1 = f1.read(MAX_CHUNK_SIZE)
            chunk2 = f2.read(MAX_CHUNK_SIZE)
            if chunk1 != chunk2:
                return False
            if not chunk1:
                break
    return True
