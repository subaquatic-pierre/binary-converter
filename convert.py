from decimal_to_binary import decimal_to_binary
from binary_to_decimal import binary_to_decimal
import click


@click.command()
@click.option("--decimal", help="Enter decimal number to convert")
@click.option("--binary", help="Enter binary number to convert")
def convert(decimal, binary):
    """ Decimal / Binary converter, enter the value which you would like to convert.
    The program returns either binary or deicaml value
    depending on the option you choose to convert from. """
    if decimal:
        res = decimal_to_binary(int(decimal))
        click.echo(f"{decimal} to binary is {res}")
    elif binary:
        res = binary_to_decimal(str(binary))
        click.echo(f"{binary} to decimal is {res}")


if __name__ == "__main__":
    convert()
