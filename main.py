from FixDispatch import *
from bundle import *

running = True
while running:
    modules = []
    option = input(f"\n1: Fix Dispatch Files \n"
                   f"2: Bundle Module Flavors \n"
                   f"3: Update Config File \n"
                   f"0: Quit\n"
                   f"Select option: ")
    if option == "1":
        print("\n Fixing Dispatch Files")
        print("-" * 30)
        apply_fix()
    elif option == "2":
        print("\n Bundling Modules")
        print("-" * 30)
        bundle()
    elif option == "3":
        print("\n Update Config")
        print("-" * 30)
    elif option == "0":
        print("\n Quiting...")
        running = False
