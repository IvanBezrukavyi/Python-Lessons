bugs = [
    {"id": 1, "title": "Login error", "severity": "low", "status": "open"},
    {"id": 2, "title": "PAYMENT failed", "severity": "high", "status": "open"},
    {"id": 3, "title": "Page not found", "severity": "medium", "status": "closed"},
    {"id": 4, "title": "payment timeout", "severity": "high", "status": "open"},
]

# Task 1
# Count bugs with status == "open" and contain "payment" у title w/o register.

def count_payment_bugs(bugs):
    count = 0

    for bug in bugs:
        title = bug["title"].lower()
        status = bug["status"]
        
        if status == "open" and "payment" in title:
            count += 1 
    return count
result =  count_payment_bugs(bugs)         
print(f"Payment open bugs: {result}")

# Task 2. Count the total open bugs
def count_open_bugs(bugs):
    count = 0

    for bug in bugs:
        status = bug["status"]

        if status == "open":
            count +=1
    return count

open_bug_result = count_open_bugs(bugs)
print("Total open bugs: ", open_bug_result)

# Task 3. Count total bugs with high or low severity
def count_bugs_by_severity(bugs, severity):
    target_severity = severity.lower()
    count = 0
    
    for bug in bugs:
        bug_severity = bug["severity"].lower()

        if bug_severity == target_severity:
            count +=1
    return count
high_severity_bug = count_bugs_by_severity(bugs, "HIGH")
print("Total bugs with HIGH severity: ", high_severity_bug)

low_severity_bug = count_bugs_by_severity(bugs, "LOW")
print("Total bugs with LOW severity: ", low_severity_bug)

# Task 4. Provide statistics by severity, e.g. {"low": 1, "medium": 1, "high": 2}

def count_bugs_by_severity(bugs):
   
    stats = {
    "low": 0,
    "medium": 0,
    "high": 0
}
    
    for bug in bugs:
        current_severity = bug["severity"].lower()

        if current_severity not in stats:
            stats[current_severity] = 0
        stats[current_severity] += 1    
    return stats
bugs_by_severity = count_bugs_by_severity(bugs)
print(bugs_by_severity)

# Task 5. Provide statistics by severity + status, e.g. "high_open": 2, "high_closed": 0      

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