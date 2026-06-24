"""
Inception BD Mini Course Management System
A console-based course enrollment system demonstrating OOP principles:
- Classes & Objects
- Inheritance
- Encapsulation
- Polymorphism

Author: Adnan
Course: Basic Python Programming
"""

# ============================================================================
# STEP 1: Base User Class
# ============================================================================

class User:
    """
    Base class for all users in the system.
    Demonstrates basic class structure with public and protected attributes.
    """
    
    def __init__(self, name, email):
        """
        Initialize a User object.
        
        Args:
            name (str): Public attribute - user's full name
            email (str): Protected attribute - user's email address
        """
        self.name = name          # Public attribute
        self._email = email       # Protected attribute (convention with underscore)
    
    def display_profile(self):
        """
        Display user profile information.
        This method will be overridden by child classes (Polymorphism).
        """
        print(f"Name: {self.name}")
        print(f"Email: {self._email}")
    
    def get_email(self):
        """
        Getter method for protected email attribute.
        Demonstrates encapsulation by providing controlled access.
        """
        return self._email
    
    def set_email(self, new_email):
        """
        Setter method for protected email attribute.
        Allows controlled modification of protected data.
        """
        if "@" in new_email and "." in new_email:
            self._email = new_email
            return True
        return False


# ============================================================================
# STEP 2: Student Class (Inherits from User)
# ============================================================================

class Student(User):
    """
    Student class that inherits from User.
    Demonstrates Inheritance, Encapsulation, and Polymorphism.
    """
    
    def __init__(self, name, email, student_id=None):
        """
        Initialize a Student object.
        
        Args:
            name (str): Student's full name
            email (str): Student's email address
            student_id (str, optional): Student's ID number
        """
        # Call parent class constructor
        super().__init__(name, email)
        
        # Private attribute (Encapsulation with double underscore)
        self.__enrolled_courses = []
        
        # Additional public attributes
        self.student_id = student_id if student_id else f"ST{id(self)}"
    
    def enroll(self, course_name):
        """
        Enroll the student in a course.
        
        Args:
            course_name (str): Name of the course to enroll in
            
        Returns:
            bool: True if enrollment successful, False if already enrolled
        """
        # Check if already enrolled
        if course_name in self.__enrolled_courses:
            print(f"⚠️  {self.name} is already enrolled in '{course_name}'!")
            return False
        
        # Add course to private list
        self.__enrolled_courses.append(course_name)
        print(f"✅ {self.name} has been enrolled in '{course_name}'!")
        return True
    
    def unenroll(self, course_name):
        """
        BONUS: Unenroll the student from a course.
        
        Args:
            course_name (str): Name of the course to unenroll from
            
        Returns:
            bool: True if unenrollment successful, False if not enrolled
        """
        # Check if enrolled in the course
        if course_name not in self.__enrolled_courses:
            print(f"❌ {self.name} is not enrolled in '{course_name}'!")
            return False
        
        # Remove course from private list
        self.__enrolled_courses.remove(course_name)
        print(f"✅ {self.name} has been unenrolled from '{course_name}'!")
        return True
    
    def view_courses(self):
        """
        Display all courses the student is enrolled in.
        """
        if not self.__enrolled_courses:
            print(f"📚 {self.name} is not enrolled in any courses.")
            return
        
        print(f"\n📚 {self.name}'s Enrolled Courses:")
        print("-" * 40)
        for i, course in enumerate(self.__enrolled_courses, 1):
            print(f"  {i}. {course}")
        print("-" * 40)
    
    def get_enrolled_courses(self):
        """
        Getter method for private __enrolled_courses.
        Returns a copy to maintain encapsulation.
        """
        return self.__enrolled_courses.copy()
    
    def display_profile(self):
        """
        Override display_profile() to show student-specific information.
        Demonstrates POLYMORPHISM.
        """
        print("\n" + "="*50)
        print("🎓 STUDENT PROFILE")
        print("="*50)
        print(f"Name: {self.name}")
        print(f"Email: {self._email}")
        print(f"Student ID: {self.student_id}")
        print(f"Enrolled Courses: {len(self.__enrolled_courses)}")
        print(f"Status: Active Student 🟢")
        print("="*50)


