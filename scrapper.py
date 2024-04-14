
import csv
import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup


def get_user_input(message):

  while True:
    value = input(message)
    if value.strip():
      return value.strip()
    else:
      print("Please enter a tag/category.")




# Function to scrape data from the webpage
def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')


 

        specific_question_header_div = soup.find('div', id='question-header')

        header_tags = specific_question_header_div.find('a')

        scraped_question_header_data = header_tags.text.strip()

        # print(scraped_question_header_data)




        scraped_question = []


        # Fscrape question
        specific_div = soup.find('div', class_='question js-question', id='question')

        if specific_div:
            # Find all <p> tags under the specific <div>
            paragraph_tags = specific_div.find_all('p')

            if paragraph_tags:
                # Extract the text from the paragraph tags
                scraped_question_data = [tag.text.strip() for tag in paragraph_tags]
                # print(len(scraped_question_data))
                scraped_question.extend(scraped_question_data)
            else:
                print("No <p> tags found under the specified <div>.")
        else:
            print("No <div> found with the specified class and id.")


        # temporary comment end



        specific_div_answer = soup.find('div', class_='answer js-answer accepted-answer js-accepted-answer')

        # specific_div_answer = soup.find('div', class_="answer js-answer")


        scraped_answer = []

        if specific_div_answer:
            # Find all <p> tags under the specific <div>
            paragraph_tags = specific_div_answer.find_all('p')

            if paragraph_tags:
                # Extract the text from the paragraph tags
                scraped_answer_data = [tag.text.strip() for tag in paragraph_tags]
                # print(len(scraped_answer_data))
                scraped_answer.extend(scraped_answer_data)
            else:
                print("No <p> tags found under the specified <div>.")
        else:
            print("No <div> found with the specified class and id.")




        specific_div_answer = soup.find('div', class_="answer js-answer")


        scraped_answer2 = []

        if specific_div_answer:
            # Find all <p> tags under the specific <div>
            paragraph_tags = specific_div_answer.find_all('p')

            if paragraph_tags:
                # Extract the text from the paragraph tags
                scraped_answer_data2 = [tag.text.strip() for tag in paragraph_tags]
                # print(len(scraped_answer_data2))
                scraped_answer2.extend(scraped_answer_data2)
            else:
                print("No <p> tags found under the specified <div>.")
        else:
            print("No <div> found with the specified class and id.")


   

        final_data = {
           "title": scraped_question_header_data,
           "question": scraped_question,
           "answer": scraped_answer,
           "answer2": scraped_answer2

        }


        return final_data
    else:
        print("Failed to retrieve webpage.")
        return None


def create_csv(folder_path, data, data2):
    # Check if the specified folder exists, if not, create it
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Specify the CSV file path with timestamp
    file_name = f"data_{timestamp}.csv"
    file_path = os.path.join(folder_path, file_name)

    # Write the data to the CSV file
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        # Create a CSV writer object
        writer = csv.writer(file)

        # Write the data to the CSV file
        writer.writerow(data)
        writer.writerow(data2)

    print("CSV file created and saved successfully:", file_path)



# Main function
def main():
    # URL of the webpage to scrape
 
    # Prompt for custom user input
    custom_value = get_user_input("Enter your tag or category: ")



    url = "https://worldbuilding.stackexchange.com/questions/112945/creating-a-portable-nuclear-bomb-launcher"


    # Scrape data from the webpage
    scraped_data = scrape_website(url)


    # Check if data was scraped successfully
    if scraped_data:
        # # Specify the filename for the CSV file
    
        # Example usage:
        folder_path = './scraped'
        # data = ['Column 1', 'Column 2', 'Column 3'] 

        data1 = [custom_value, scraped_data["title"], scraped_data["answer"]]  

        data2 = [custom_value, scraped_data["question"], scraped_data["answer2"]] 

        create_csv(folder_path, data1, data2)


        print("Scraped data exported to", folder_path)
    else:
        print("No data scraped.")

if __name__ == "__main__":
    main()
