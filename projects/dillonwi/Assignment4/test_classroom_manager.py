from unittest import TestCase
import classroom_manager


class TestStudent(TestCase):
    def test_get_full_name(self):
        # Initialize a student, Jerry Seinfeld
        tStu = classroom_manager.Student(3, "Jerry", "Seinfeld")
        self.assertEqual(tStu.id, 3)
        self.assertEqual(tStu.first_name, "Jerry")
        self.assertEqual(tStu.last_name, "Seinfeld")

        #Run the get full name
        fName = tStu.get_full_name()

        #Check to see that Jerry Seinfeld is the string returned when get_full_name is called.
        self.assertEqual("Jerry Seinfeld", fName)

        pass

    def test_submit_assignment(self):
        #Create a student for whom the assignment will be submitted.
        sStu = classroom_manager.Student(5, "Eric", "Cartman")

        #Create an assignment that will be submitted
        Assgn1 = classroom_manager.Assignment("HW1", 100)
        self.assertEqual(Assgn1.name, "HW1")
        self.assertEqual(Assgn1.grade, None)
        self.assertEqual(Assgn1.max_score, 100)

        #Check to see that there are no assignments for this student. All students start with no assignments
        self.assertEqual(0, len(sStu.assignments))

        #submit the assignment
        sStu.submit_assignment(Assgn1)

        #Check the length again
        self.assertEqual(1, len(sStu.assignments))
        self.assertEqual(Assgn1, sStu.assignments[0])

        pass

    def test_get_assignments(self):
        #Create a student to whom assignments will be added
        Stu = classroom_manager.Student(7, "Travis", "Touchdown")

        #Create a bunch of assignments that will be submitted for this student.
        A1 = classroom_manager.Assignment("HW1", 100)
        A2 = classroom_manager.Assignment("HW2", 50)
        A3 = classroom_manager.Assignment("HW3", 100)
        A4 = classroom_manager.Assignment("HW4", 200)
        A5 = classroom_manager.Assignment("HW5", 10)

        #Submit multiple assignments for this student
        Stu.submit_assignment(A1)
        Stu.submit_assignment(A2)
        Stu.submit_assignment(A3)
        Stu.submit_assignment(A4)
        Stu.submit_assignment(A5)

        #Check to see that 5 assignments have indeed been added.
        self.assertEqual(5, len(Stu.assignments))

        #make a list of assignments
        list = []

        #Run the get_assignments function, and set the assignments into the list
        list = Stu.get_assignments()

        #After doing this, check to see that the get_assignments indeed returned all the assignments.
        self.assertEqual("HW1", list[0].name)
        self.assertEqual("HW2", list[1].name)
        self.assertEqual("HW3", list[2].name)
        self.assertEqual("HW4", list[3].name)
        self.assertEqual("HW5", list[4].name)

        pass

    def test_get_assignment(self):
        # Create a student to whom assignments will be added
        bStu = classroom_manager.Student(12, "Benny", "Beaver")

        # Create a bunch of assignments that will be submitted for this student.
        A1 = classroom_manager.Assignment("HW1", 100)
        A2 = classroom_manager.Assignment("HW2", 50)
        A3 = classroom_manager.Assignment("HW3", 100)

        #Submit multiple assignments for this student
        bStu.submit_assignment(A1)
        bStu.submit_assignment(A2)
        bStu.submit_assignment(A3)

        # Check to see that 3 assignments have indeed been added.
        self.assertEqual(3, len(bStu.assignments))

        #Set up a variable that contains the result of running get_assignment
        vAssign = bStu.get_assignment("HW1")

        #check to see that vAssign is equal to A1, then try it for other assignments in the array.
        self.assertEqual(vAssign, A1)

        vAssign = bStu.get_assignment("HW2")
        self.assertEqual(vAssign, A2)

        #Finally, test this for when the get_assignment returns None
        vAssign = bStu.get_assignment("Extra Credit")
        self.assertEqual(vAssign, None)

        pass

    def test_get_average(self):
        # Create a student to whom assignments will be added
        lStu = classroom_manager.Student(34, "Lou", "Albano")

        # Create a bunch of assignments that will be submitted for this student.
        A1 = classroom_manager.Assignment("HW1", 50)
        A2 = classroom_manager.Assignment("HW2", 50)
        A3 = classroom_manager.Assignment("HW3", 150)

        #Set grades for the assignment. Note that we expect the assign_grade for A2 to return -1 because 100 > 50.
        A1.assign_grade(0)
        A2.assign_grade(100)
        A3.assign_grade(150)

        #Check to see that the grades have been assigned as expected
        self.assertEqual(0, A1.grade)
        self.assertEqual(None, A2.grade)
        self.assertEqual(150, A3.grade)

        #Submit these assignments for the student.
        lStu.submit_assignment(A1)
        lStu.submit_assignment(A2)
        lStu.submit_assignment(A3)

        #The average of these grades should come out to be 75. The grade for A2 is none, so it shouldn't factor in.
        self.assertEqual(75, lStu.get_average())


        pass

    def test_remove_assignment(self):
        # Create a student to whom assignments will be added
        fStu = classroom_manager.Student(19, "Freddy", "Freaker")

        # Create a bunch of assignments that will be submitted for this student.
        A1 = classroom_manager.Assignment("HW1", 100)
        A2 = classroom_manager.Assignment("HW2", 50)
        A3 = classroom_manager.Assignment("HW3", 100)

        # Submit multiple assignments for this student
        fStu.submit_assignment(A1)
        fStu.submit_assignment(A2)
        fStu.submit_assignment(A3)

        # Confirm that the student has 3 assignments.
        self.assertEqual(3, len(fStu.assignments))

        #Attempt to remove HW3
        fStu.remove_assignment("HW3")

        #After removing HW3, attempt to get it. It should return None, because that is no longer in there.
        self.assertEqual(None, fStu.get_assignment("HW3"))

        #Check to see that there's only 2 assignments left in the pile of assignments
        self.assertEqual(2, len(fStu.assignments))

        # Remove 1 more and try to remove another that's not in the pile.
        fStu.remove_assignment("HW3")
        fStu.remove_assignment("HW1")

        # Check to see that there's only 1 assignments left in the pile of assignments
        self.assertEqual(1, len(fStu.assignments))
        pass


class TestAssignment(TestCase):
    def test_assign_grade(self):
        # Create a student to whom assignments will be added
        tStu = classroom_manager.Student(15, "Dwayne", "Johnson")

        # Create a bunch of assignments that will be submitted for this student.
        A1 = classroom_manager.Assignment("HW1", 50)
        A2 = classroom_manager.Assignment("HW2", 50)
        A3 = classroom_manager.Assignment("HW3", 200)


        # Set grades for the assignment. Note that we expect the assign_grade for A2 to return -1 because 100 > 50.
        A1.assign_grade(50)
        A2.assign_grade(100)
        A3.assign_grade(110)


        # Check to see that the grades have been assigned as expected.
        self.assertEqual(50, A1.grade)
        self.assertEqual(None, A2.grade)
        self.assertEqual(110, A3.grade)

        pass
