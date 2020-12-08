import argparse


def parse_arguments():
    # ---------- START ---------- #
    parser = argparse.ArgumentParser(description='Remote sequence downloader from NCBI Nucleotide Blast database')

    # ---------- POSITIONALS ---------- #
    parser.add_argument('-q', '--query', type=str, metavar='', required=True, help='Nucleotide sequence query')

    parser.add_argument('-o', '--organism', type=str, metavar='', required=True, help='Name of the organism input')

    # ---------- OPTIONALS ---------- #
    group = parser.add_mutually_exclusive_group()

    group.add_argument('-e', '--exclude', type=str, metavar='', required=False, help='Exclude provided organism (True / False)')

    group.add_argument('-n', '--number_seq', type=str, metavar='', required=False, help='Select maximum numbers of aligned sequences to download (10 / 50 / 100 / 250 / 500/ 1000/ 5000 avalaible)')

    group.add_argument('-a', '--aligned', type=str, metavar='', required=False, help='Download aligned sequences (True / False)')

    # ---------- PARSE ARGS ---------- #
    args = parser.parse_args()

    return args


