from pathlib import Path

import click

from . import __version__
from .asset import TARGET_DOCKER_DIR, get_copy_list
from .template import assemble_template, get_post_templates, get_templates
from .templates.settting import DEFAULT_TEMPLATE
from .utils import copy_targets, create_project_dir, write_file


@click.group()
@click.version_option(__version__)
def main():
    """A command line tool to create a new project directory with predefined
    templates.

    Usage: python <script_name> <command> [OPTIONS] [ARGS]...

    Use the --help flag for more information about each command.
    """
    pass


@main.command()
@click.argument("name")
@click.option(
    "-t",
    "--template",
    type=click.Choice(get_templates()),
    help=f"Specify a template for the project (default: {DEFAULT_TEMPLATE}).",
)
@click.option(
    "--full",
    is_flag=True,
    help="Include a full set of files in the project directory (default: False).",
)
@click.option(
    "-p",
    "--post",
    multiple=True,
    type=click.Choice(get_post_templates()),
    help="Include one or more post templates in the project directory.",
)
def new(name, template=None, full=False, post=None):
    """Create a new project directory with predefined templates.

    Usage: python <script_name> new [OPTIONS] <name>

    Arguments:
    <name>        Name of the new project directory to be created.

    Options:
    -t, --template TEXT     Specify a template for the project (default: default).
    --full                  Include a full set of files in the project directory (default: False).
    -p, --post [TEXT]...    Include one or more post templates in the project directory.
    """
    project_dir = create_project_dir(name)
    if project_dir is None:
        return

    copy_targets(get_copy_list(template, project_dir))
    write_file(
        project_dir / TARGET_DOCKER_DIR / "Dockerfile",
        assemble_template(template, full, post),
    )
    print(
        f"Project {name} created. Build the container and get started with:"
        f"\n> cd {name}"
        "\n\n# Build and start the container."
        "\n> python docker.py startd"
        "\n\n# Get into the container."
        "\n> python docker.py"
    )


@main.command()
@click.argument("directory")
@click.option(
    "-t",
    "--template",
    type=click.Choice(get_templates()),
    help=f"Specify a template for the project (default: {DEFAULT_TEMPLATE}).",
)
@click.option(
    "--full",
    is_flag=True,
    help="Include a full set of files in the project directory (default: False).",
)
@click.option(
    "-p",
    "--post",
    multiple=True,
    type=click.Choice(get_post_templates()),
    help="Include one or more post templates in the project directory.",
)
def init(directory=".", template=None, full=False, post=None):
    """Initialize a new project in the target directory with the specified
    options."""
    project_dir = Path(directory).resolve()
    copy_targets(get_copy_list(template, project_dir))
    write_file(
        project_dir / TARGET_DOCKER_DIR / "Dockerfile",
        assemble_template(template, full, post),
    )
    print(
        "Project initialized."
        "\n\n# Build and start the container."
        "\n> python docker.py startd"
        "\n\n# Get into the container."
        "\n> python docker.py"
    )


@main.command()
def ls():
    """List available templates and post templates."""
    get_templates(verbose=True)
    print()
    get_post_templates(verbose=True)


@main.command()
@click.argument(
    "template", type=click.Choice(get_templates()), default="default"
)
@click.option(
    "--full",
    is_flag=True,
    help="Include a full set of files in the project directory (default: False).",
)
@click.option(
    "-p",
    "--post",
    multiple=True,
    type=click.Choice(get_post_templates()),
    help="Include one or more post templates in the project directory.",
)
def use(template, full, post):
    """Use an existing template to replace the current Dockerfile."""
    text = assemble_template(template, full=full, post_templates=post)
    f_dst = Path(".") / TARGET_DOCKER_DIR / "Dockerfile"
    write_file(f_dst, text)
    print(f"Template {template} applied. See {f_dst} for details.")


@main.command()
@click.argument(
    "template", type=click.Choice(get_templates()), default="default"
)
@click.option(
    "--full",
    is_flag=True,
    help="Include a full set of files in the project directory (default: False).",
)
@click.option(
    "-p",
    "--post",
    multiple=True,
    type=click.Choice(get_post_templates()),
    help="Include one or more post templates in the project directory.",
)
def add(template, full, post):
    """Add an existing template with a new Dockerfile with a suffix."""
    text = assemble_template(template, full=full, post_templates=post)
    f_dst = Path(".") / TARGET_DOCKER_DIR / f"Dockerfile.{template}"
    write_file(f_dst, text)
    print(f"Template {template} applied. See {f_dst} for details.")


if __name__ == "__main__":
    main()
