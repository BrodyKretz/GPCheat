import openai
import time

# Setup OpenAI API Key
openai.api_key = "your_openai_api_key"

# Function to query GPT and get the answer using the latest OpenAI API
def get_answer_from_gpt(question_text):
    prompt = f"Here is a multiple choice question: {question_text}. What is the correct answer? (A, B, C, or D)"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers multiple choice questions."},
            {"role": "user", "content": prompt}
        ]
    )
    
    answer = response['choices'][0]['message']['content'].strip().upper()
    
    return answer

# Function to simulate buzzing based on answer (A = 1 buzz, B = 2 buzzes, etc.)
def buzz_based_on_answer(answer):
    buzz_count = {"A": 1, "B": 2, "C": 3, "D": 4}.get(answer, 0)
    
    if buzz_count > 0:
        print(f"Detected Answer: {answer}")
        for _ in range(buzz_count):
            print("buzz", end=" ")
            time.sleep(0.5)  # Simulate the buzzing sound
        print("\n")
    else:
        print("No valid answer detected.")

# Main function
def main():
    try:
        print("Ask me a multiple choice question, and I'll determine the answer (A, B, C, or D).")
        
        while True:
            question_text = input("Enter your multiple choice question (or type 'exit' to quit): ")
            
            if question_text.lower() == "exit":
                break
            
            print("Processing the question...")
            
            answer = get_answer_from_gpt(question_text)
            buzz_based_on_answer(answer)
            
    except KeyboardInterrupt:
        print("Program interrupted.")
    finally:
        print("Goodbye!")

if __name__ == "__main__":
    main()
