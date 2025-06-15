# main.py
import console
import graphics

def main():
    score = console.run_console_checker()
    print(f"Risk score: {score}")
    graphics.draw_lungs_tk(score)

if __name__ == "__main__":
    main()
