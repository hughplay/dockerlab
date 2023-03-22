from pathlib import Path

from .template import resolve_template
from .templates.settting import TEMPLATE_SETTING

# these files will be copied to the root of the project directory
# other files will be copied to the docker directory
DEFAULT_ROOT_FILES = [
    "docker-compose.yml",
    "docker.py",
    ".gitignore",
]
ASSETS_DIR = Path(__file__).parent.resolve() / "assets"
TARGET_DOCKER_DIR = "docker"


def get_copy_list(template, target_dir):
    template = resolve_template(template)
    target_dir = Path(target_dir).resolve()

    copy_list = []
    for target in DEFAULT_ROOT_FILES:
        copy_list.extend(
            list(unfold_src_target(ASSETS_DIR / target, target_dir / target))
        )
    extra_assets = TEMPLATE_SETTING[template].get("assets", [])
    for target in extra_assets:
        copy_list.extend(
            list(
                unfold_src_target(
                    ASSETS_DIR / target, target_dir / TARGET_DOCKER_DIR / target
                )
            )
        )

    return copy_list


def unfold_src_target(src, target):
    if src.is_dir():
        for child in src.iterdir():
            yield from unfold_src_target(child, target / child.name)
    else:
        yield src, target