# ============================================================================
# STEP 2 (Continued): Instructor Class (Inherits from User)
# ============================================================================

class Instructor(User):
    """
    Instructor class that inherits from User.
    Demonstrates Inheritance and Polymorphism.
    """
    
    def __init__(self, name, email, assigned_department):
        """
        Initialize an Instructor object.
        
        Args:
            name (str): Instructor's full name
            email (str): Instructor's email address
            assigned_department (str): Department the instructor belongs to
        """
        # Call parent class constructor
        super().__init__(name, email)
        
        # Instructor-specific attributes
        self.assigned_department = assigned_department
        self.courses_teaching = []  # Track courses they teach
    
    def add_course(self, course_name):
        """
        Add a course to the instructor's teaching list.
        
        Args:
            course_name (str): Name of the course to add
        """
        if course_name not in self.courses_teaching:
            self.courses_teaching.append(course_name)
    
    def view_teaching_courses(self):
        """
        Display all courses the instructor is teaching.
        """
        if not self.courses_teaching:
            print(f"📝 {self.name} is not teaching any courses.")
            return
        
        print(f"\n📝 {self.name}'s Teaching Courses:")
        print("-" * 40)
        for i, course in enumerate(self.courses_teaching, 1):
            print(f"  {i}. {course}")
        print("-" * 40)
    
    def display_profile(self):
        """
        Override display_profile() to show instructor-specific information.
        Demonstrates POLYMORPHISM.
        """
        print("\n" + "="*50)
        print("👨‍🏫 INSTRUCTOR PROFILE")
        print("="*50)
        print(f"Name: {self.name}")
        print(f"Email: {self._email}")
        print(f"Department: {self.assigned_department}")
        print(f"Courses Teaching: {len(self.courses_teaching)}")
        print(f"Status: Active Instructor 🔵")
        print("="*50)


# ============================================================================
# STEP 3: Course Class
# ============================================================================

class Course:
    """
    Course class that associates with an Instructor.
    """
    
    def __init__(self, course_name, duration, instructor):
        """
        Initialize a Course object.
        
        Args:
            course_name (str): Name of the course
            duration (str): Duration of the course (e.g., "6 Days")
            instructor (Instructor): Instructor object teaching the course
        """
        self.course_name = course_name
        self.duration = duration
        self.instructor = instructor  # This should be an Instructor object
        self.enrolled_students = []   # Track enrolled students
        
        # Add this course to instructor's teaching list
        if isinstance(instructor, Instructor):
            instructor.add_course(course_name)
    
    def add_student(self, student):
        """
        Add a student to the course.
        
        Args:
            student (Student): Student object to add
        """
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
    
    def course_details(self):
        """
        Display detailed information about the course.
        """
        print("\n" + "="*60)
        print("📖 COURSE DETAILS")
        print("="*60)
        print(f"Course Name: {self.course_name}")
        print(f"Duration: {self.duration}")
        print(f"Instructor: {self.instructor.name}")
        print(f"Department: {self.instructor.assigned_department}")
        print(f"Enrolled Students: {len(self.enrolled_students)}")
        
        if self.enrolled_students:
            print(f"\n📋 Student List:")
            for i, student in enumerate(self.enrolled_students, 1):
                print(f"  {i}. {student.name} (ID: {student.student_id})")
        
        print("="*60)


# ============================================================================
# STEP 4: Execution - Bring it All Together
# ============================================================================

