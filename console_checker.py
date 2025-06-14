def run_console_checker():
    print("🫁 Welcome to Breathe-Easy Console!\n")
    
    cough = input("Do you often experience chronic cough? (yes/no): ").strip().lower()
    breathless = input("Do you feel breathless during light activities? (yes/no): ").strip().lower()
    smoking = input("Do you smoke or have a history of smoking? (yes/no): ").strip().lower()

    risk_score = 0
    if cough == "yes":
        risk_score += 1
    if breathless == "yes":
        risk_score += 1
    if smoking == "yes":
        risk_score += 1

    if risk_score == 3:
        print("⚠️ High Risk: You may be at risk of COPD.")
    elif risk_score == 2:
        print("⚠️ Moderate Risk: Watch your respiratory health.")
    else:
        print("✅ Low Risk: Keep taking care of your lungs!")

    print("\n💡 Lung Health Tips:")
    print("- Avoid smoking and secondhand smoke.")
    print("- Exercise regularly.")
    print("- Avoid air pollution when possible.")
    print("- Stay hydrated and eat healthy.")
    
    return risk_score

# So if run standalone, it runs the console checker and prints score
if __name__ == "__main__":
    score = run_console_checker()
    print(f"Risk Score: {score}")
