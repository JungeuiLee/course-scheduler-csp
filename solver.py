from typing import Dict, List
from models import Course, Section, Metrics
from constraints import not_conflicting_with_selected_sections, time_conflict

class Solver:
    def __init__(self, courses: List[Course], mode: str = "basic"):
        self.courses = courses
        self.mode = mode
        self.metrics = Metrics()

    def solve(self):
        assignment = {}
        #Constraint Propagation will have different domains for each course
        if self.mode == "mrv_degree_mac":
            domains = {}
            for i in self.courses:
                course_id = i.course_id
                sections_copy = i.sections[:]
                domains[course_id] = sections_copy

            return self.backtrack_mac(assignment, domains)

        return self.backtrack(assignment)
    
    '''
    Backtracking
    '''
    def backtrack(self, assignment: Dict[str, Section]):
        #When all the courses are assigned, success
        if len(assignment) == len(self.courses):
            return assignment.copy()
        
        self.metrics.nodes_visited += 1
        
        #choose first unassigned course by calling choose_unassigned_course
        course = self.choose_unassigned_course(assignment)
        #try all the sections of the chosen course
        for section in course.sections:
            if not_conflicting_with_selected_sections(section, assignment):
                assignment[course.course_id] = section
                result = self.backtrack(assignment)
                if result is not None:
                    return result

                #Remove the sectioin from the assignment if it fails
                del assignment[course.course_id]
        self.metrics.backtracks += 1
        return None
    
    '''
    Backtracking for Constraint Propagation (MAC / AC-3)
    '''
    def backtrack_mac(self, assignment: Dict[str, Section], domains: Dict[str, List[Section]]):
        if len(assignment) == len(self.courses):
            return assignment.copy()
        
        self.metrics.nodes_visited += 1
        course = self.choose_unassigned_course_mrv_degree_mac(assignment, domains)

        for section in domains[course.course_id]:
            if not_conflicting_with_selected_sections(section, assignment):
                assignment[course.course_id] = section

                # Copy only dict/list containers; Section objects are read-only here.
                new_domains = {}
                for cid, sections in domains.items():
                    new_domains[cid] = sections[:] # Copy list contents, not references
                new_domains[course.course_id] = [section]

                if self.ac3(new_domains, assignment): #ac3 function line 160
                    result = self.backtrack_mac(assignment, new_domains)
                    if result is not None:
                        return result
                
                #Remove the section from the assignment if it fails
                del assignment[course.course_id]
        #Backtrack if all the sections fail
        self.metrics.backtracks += 1
        return None


    #Choosing unassigned courses based on the mode
    def choose_unassigned_course(self, assignment: Dict[str, Section]):
        if self.mode == "basic":
            return self.choose_unassigned_course_basic(assignment)
        if self.mode == "mrv_degree":
            return self.choose_unassigned_course_mrv_degree(assignment)
        raise ValueError(f"Unknown mode: {self.mode}")
    
    def choose_unassigned_course_mrv_degree_mac(self, assignment: Dict[str, Section], domains: Dict[str, List[Section]]):
        unassigned = self.get_unassigned_courses(assignment)

        min_section_count = float('inf')
        candidates = []

        for course in unassigned:
            section_count = len(domains[course.course_id])

            if section_count < min_section_count:
                min_section_count = section_count
                candidates = [course]
            elif section_count == min_section_count:
                candidates.append(course)

        if len(candidates) == 1:
            return candidates[0]

        result = None
        maximum = -1

        for course in candidates:
            degree = self.get_degree(course, unassigned)
            if degree > maximum:
                maximum = degree
                result = course

        return result

    #helper to get unassigned courses
    def get_unassigned_courses(self, assignment: Dict[str, Section]) -> List[Course]:
        unassigned_courses = []

        for course in self.courses:
            if course.course_id not in assignment:
                unassigned_courses.append(course)

        return unassigned_courses

    '''
    [Backtracking] For choosing unassigned courses from the list of courses
    '''
    def choose_unassigned_course_basic(self, assignment: Dict[str, Section]):
        unassigned = self.get_unassigned_courses(assignment)
        return unassigned[0]
    '''
    [Heuristics (MRV + Degree Heuristic)]
    '''
    def choose_unassigned_course_mrv_degree(self, assignment: Dict[str, Section]):
        unassigned = self.get_unassigned_courses(assignment)

        #get the min count of sections for the unassigned courses and choose the course
        min_section_count = float('inf')
        candidates = []

        for i in unassigned:
            section_count = self.get_section_count(i, assignment)
            if section_count < min_section_count:
                min_section_count = section_count
                candidates = [i]
            elif section_count == min_section_count:
                candidates.append(i)
        
        #if length of candidate is 1, return the course =
        if len(candidates) == 1:
            return candidates[0]
        #if not, apply degree heuristic
        result = None
        maximum = -1
        for i in candidates:
            degree = self.get_degree(i, unassigned)
            if degree > maximum:
                maximum = degree
                result = i
        return result
    
    def get_section_count(self, course: Course, assignment: Dict[str, Section]):
        count = 0
        for i in course.sections:
            if not_conflicting_with_selected_sections(i, assignment):
                count += 1
        return count
    
    #helper to get the degree of a course
    def get_degree(self, course: Course, unassigned: List[Course]):
        degree = 0
        for i in unassigned:
            if i.course_id == course.course_id:
                continue
            if self.number_of_conflicts(course, i):
                degree += 1
        return degree
    def number_of_conflicts(self, c1: Course, c2: Course):
        for i in c1.sections:
            for j in c2.sections:
                if time_conflict(i, j):
                    return True
        return False

    '''
    #[Constraints Propagation (MAC / AC-3)]
    '''
    #ac3: arc consistency algorithm
    def ac3(self, domains: Dict[str, List[Section]], assignment: Dict[str, Section]):
        queue = []

        course_ids = []
        for course in self.courses:
            course_ids.append(course.course_id)

        #Push all the arcs into the queue
        for i in course_ids:
            for j in course_ids:
                if i != j:
                    queue.append((i, j))
        
        while queue:
            course_one, course_two = queue.pop(0)

            #Detect conflict sections using revise function
            if self.revise(course_one, course_two, domains):
                if len(domains[course_one]) == 0:
                    return False
                #Re-insert the arcs into the queue since the domain has been revised
                for i in course_ids:
                    if i != course_one and i != course_two:
                        queue.append((i, course_one))
        return True
    
    #revise function: eliminate the section that conflicts with other course's section
    def revise(self, course_one: str, course_two: str, domains: Dict[str, List[Section]]):
        #Checker for if domain is revised
        revised = False
        #New domain for the course_one
        new_domain = []

        for section_one in domains[course_one]:
            #Check if the section is valid for the other course
            validity = False
            #Compare one of the sections of course_one with all the sections of course_two
            for section_two in domains[course_two]:
                #If at least one section of course_one is valid for course_two, then the section is valid for course_one
                if not time_conflict(section_one, section_two):
                    validity = True
                    break
            #Keep the section if it is valid
            if validity:
                new_domain.append(section_one)
            else:
                revised = True
        #update the domain of course_one
        domains[course_one] = new_domain
        return revised