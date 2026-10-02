class LeadTracker:

    def __init__(self, client_name, emails):
        self.client_name = client_name
        self.emails = emails

    def save_lead(self):
        # Save the lead information to a file
        with open("leads.txt", "a") as file:   # this is automatic file closing using 'with' statement after file operations are done
            file.write(f"Client Name: {self.client_name}, Emails: {', '.join(self.emails)}\n")

lead1 = LeadTracker("Amit", ["itspk226@gmail.com"])
lead1.save_lead()
print(lead1.client_name, lead1.emails)
