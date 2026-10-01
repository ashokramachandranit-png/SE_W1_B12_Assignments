import streamlit as st
import pandas as pd


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Student Result Manager",
    page_icon="🎓",
    layout="wide"
)


# --------------------------------------------------
# Application Title
# --------------------------------------------------

st.title("🎓 Student Result Manager")
st.markdown(
    "View student marks and check **Pass/Fail status for each subject**."
)

st.divider()


# --------------------------------------------------
# Student Data
# --------------------------------------------------

students = [
    {
        "Name": "Ashok",
        "Python": 85,
        "SQL": 78,
        "Java": 90,
        "AI": 88,
        "Cloud": 76
    },
    {
        "Name": "Rahul",
        "Python": 65,
        "SQL": 35,
        "Java": 68,
        "AI": 75,
        "Cloud": 70
    },
    {
        "Name": "Priya",
        "Python": 45,
        "SQL": 52,
        "Java": 32,
        "AI": 55,
        "Cloud": 60
    },
    {
        "Name": "Anitha",
        "Python": 30,
        "SQL": 42,
        "Java": 35,
        "AI": 38,
        "Cloud": 45
    },
    {
        "Name": "Kumar",
        "Python": 92,
        "SQL": 88,
        "Java": 95,
        "AI": 90,
        "Cloud": 94
    }
]


# --------------------------------------------------
# Configuration
# --------------------------------------------------

PASS_MARK = 40

subjects = [
    "Python",
    "SQL",
    "Java",
    "AI",
    "Cloud"
]


# --------------------------------------------------
# Functions
# --------------------------------------------------

def get_status(mark):
    """Return Pass or Fail based on the mark."""

    if mark >= PASS_MARK:
        return "Pass"

    return "Fail"


def get_grade(average):
    """Calculate overall grade."""

    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


# --------------------------------------------------
# Create Result Data
# --------------------------------------------------

results = []

for student in students:

    total = 0
    passed_subjects = 0
    failed_subjects = 0

    result = {
        "Name": student["Name"]
    }

    # Calculate each subject status
    for subject in subjects:

        marks = student[subject]

        status = get_status(marks)

        result[f"{subject} Marks"] = marks
        result[f"{subject} Status"] = status

        total += marks

        if status == "Pass":
            passed_subjects += 1
        else:
            failed_subjects += 1

    # Overall calculations
    average = total / len(subjects)

    if failed_subjects == 0:
        overall_status = "Pass"
    else:
        overall_status = "Fail"

    grade = get_grade(average)

    result["Total"] = total
    result["Average"] = round(average, 2)
    result["Passed Subjects"] = passed_subjects
    result["Failed Subjects"] = failed_subjects
    result["Overall Grade"] = grade
    result["Overall Status"] = overall_status

    results.append(result)


# --------------------------------------------------
# Convert to DataFrame
# --------------------------------------------------

df = pd.DataFrame(results)


# --------------------------------------------------
# Dashboard Summary
# --------------------------------------------------

st.subheader("📊 Class Summary")

total_students = len(df)

passed_students = len(
    df[df["Overall Status"] == "Pass"]
)

failed_students = len(
    df[df["Overall Status"] == "Fail"]
)

class_average = round(
    df["Average"].mean(),
    2
)


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👨‍🎓 Total Students",
        total_students
    )

with col2:
    st.metric(
        "✅ Passed",
        passed_students
    )

with col3:
    st.metric(
        "❌ Failed",
        failed_students
    )

with col4:
    st.metric(
        "📈 Class Average",
        class_average
    )


st.divider()


# --------------------------------------------------
# Student Selection
# --------------------------------------------------

st.subheader("🔎 Student Details")

student_names = [
    student["Name"]
    for student in students
]

selected_student = st.selectbox(
    "Select a student",
    student_names
)


# Find selected student
student = next(
    student
    for student in students
    if student["Name"] == selected_student
)


# --------------------------------------------------
# Student Information
# --------------------------------------------------

st.markdown(
    f"### 👤 {selected_student}'s Result"
)


# Calculate student information
total = sum(
    student[subject]
    for subject in subjects
)

average = total / len(subjects)

passed = sum(
    1
    for subject in subjects
    if student[subject] >= PASS_MARK
)

failed = len(subjects) - passed

overall_status = (
    "Pass"
    if failed == 0
    else "Fail"
)

grade = get_grade(average)


# --------------------------------------------------
# Student Summary
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Marks",
        f"{total}/500"
    )

with col2:
    st.metric(
        "Average",
        f"{average:.2f}%"
    )

with col3:
    st.metric(
        "Subjects Passed",
        passed
    )

with col4:
    st.metric(
        "Grade",
        grade
    )


# Overall status
if overall_status == "Pass":
    st.success(
        f"🎉 Overall Result: {overall_status}"
    )
else:
    st.error(
        f"⚠️ Overall Result: {overall_status}"
    )


st.divider()


# --------------------------------------------------
# Subject-wise Results
# --------------------------------------------------

st.subheader("📚 Subject-wise Results")


for subject in subjects:

    marks = student[subject]

    status = get_status(marks)

    col1, col2, col3 = st.columns([3, 2, 2])

    with col1:
        st.write(f"**{subject}**")

    with col2:
        st.write(f"Marks: **{marks}/100**")

    with col3:

        if status == "Pass":
            st.success("PASS")
        else:
            st.error("FAIL")


# --------------------------------------------------
# Complete Student Table
# --------------------------------------------------

st.divider()

st.subheader("📋 All Student Results")

display_columns = [
    "Name",
    "Python Marks",
    "Python Status",
    "SQL Marks",
    "SQL Status",
    "Java Marks",
    "Java Status",
    "AI Marks",
    "AI Status",
    "Cloud Marks",
    "Cloud Status",
    "Total",
    "Average",
    "Passed Subjects",
    "Failed Subjects",
    "Overall Grade",
    "Overall Status"
]

st.dataframe(
    df[display_columns],
    use_container_width=True,
    hide_index=True
)


# --------------------------------------------------
# Footer
# ---------a-----------------------------------------

st.divider()

st.caption(
    f"Passing mark for each subject: {PASS_MARK}/100"
)