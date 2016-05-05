"""
Given a list of tickets, find itinerary in order using the given list.
Input:
"Chennai" -> "Banglore"
"Bombay" -> "Delhi"
"Goa"    -> "Chennai"
"Delhi"  -> "Goa"

Output:
Bombay->Delhi, Delhi->Goa, Goa->Chennai, Chennai->Banglore
"""

def build_itinerary(tickets):
    h={}
    for ticket in tickets:
        if ticket[0] in h:
            return "find cycle, not supposed to happen"
        h[ticket[0]] = ticket[1]

    

    return None

print(build_itinerary([("Chennai", "Banglore"), ("Bombay", "Delhi"), ("Goa", "Chennai"), ("Delhi", "Goa")]))
