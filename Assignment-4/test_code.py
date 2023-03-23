# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 22:20:59 2023

@author: Dr. Albert Esterline
"""

if __name__ == "__main__":
    p1 = PersonData(31, spouse="Sue", children=2)
    print(p1)
    p1.print_data()
    p1.birthday()
    p1.new_child()
    p1.divorces()
    p1.print_data()
    p1.marries("Pam")
    try:
       p1.marries("Sue")
    except Exception as detail:
       print(detail)
    try:
       p1.divorces()
       p1.divorces()
    except AttributeError as detail:
       print(detail)
    #p1.print_data()
    p2 = PersonData(39)
    p2.print_data()
    ep1 = EmployedPersonData(31, "Google", spouse="Tom", children=3)
    print(ep1)
    ep1.print_data()

