class AttendanceSystem:
    def __init__(self):
        self.attendance_records = {}

    def mark_attendance(self, student_id):
        if student_id in self.attendance_records:
            print("Attendance already marked for this student.")
        else:
            self.attendance_records[student_id] = True
            print("Attendance marked successfully.")

    def view_attendance(self):
        print("Attendance Records:")
        for student_id, present in self.attendance_records.items():
            print(f"Student ID: {student_id}, Present: {'Yes' if present else 'No'}")

# Main program
attendance_system = AttendanceSystem()

while True:
    print("\nAttendance Management System")
    print("1. Mark Attendance")
    print("2. View Attendance Records")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        student_id = input("Enter student ID: ")
        attendance_system.mark_attendance(student_id)
    elif choice == '2':
        attendance_system.view_attendance()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
