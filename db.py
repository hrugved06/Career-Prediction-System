import sqlite3
conn = sqlite3.connect('CBRSdata.db', check_same_thread=False)
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS predictiontable(Name TEXT,Contact_Number INTEGER,Email_address TEXT,Logical_quotient_rating INTEGER, coding_skills_rating INTEGER, hackathons INTEGER, public_speaking_points INTEGER, self_learning_capability TEXT, Extra_courses_did TEXT, Taken_inputs_from_seniors_or_elders TEXT, worked_in_teams_ever TEXT, Introvert TEXT, reading_and_writing_skills TEXT, memory_capability_score TEXT, smart_or_hard_work TEXT, Management_or_Techinical TEXT, Interested_subjects TEXT, Interested_Type_of_Books TEXT, certifications TEXT, workshops TEXT, Type_of_company_want_to_settle_in TEXT, interested_career_area TEXT)')


def add_data(Name,Contact_Number,Email_address,Logical_quotient_rating, coding_skills_rating, 
		hackathons, public_speaking_points, self_learning_capability, 
       	Extra_courses_did, Taken_inputs_from_seniors_or_elders,worked_in_teams_ever,
		Introvert, reading_and_writing_skills, memory_capability_score, smart_or_hard_work, 
		Management_or_Techinical, Interested_subjects, Interested_Type_of_Books,certifications, 
		workshops, Type_of_company_want_to_settle_in, interested_career_area):

	c.execute('INSERT INTO predictiontable(Name,Contact_Number,Email_address,Logical_quotient_rating, coding_skills_rating, hackathons, public_speaking_points, self_learning_capability, Extra_courses_did, Taken_inputs_from_seniors_or_elders,worked_in_teams_ever,Introvert, reading_and_writing_skills, memory_capability_score, smart_or_hard_work, Management_or_Techinical, Interested_subjects, Interested_Type_of_Books,certifications, workshops, Type_of_company_want_to_settle_in, interested_career_area) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
		(Name,Contact_Number,Email_address,Logical_quotient_rating, 
	   	coding_skills_rating, hackathons, public_speaking_points, self_learning_capability, 
       	Extra_courses_did, Taken_inputs_from_seniors_or_elders,worked_in_teams_ever,Introvert, 
		reading_and_writing_skills, memory_capability_score, smart_or_hard_work, 
		Management_or_Techinical, Interested_subjects, Interested_Type_of_Books,certifications, 
		workshops, Type_of_company_want_to_settle_in, interested_career_area))
	conn.commit()

