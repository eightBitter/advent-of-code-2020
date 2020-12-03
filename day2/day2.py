# Code for Day 2 of Advent of Code 2020

## Challenge 1
### Their password database seems to be a little corrupted: some of the passwords 
### wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

###To try to debug the problem, they have created a list (your puzzle input) of 
### passwords (according to the corrupted database) and the corporate policy when that 
### password was set.

## Challenge 2
### Each policy actually describes two positions in the password, where 1 means 
### the first character, 2 means the second character, and so on. (Be careful; 
### Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of 
### these positions must contain the given letter. Other occurrences of the letter 
### are irrelevant for the purposes of policy enforcement.

### How many passwords are valid according to the new interpretation of the policies?

## generate list from data file
def get_fake_passwords():
    fake_passwords = []
    with open('day2/data/fake_passwords.txt','r') as pass_list:
        for fake_pass in pass_list:
            fake_passwords.append(fake_pass.replace("\n", "").replace(":", ""))
    return fake_passwords

## create a list of dictionaries that splits up parts of each string into indexable chunks
def create_evaluation_list():
    fake_passwords = get_fake_passwords()
    evaluation_list = []
    for fake_pass in fake_passwords:
        eval_dict = {}
        split_up = fake_pass.split(" ")
        eval_dict["num_range"] = split_up[0]
        eval_dict["num_range"] = eval_dict["num_range"].split("-")
        eval_dict["eval_letter"] = split_up[1]
        eval_dict["pass_string"] = split_up[2]
        evaluation_list.append(eval_dict)
    return evaluation_list

## returns all passwords that meet the criteria for challenge 1
def evaluate_passwords_former():
    evaluation_list = create_evaluation_list()
    passing_passes = []
    for criteria in evaluation_list:
        letter_to_count = []
        for letter in criteria["pass_string"]:
            ## pulls out all instances of the letter we want to count
            if letter == criteria["eval_letter"]:
                letter_to_count.append(letter)
        ## evalutes whether the count of instances is within the specified range
        if len(letter_to_count) >= int(criteria["num_range"][0]) and len(letter_to_count) <= int(criteria["num_range"][1]):
            passing_passes.append(criteria["pass_string"])
    return passing_passes

## returns all passwords that meet the criteria for challenge 2
def evaluate_passwords_current():
    evaluation_list = create_evaluation_list()
    passing_passes = []
    for criteria in evaluation_list:
        ## looks for specific letters in the pass string based on the number range. 
        ## If the criteria matches the password criteria, it adds the pass string to a 
        ## list to be counted later
        if criteria["pass_string"][int(criteria["num_range"][0])-1] == criteria["eval_letter"] and criteria["pass_string"][int(criteria["num_range"][1])-1] != criteria["eval_letter"]:
            passing_passes.append(criteria["pass_string"])
        elif criteria["pass_string"][int(criteria["num_range"][1])-1] == criteria["eval_letter"] and criteria["pass_string"][int(criteria["num_range"][0])-1] != criteria["eval_letter"]:
            passing_passes.append(criteria["pass_string"])
        else:
            pass
    return passing_passes

def main():
    ## prints the number of passing passwords for the former policy
    print(len(evaluate_passwords_former()))

    ## prints the number of passing passwords for the current policy
    print(len(evaluate_passwords_current()))

if __name__ == "__main__":
    main()