from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage
students = []


@app.route("/")
def home():
    return redirect(url_for("add_student"))


# ---------------------------------
# TODO: IMPLEMENT THIS ROUTE
# ---------------------------------
@app.route("/add", methods=["GET", "POST"])
def add_student():
    error = None

    if request.method == "POST":
        name = request.form.get("name")
        grade = request.form.get("grade")

        # TODO:
        # 1. Validate name
        if not name or name.strip() == "":
            error = "Name cannot be empty."
        # 2. Validate grade is number
        try:
            grade = float(grade)
        except ValueError:
            error = "Grade must be a number."
        # 3. Validate grade range 0–100
        if grade < 0 or grade > 100:
            error = "Grade must be between 0 and 100"
        if error is not None:
            return render_template("add.html", error=error)
        # 4. Add to students list as dictionary
        students.append({"Name" : name, "Grade" : grade})
        # 5. Redirect to /students
        return redirect(url_for("display_students"))



    return render_template("add.html", error=error)


# ---------------------------------
# TODO: IMPLEMENT DISPLAY
# ---------------------------------
@app.route("/students")
def display_students():

    return render_template("students.html", students=students)


# ---------------------------------
# TODO: IMPLEMENT SUMMARY
# ---------------------------------
@app.route("/summary")
def summary():
    # TODO:
    # Calculate:
    # - total students
    total = len(students)
    # - average grade
    grades = []
    total_grades = 0
    count = 0
    for student in students:
        total_grades += student["Grade"]
        count += 1
        grades.append(student["Grade"])
    avg = float(total_grades/count)
    # - highest grade
    highest = max(grades)
    # - lowest grade
    lowest = min(grades)

    return render_template("summary.html",students=students, total=total, avg=avg, highest=highest, lowest=lowest)


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
