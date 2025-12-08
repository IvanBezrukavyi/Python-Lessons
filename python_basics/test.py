
# Task 4. Provide statistics by severity + status, e.g. "high_open": 2, "high_closed": 0

bugs = [
    {"id": 1, "title": "Login error", "severity": "low", "status": "open"},
    {"id": 2, "title": "PAYMENT failed", "severity": "high", "status": "open"},
    {"id": 3, "title": "Page not found", "severity": "medium", "status": "closed"},
    {"id": 4, "title": "payment timeout", "severity": "high", "status": "open"},
]

def count_bugs_by_severity(bugs):
   
    stats = {

    }

    for bug in bugs:
        current_severity = bug["severity"].lower()
        current_status = bug["status"].lower()
    
        result = current_severity + "_" + current_status
        if result not in stats:
            stats[result] = 0
        stats[result] += 1
    return stats

result_by_severity_status =  count_bugs_by_severity(bugs)
print(result_by_severity_status)