def main():
    """
    Main execution function to demonstrate the Course Management System.
    """
    
    print("\n" + "="*70)
    print("🌟 INCEPTION BD - MINI COURSE MANAGEMENT SYSTEM 🌟")
    print("="*70)
    print("\nDemonstrating OOP Principles:")
    print("  • Classes & Objects")
    print("  • Inheritance")
    print("  • Encapsulation")
    print("  • Polymorphism")
    print("\n" + "="*70)
    
    # -----------------------------------------------------------------------
    # Test Phase 1: Create Users (Instructors and Students)
    # -----------------------------------------------------------------------
    
    print("\n\n📌 PHASE 1: CREATING USERS")
    print("-" * 50)
    
    # 1. Instantiate an Instructor
    print("\n🔹 Creating Instructor...")
    instructor1 = Instructor(
        name="Md. Rahman",
        email="rahman@inceptionbd.com",
        assigned_department="Data Science"
    )
    print(f"✅ Instructor created: {instructor1.name}")
    
    # Create another instructor for demonstration
    instructor2 = Instructor(
        name="Fatima Akter",
        email="fatima@inceptionbd.com",
        assigned_department="Software Engineering"
    )
    print(f"✅ Instructor created: {instructor2.name}")
    
    # 2. Instantiate Course objects with instructors
    print("\n🔹 Creating Courses...")
    
    course1 = Course(
        course_name="Python for Data Science",
        duration="6 Days",
        instructor=instructor1
    )
    print(f"✅ Course created: {course1.course_name}")
    
    course2 = Course(
        course_name="Web Development with Django",
        duration="8 Days",
        instructor=instructor2
    )
    print(f"✅ Course created: {course2.course_name}")
    
    course3 = Course(
        course_name="Machine Learning Fundamentals",
        duration="10 Days",
        instructor=instructor1
    )
    print(f"✅ Course created: {course3.course_name}")
    
    # 3. Instantiate Student objects
    print("\n🔹 Creating Students...")
    
    student1 = Student(
        name="Adnan Rahman",
        email="adnan@email.com",
        student_id="ST2024001"
    )
    print(f"✅ Student created: {student1.name}")
    
    student2 = Student(
        name="Tahmid Hassan",
        email="tahmid@email.com",
        student_id="ST2024002"
    )
    print(f"✅ Student created: {student2.name}")
    
    student3 = Student(
        name="Nusrat Jahan",
        email="nusrat@email.com",
        student_id="ST2024003"
    )
    print(f"✅ Student created: {student3.name}")
    
    # -----------------------------------------------------------------------
    # Test Phase 2: Enroll Students in Courses
    # -----------------------------------------------------------------------
    
    print("\n\n📌 PHASE 2: ENROLLING STUDENTS")
    print("-" * 50)
    
    # Enroll students in various courses
    print(f"\n🔹 {student1.name} enrolling in courses...")
    student1.enroll(course1.course_name)
    course1.add_student(student1)
    
    student1.enroll(course2.course_name)
    course2.add_student(student1)
    
    print(f"\n🔹 {student2.name} enrolling in courses...")
    student2.enroll(course1.course_name)
    course1.add_student(student2)
    
    student2.enroll(course3.course_name)
    course3.add_student(student2)
    
    print(f"\n🔹 {student3.name} enrolling in courses...")
    student3.enroll(course2.course_name)
    course2.add_student(student3)
    
    student3.enroll(course3.course_name)
    course3.add_student(student3)
    
    # -----------------------------------------------------------------------
    # Test Phase 3: Demonstrate Polymorphism
    # -----------------------------------------------------------------------
    
    print("\n\n📌 PHASE 3: DISPLAYING PROFILES (POLYMORPHISM)")
    print("-" * 50)
    
    # Create a list of all users to demonstrate polymorphism
    all_users = [instructor1, instructor2, student1, student2, student3]
    
    print("\n🔹 Displaying all user profiles:")
    print("   (Notice how each class has its own display_profile() implementation)")
    
    for user in all_users:
        user.display_profile()  # Polymorphism in action!
    
    # -----------------------------------------------------------------------
    # Test Phase 4: Display Course Details
    # -----------------------------------------------------------------------
    
    print("\n\n📌 PHASE 4: COURSE DETAILS")
    print("-" * 50)
    
    all_courses = [course1, course2, course3]
    
    print("\n🔹 Displaying all course details:")
    for course in all_courses:
        course.course_details()
    
    # -----------------------------------------------------------------------
    # Test Phase 5: View Enrolled Courses (Per Student)
    # -----------------------------------------------------------------------
    
    print("\n\n📌 PHASE 5: STUDENT COURSE LISTS")
    print("-" * 50)
    
    students = [student1, student2, student3]
    
    for student in students:
        student.view_courses()
    
    # -----------------------------------------------------------------------
    # Test Phase 6: Instructor's Teaching Load
    # -----------------------------------------------------------------------
    
    print("\n\n📌 PHASE 6: INSTRUCTOR TEACHING LOADS")
    print("-" * 50)
    
    instructors = [instructor1, instructor2]
    
    for instructor in instructors:
        instructor.view_teaching_courses()
    
    # -----------------------------------------------------------------------
    # BONUS: Demonstrate Unenrollment
    # -----------------------------------------------------------------------
    
    print("\n\n🌟 BONUS: TESTING UNENROLLMENT FEATURE")
    print("-" * 50)
    
    print(f"\n🔹 {student1.name} attempting to unenroll from {course2.course_name}...")
    if student1.unenroll(course2.course_name):
        # Also remove from course's student list
        course2.enrolled_students.remove(student1)
    
    print(f"\n🔹 {student1.name} attempting to unenroll from a course they're not in...")
    student1.unenroll("Advanced AI")  # Should show error
    
    print(f"\n🔹 Updated course list for {student1.name}:")
    student1.view_courses()
    
    # -----------------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------------
    
    print("\n\n" + "="*70)
    print("✅ SYSTEM DEMONSTRATION COMPLETE")
    print("="*70)
    
    print("\n📊 SYSTEM SUMMARY:")
    print("-" * 40)
    print(f"Total Instructors: {len(instructors)}")
    print(f"Total Students: {len(students)}")
    print(f"Total Courses: {len(all_courses)}")
    print(f"Total Enrollments: {sum(len(course.enrolled_students) for course in all_courses)}")
    
    print("\n🎯 OOP CONCEPTS DEMONSTRATED:")
    print("-" * 40)
    print("✅ Classes & Objects: User, Student, Instructor, Course classes")
    print("✅ Inheritance: Student and Instructor inherit from User")
    print("✅ Encapsulation: Private __enrolled_courses, protected _email")
    print("✅ Polymorphism: display_profile() overridden in each subclass")
    
    print("\n" + "="*70)
    print("🌟 Thank you for using Inception BD CMS! 🌟")
    print("="*70 + "\n")


