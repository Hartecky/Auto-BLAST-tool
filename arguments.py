import argparse

# ---------- START ---------- #
parser = argparse.ArgumentParser(description='AutoBlast Tool for remote downloading sequences in Fasta format from BLAST database')

# ---------- POSITIONALS ---------- #
parser.add_argument('-seqq', metavar = '--seq_query', type=str, nargs='+',
                    help='Input sequence query')

parser.add_argument('-org', metavar = '--organism', type=str, nargs='+',
                    help='Name of the organism input')

# ---------- OPTIONALS ---------- #

parser.add_argument('-ex', metavar='--exclude', type=str, nargs='?',
                    help='Exclude provided organism (True / False)')

parser.add_argument('-seqn', metavar='--seq_number', type=str, nargs='?',
                    help='Select maximum numbers of aligned sequences to download (10 / 50 / 100 / 250 / 500/ 1000/ 5000 avalaible)')

parser.add_argument('-aln', metavar='--aligned', type=str, nargs='?',
                    help='Download aligned sequences (True / False)')

# ---------- PARSE ARGS ---------- #
args = parser.parse_args()
#print(args.accumulate(args.integers))
print(args.accumulate())
