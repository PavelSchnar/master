from utils import show_sales
import sys

if len(sys.argv) == 2:
    command1 = int(sys.argv[1])
    show_sales(command1)

elif len(sys.argv) == 3:
    command1 = int(sys.argv[1])
    command2 = int(sys.argv[2])
    show_sales(command1, command2)

elif len(sys.argv) == 1:
    show_sales()
