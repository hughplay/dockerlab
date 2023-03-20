from pathlib import Path

import click

from .template import assemble_template, get_post_templates, get_templates
from .utils import FILES, copy_target, create_project_dir, write_file


@click.group()
def main():
    pass


@main.command()
@click.argument("name")
@click.option(
    "-t", "--template", type=click.Choice(get_templates()), default="default"
)
@click.option("--full", is_flag=True)
@click.option(
    "-p", "--post", multiple=True, type=click.Choice(get_post_templates())
)
def new(name, template="default", full=False, post=None):
    project_dir = create_project_dir(name)
    if project_dir is None:
        return
    for target in FILES:
        copy_target(project_dir, target)
    write_file(
        project_dir / "docker" / "Dockerfile",
        assemble_template(template, full, post),
    )


@main.command()
@click.argument("directory")
@click.option(
    "-t", "--template", type=click.Choice(get_templates()), default="default"
)
@click.option("--full", is_flag=True)
@click.option(
    "-p", "--post", multiple=True, type=click.Choice(get_post_templates())
)
def init(directory=".", template="default", full=False, post=None):
    project_dir = Path(directory).resolve()
    for target in FILES:
        copy_target(project_dir, target)
    write_file(
        project_dir / "docker" / "Dockerfile",
        assemble_template(template, full, post),
    )


@main.command()
def ls():
    get_templates(verbose=True)
    print()
    get_post_templates(verbose=True)


@main.command()
@click.argument(
    "template", type=click.Choice(get_templates()), default="default"
)
@click.option("--full", is_flag=True)
@click.option(
    "-p", "--post", multiple=True, type=click.Choice(get_post_templates())
)
def use(template, full, post):
    text = assemble_template(template, full=full, post_templates=post)
    f_dst = Path(".") / "docker" / "Dockerfile"
    write_file(f_dst, text)
    print(f"Template {template} applied. See {f_dst} for details.")


@main.command()
@click.argument(
    "template", type=click.Choice(get_templates()), default="default"
)
@click.option("--full", is_flag=True)
@click.option(
    "-p", "--post", multiple=True, type=click.Choice(get_post_templates())
)
def add(template, full, post):
    text = assemble_template(template, full=full, post_templates=post)
    f_dst = Path(".") / "docker" / f"Dockerfile.{template}"
    write_file(f_dst, text)
    print(f"Template {template} applied. See {f_dst} for details.")


if __name__ == "__main__":
    main()
