import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    try:
        grades_df = pd.read_csv("grades.txt", sep=":", header=None, names=["username", "grades"])
        eca_df = pd.read_csv("eca.txt", sep=":", header=None, names=["username", "activities"])
    except FileNotFoundError:
        print("Required data files not found.")
        return None, None

    # Process grades
    grades_df["grades"] = grades_df["grades"].apply(lambda g: list(map(int, g.split(","))))

    grades_df[["sub1", "sub2", "sub3", "sub4", "sub5"]] = pd.DataFrame(grades_df["grades"].tolist(), index=grades_df.index)
    grades_df["average"] = grades_df[["sub1", "sub2", "sub3", "sub4", "sub5"]].mean(axis=1)

    # Process ECA
    eca_df["activities"] = eca_df["activities"].astype(str)  # Convert to string
    eca_df["activity_count"] = eca_df["activities"].apply(lambda x: len(x.split(",")) if x.strip() else 0)

    return grades_df, eca_df


def show_grade_trends(grades_df):
    subject_cols = ["sub1", "sub2", "sub3", "sub4", "sub5"]
    subject_means = grades_df[subject_cols].mean()
                                        
    plt.figure(figsize=(8, 5))
    subject_means.plot(kind="bar", color="skyblue")
    plt.title("📘 Average Grades per Subject")
    plt.ylabel("Average Grade")
    plt.xlabel("Subjects")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


def show_eca_correlation(grades_df, eca_df):
    merged_df = pd.merge(grades_df[["username", "average"]], eca_df[["username", "activity_count"]], on="username")

    plt.figure(figsize=(6, 6))
    plt.scatter(merged_df["activity_count"], merged_df["average"], c="green", edgecolors="black")
    plt.title("🎯 ECA Involvement vs Academic Performance")
    plt.xlabel("ECA Activity Count")
    plt.ylabel("Average Grade")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def show_performance_alerts(grades_df, threshold=50):
    low_performers = grades_df[grades_df["average"] < threshold]
    if low_performers.empty:
                    
        print("✅ No students below the performance threshold.")
    else:
        print("🚨 Students Below Threshold:")
        print(low_performers[["username", "average"]])


def run_analytics_dashboard():
    grades_df, eca_df = load_data()
    if grades_df is None or eca_df is None:
        return

    while True:
        print("\n📊 Analytics Dashboard")
        print("1. Show Grade Trends")
        print("2. ECA vs Performance")
        print("3. Performance Alerts")
        print("0. Back")
        choice = input("Select an option: ")

        if choice == "1":
            show_grade_trends(grades_df)
        elif choice == "2":
            show_eca_correlation(grades_df, eca_df)
        elif choice == "3":
            threshold = input("Enter grade threshold (default 50): ")
            threshold = int(threshold) if threshold else 50
            show_performance_alerts(grades_df, threshold)
        elif choice == "0":
            print("Returning to admin menu...")
            break
        else:
            print("❌ Invalid choice.")