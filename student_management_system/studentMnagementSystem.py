students = []

def add_student():
	name = input("Enter student name: ").strip()
	if not name:
		print("No name entered.")
		return
	students.append(name)
	print(f"Added student: {name}")


def list_students():
	if not students:
		print("No students.")
		return
	print("Students:")
	for i, s in enumerate(students, 1):
		print(f"{i}. {s}")


def main():
	while True:
		print("\nStudent Management System")
		print("1. Add student")
		print("2. List students")
		print("3. Exit")
		choice = input("Choice: ").strip()
		if choice == '1':
			add_student()
		elif choice == '2':
			list_students()
		elif choice == '3':
			print("Exiting.")
			break
		else:
			print("Invalid choice.")


if __name__ == '__main__':
	main()