# ============================================================================
# Additional Test Functions (Optional)
# ============================================================================

def test_encapsulation():
    """
    Demonstrate encapsulation with private and protected attributes.
    """
    print("\n" + "="*60)
    print("🔒 ENCAPSULATION DEMONSTRATION")
    print("="*60)
    
    student = Student("Test Student", "test@email.com", "ST999")
    
    # This works (public attribute)
    print(f"✅ Public attribute access: {student.name}")
    
    # This works but is discouraged (protected attribute)
    print(f"⚠️  Protected attribute access (possible but discouraged): {student._email}")
    
    # This will raise an AttributeError (private attribute)
    try:
        print(student.__enrolled_courses)
    except AttributeError as e:
        print(f"❌ Cannot access private attribute directly: {e}")
    
    # Correct way to access private data (through public methods)
    courses = student.get_enrolled_courses()
    print(f"✅ Accessing through getter method: {courses}")


def test_polymorphism():
    """
    Demonstrate polymorphism with a common interface.
    """
    print("\n" + "="*60)
    print("🔄 POLYMORPHISM DEMONSTRATION")
    print("="*60)
    
    # Create different user types
    users = [
        Student("Alice", "alice@email.com", "ST001"),
        Instructor("Bob", "bob@email.com", "AI"),
        Student("Charlie", "charlie@email.com", "ST002"),
        Instructor("Diana", "diana@email.com", "Web Dev")
    ]
    
    print("\n🔹 Calling display_profile() on different user types:")
    print("   (Same method name, different behaviors)\n")
    
    for user in users:
        print(f"Type: {type(user).__name__}")
        user.display_profile()
        print()


# ============================================================================
# Run the main program
# ============================================================================

if __name__ == "__main__":
    try:
        # Run main demonstration
        main()
        
        # Run additional demonstrations (optional)
        print("\n\n" + "="*70)
        print("ADDITIONAL DEMONSTRATIONS")
        print("="*70)
        
        test_encapsulation()
        test_polymorphism()
        
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        import traceback
        traceback.print_exc()
