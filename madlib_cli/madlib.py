import re

"""

X Print out a Welcome Message to the user that explains the game

X Grab a template from our filesysystem  >> readTemplate function
      - RAWSTRING this turns it into a string

X We need to break it down into two Parts >> parseTemplate function
      -this will return two things
          - STRIPPEDSTRING
          - KEYWORDS TUPLE

X Maybe create a function to ask the user Questions
    - def ASKUSERQUESTIONS
        - declare USERRESPONSE list to keep track of the user answers
        - will need to use KEYWORDS TUPLE
        - for loop through KEYWORDS TUPLE
            print "Give me a KEYWORD"
            store it into an input
            response = input( userAnswer)
            add the response to USERRESPONSE LIST
    - return a list USERRESPONSE

X Once we get the user response. Just combine the userResponse with the stripped string
    - use the MERGE function


- Once we get that mergedString
      - print it back to the user
      - save it to a file



"""

def print_welcome_message():
  print("""
  **   Welcome User!   **
  
  A number of questions will be asked. 
  Please answer all questions. 
  """)


def read_template(string):
  with open(string, 'r') as reader:
    return(reader.read())

def parse_template(string):
  pattern = r"\{([\w\s\d\'\-]+)\}"
  words_list = re.findall(pattern, string)
  words_tuple = tuple(words_list)
  replace = r"\{([\w\s\d\'\-]+)\}"
  new_string = re.sub(replace, "{}", string)
  return (new_string, words_tuple)

def merge(string: str, user_input: tuple) -> str:
  """
  Input >> string, tuple
  Output >> string

  Goal of this function. is to merge into a string

  string = "It was a {} and {} {}."
  user_input = ("dark", "stormy", "night")

  """
  merged_string = string.format(*user_input)
  return merged_string


def ask_user_questions(words_tuple):
  user_response = []
  for word in words_tuple:
    answer = input(f"Please enter a(n) {word}  >>  ")
    user_response.append(answer)
  return tuple(user_response)


def initialize(path):
  # this is going to start our script
  print_welcome_message()
  raw_template = read_template(path)
  parsed = parse_template(raw_template)
  stripped_string = parsed[0]
  keywords_tuple = parsed[1]
  user_answer = ask_user_questions(keywords_tuple)
  response_merge = merge(stripped_string, user_answer)
  print(response_merge)
  with open("assets/newfile.txt", "w") as new_file:
    new_file.write(response_merge)
  




if __name__ == "__main__":
  initialize("assets/madlib_template.txt")
  

















  """
  test1 = read_template("assets/dark_and_stormy_night_template.txt")
  parsed_item = parse_template(test1)
  # print(parsed_item)
  print(parsed_item[0])
  print('-----------------')
  print(parsed_item[1])
  """