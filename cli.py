import click

from cv_data import cv_data


@click.command()
@click.argument('section', type=click.Choice(['personal', 'experience', 'education']))
def display_cv_data(section):
    """
    Command to print CV data in JSON format.
    """
    if section in cv_data:
        data = cv_data[section]
        click.echo(click.style(f"CV {section.capitalize()} Information", fg='blue'))
        if isinstance(data, list):
            for item in data:
                for key, value in item.items():
                    click.echo(f"{key.capitalize()}: {value}")
        else:
            for key, value in data.items():
                click.echo(f"{key.capitalize()}: {value}")
    else:
        click.echo(click.style(f"Section '{section}' not found in CV data.", fg='red'))


if __name__ == '__main__':
    display_cv_data()
