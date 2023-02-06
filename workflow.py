import gpt, speak, listen
import sys
from test_constants import TEST_RESPONSE

TEST_FLAG = False

def record_voice_input():
    print("Recording speech for 5 seconds...")
    try:
        speech = listen.record_input()
    except:
        print("Error: Unable to resolve speech.")
        exit()
    return speech


if __name__ == "__main__":
    # Check test flag
    if len(sys.argv) == 2:
        if sys.argv[1] == "-t":
            TEST_FLAG = True

    print("Starting workflow.")

    # Record user voice input
    speech = record_voice_input()

    # Confirm user voice input
    sys.stdout.write(f"Send to GPT: {speech} \nIs this okay? [y/N]")
    approve = input()
    while approve != "y" and approve != "N":
        sys.stdout.write("Please enter [y] or [N]")
        approve = input()

    if approve == "N":
        print("Exiting.")
        exit()

    # Call ChatGPT
    print("Calling GPT api with prompt: ", speech)
    if TEST_FLAG:
        response = TEST_RESPONSE
    else:
        response = gpt.completion(speech)

    print("Received response.")
    print(response)

    # Convert text to speech
    text = response.get("choices")[0].get("text")
    if text:
        speak.speak(text)

        

    
    

    
