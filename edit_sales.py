from utils import edit_sales
import sys

if len(sys.argv) == 3:
    command1 = int(sys.argv[1])
    command2 = float(sys.argv[2])
    edit_sales(command1, command2)
