from models import Section

def time_conflict(s1: Section, s2: Section):
    #check if the two sections' days are not the same
    if not set(s1.days).intersection(set(s2.days)):
        return False
    #If both section have at least one day in common, check if the time conflicts
    else:
        return s1.start < s2.end and s2.start < s1.end
    
def not_conflicting_with_selected_sections(new_section: Section, assignment: dict):
    for assigned_section in assignment.values():
        if time_conflict(new_section, assigned_section):
            return False
    return True


