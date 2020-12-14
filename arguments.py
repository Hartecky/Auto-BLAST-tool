import argparse

def string_to_bool(value):

    """
    Checks if converted string has the bool meaning

    Parameters:
    value: string provided by user
    """
    if isinstance(value, bool):
       return value
    if value.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif value.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def parse_arguments():

    """
    Parses and operates on arguments through the command line
    """

    # ---------- START ---------- #
    parser = argparse.ArgumentParser(description='Remote sequence downloader from NCBI Nucleotide Blast database')

    # ---------- required ---------- #
    required = parser.add_argument_group('required arguments')

    # query input sequence
    required.add_argument('-q',
                          '--query',
                          type=str,
                          metavar='',
                          help='Nucleotide sequence query')

    # organism output sequence
    required.add_argument('-o',
                          '--organism',
                          type=str,
                          metavar='',
                          help='Name of the organism input')

    # ---------- additionals ---------- #
    #group = parser.add_mutually_exclusive_group()

    # Exclude option
    required.add_argument('-e', '--exclude',
                       type=string_to_bool,
                       metavar='',
                       required=False,
                       help='Exclude provided organism (False by default)')

    # Target sequences
    required.add_argument('-n', '--num_seq',
                       type=str,
                       metavar='',
                       required=False,
                       choices=['10','50','100','250','500','1000','5000'],
                       help='Select sequence search target to download (100 by default)')

    # Alignment option
    required.add_argument('-a', '--align',
                       type=str,
                       metavar='',
                       required=False,
                       choices=['aligned', 'complete'],
                       help='Download aligned or complete sequences (aligned by default)')

    # Output file name
    required.add_argument('-out', '--output',
                       type=str,
                       metavar='',
                       required=False,
                       help='Output file name (output.txt by default)')


    # ---------- PARSE ARGS ---------- #
    args = parser.parse_args()

    return args

