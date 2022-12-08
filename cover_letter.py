# Import necessary libraries
import time
from datetime import datetime

# Define cover letter template
template = """
Dear [Employer],

I am writing to apply for the [Position] at [Company]. I am confident that my skills and experience make me a strong candidate for this role.

I have [X] years of experience in [Industry/Field], and have a track record of success in [Key achievements/responsibilities]. I am highly skilled in [Key skills/technologies relevant to the position], and am always looking for opportunities to learn and grow in my career.

I am excited about the potential to contribute to [Company] and believe that I would be a great fit for the [Position]. Thank you for considering my application. I look forward to the opportunity to discuss my qualifications in more detail.

Sincerely,
[Your Name]
[Your Phone Number]
[Your Email]
"""

# Prompt user for input
position = input("What is the position you are applying for? ")
company = input("What company are you applying to? ")
experience = input("How many years of experience do you have? ")
industry = input("What industry or field are you in? ")
achievements = input("What are some key achievements or responsibilities you have had in your career? ")
skills = input("What are some key skills or technologies relevant to the position you are applying for? ")
name = input("What is your name? ")
phone = input("What is your phone number? ")
email = input("What is your email address? ")

# Insert user input into cover letter template
cover_letter = template.replace("[Employer]", company)
cover_letter = cover_letter.replace("[Position]", position)
cover_letter = cover_letter.replace("[Company]", company)
cover_letter = cover_letter.replace("[X]", experience)
cover_letter = cover_letter.replace("[Industry/Field]", industry)
cover_letter = cover_letter.replace("[Key achievements/responsibilities]", achievements)
cover_letter = cover_letter.replace("[Key skills/technologies relevant to the position]", skills)
cover_letter = cover_letter.replace("[Your Name]", name)
cover_letter = cover_letter.replace("[Your Phone Number]", phone)
cover_letter = cover_letter.replace("[Your Email]", email)

# Print final cover letter
print("\nCover Letter:")
print(cover_letter)

# Save cover letter as a text file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = "cover_letter_" + timestamp + ".txt"
file = open(filename, "w")
file.write(cover_letter)
file.close()

print("\nCover letter saved to: " + filename)