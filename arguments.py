import argparse

def string_to_bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def parse_arguments():
    # ---------- START ---------- #
    parser = argparse.ArgumentParser(description='Remote sequence downloader from NCBI Nucleotide Blast database')

    # ---------- Optionals ---------- #
    group = parser.add_mutually_exclusive_group()

    group.add_argument('-e', '--exclude', type=string_to_bool, metavar='', required=False, help='Exclude provided organism (True / False)')
    group.add_argument('-n', '--number_seq', type=str, metavar='', required=False, help='Select maximum numbers of aligned sequences to download (10 / 50 / 100 / 250 / 500/ 1000/ 5000 avalaible)')
    group.add_argument('-a', '--aligned', type=str, metavar='', required=False, help='Download aligned sequences (True / False)')
    group.add_argument('-out', '--output', type=str, metavar='', required=False, help='Output file name (seqdump.txt by default)')
    # ---------- required ---------- #
    required = parser.add_argument_group('required arguments')
    required.add_argument('-q', '--query', type=str, metavar='', required=True, help='Nucleotide sequence query')
    required.add_argument('-o', '--organism', type=str, metavar='', required=True, help='Name of the organism input')

    # ---------- PARSE ARGS ---------- #
    args = parser.parse_args()

    return args

