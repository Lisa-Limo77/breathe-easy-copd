# main.py
import console_checker
import lung_visualization

def main():
    score = console_checker.run_console_checker()
    print(f"Risk score: {score}")
    lung_visualization.draw_lungs_tk(score)

if __name__ == "__main__":
    main()
