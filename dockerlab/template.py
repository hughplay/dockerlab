from pathlib import Path
from typing import List

TEMPLATES_DIR = Path(__file__).parent.resolve() / "templates"
POST_TEMPLATES_DIR = Path(__file__).parent.resolve() / "post_templates"
OFFICIAL_HUB = "deepbase/dockerlab"
DEFAULT_POST_TEMPLATES = {
    "workspace_cuda_11_1": ["python", "default"],
    "workspace_cuda_11_7": ["python", "default"],
    "workspace_pytorch_1_13": ["python", "default"],
    "workspace_pytorch_2_0": ["python", "default"],
}


def get_templates(verbose=False):
    templates = [
        (t.name, t)
        for t in TEMPLATES_DIR.iterdir()
        if t.is_dir() or t.is_symlink()
    ]
    templates.sort(key=lambda x: (not x[1].is_symlink(), x[0]))
    if verbose:
        print("Available templates:")
        for name, t in templates:
            if t.is_symlink():
                print(f"  - {name} -> {t.resolve().name}")
            else:
                print(f"  - {name}")
    return [name for name, _ in templates]


def get_post_templates(verbose=False):
    # iterate files with .txt extension
    templates = [
        t.stem
        for t in POST_TEMPLATES_DIR.iterdir()
        if t.is_file() and t.suffix == ".txt"
    ]
    if verbose:
        print("Available post templates:")
        for t in templates:
            print(f"  - {t}")
    return templates


def assemble_template(
    tag: str, full: bool = False, post_templates: List[str] = None
):
    if tag == "default":
        real_temp_dir = (TEMPLATES_DIR / "default").resolve()
        tag = real_temp_dir.name

    templates = get_templates()
    if tag not in templates:
        raise ValueError(f"Template {tag} not found.")
    temp = TEMPLATES_DIR / tag / "Dockerfile"
    temp_text = temp.read_text().strip()

    if full:
        temp_text = extend_template(temp_text, templates)

    if post_templates is None or len(post_templates) == 0:
        post_templates = DEFAULT_POST_TEMPLATES.get(tag, [])

    for post in post_templates:
        post_temp = POST_TEMPLATES_DIR / f"{post}.txt"
        post_temp_text = post_temp.read_text().strip()
        temp_text += "\n" * 3 + post_temp_text

    temp_text = (
        f"# dockerlab template: {tag}"
        + (" (full)" if full else "")
        + "\n# https://github.com/hughplay/dockerlab"
        + "\n\n"
        + temp_text
    )

    return temp_text


def extend_template(temp_text, templates):
    for line in temp_text.splitlines():
        if line.upper().startswith("FROM"):
            base_image = line.split()[1]
            project, tag = base_image.split(":")
            if project == OFFICIAL_HUB and tag in templates:
                ext_temp = TEMPLATES_DIR / tag / "Dockerfile"
                ext_temp_text = ext_temp.read_text().strip()
                temp_text = (
                    ext_temp_text + "\n\n# " + "-" * 80 + "\n# " + temp_text
                )
                temp_text = extend_template(temp_text, templates)
            break
    return temp_text
