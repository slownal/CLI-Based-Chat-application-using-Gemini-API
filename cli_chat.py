#!/usr/bin/env python3
import os
import json
import google.generativeai as genai
from datetime import datetime
from rich.console import Console
from rich.markdown import Markdown

# Initialize Rich console for better formatting
console = Console()

# Setup Google Gemini API
def setup_genai():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        console.print("[bold red]ERROR: GEMINI_API_KEY environment variable not set.[/bold red]")
        console.print("[yellow]Please set your API key with: $env:GEMINI_API_KEY='your_api_key' (PowerShell)[/yellow]")
        exit(1)
    
    genai.configure(api_key=api_key)
    
    # Try using different model names - updated to latest format
    model_options = [
        "gemini-pro",  # Original format
        "gemini-1.0-pro",  # Possible version format
        "gemini-1.5-pro",  # Latest version
        "models/gemini-pro",  # With models/ prefix
        "models/gemini-1.0-pro",
        "models/gemini-1.5-pro"
    ]
    
    # Try each model until one works
    for model_name in model_options:
        try:
            console.print(f"[yellow]Trying model: {model_name}...[/yellow]")
            model = genai.GenerativeModel(model_name)
            # Test the model with a simple prompt
            response = model.generate_content("Hello")
            console.print(f"[bold green]Successfully connected using model: {model_name}[/bold green]")
            return model
        except Exception as e:
            console.print(f"[yellow]Model {model_name} failed: {str(e)}[/yellow]")
    
    # If all models fail, show error and exit
    console.print("[bold red]ERROR: Could not connect to any Gemini model.[/bold red]")
    console.print("[yellow]Please check your API key and internet connection.[/yellow]")
    console.print("[yellow]You may also need to update the google-generativeai package:[/yellow]")
    console.print("[yellow]pip install --upgrade google-generativeai[/yellow]")
    exit(1)

# Function for saving feedback to file
def save_feedback(feedback_data, filename="feedback.txt"):
    with open(filename, "a") as f:
        f.write(f"\n--- Feedback from {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
        f.write(f"Rating: {feedback_data['rating']}/5\n")
        f.write(f"Review: {feedback_data['review']}\n")
        f.write("-" * 50 + "\n")

# Optional: Function to save chat history
def save_chat_history(user_message, ai_response, filename="chat_history.txt"):
    with open(filename, "a") as f:
        f.write(f"\nUser ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}): {user_message}\n")
        f.write(f"AI: {ai_response}\n")
        f.write("-" * 50 + "\n")

def main():
    # Setup the Gemini model
    model = setup_genai()
    
    # Initial greeting
    console.print("[bold green]Welcome to Gemini Chat CLI![/bold green]")
    console.print("Type your messages and press Enter. Type 'exit', 'bye', or similar to end the chat.")
    console.print("-" * 50)
    
    # Start chat session
    chat = model.start_chat(history=[])
    in_exit_flow = False
    
    while True:
        # Get user input
        user_message = input("\n[You]: ")
        
        try:
            # Basic exit detection without function calling
            if not in_exit_flow and any(exit_word in user_message.lower() for exit_word in ['bye', 'exit', 'quit', 'end', 'goodbye']):
                console.print("\n[bold yellow]I see you want to end our conversation.[/bold yellow]")
                console.print("[bold yellow]Before you go, could you please provide a brief review and rating (1-5) of your experience?[/bold yellow]")
                in_exit_flow = True
                continue
                
            # Handle feedback and exit
            if in_exit_flow:
                # Simple parsing of rating
                rating = None
                for word in user_message.split():
                    if word.isdigit() and 1 <= int(word) <= 5:
                        rating = int(word)
                        break
                
                if rating is None:
                    console.print("[bold yellow]I couldn't find a rating between 1-5 in your response.[/bold yellow]")
                    console.print("[bold yellow]Please include a number from 1 to 5 in your feedback.[/bold yellow]")
                    continue
                
                # Save feedback
                feedback = {
                    "review": user_message,
                    "rating": rating
                }
                save_feedback(feedback)
                console.print(f"\n[bold green]Thank you for your feedback! Your rating of {rating}/5 and review have been saved.[/bold green]")
                console.print("[bold green]Thank you for chatting! Goodbye![/bold green]")
                break
            
            # Normal chat flow
            response = chat.send_message(user_message)
            
            # Display the text response
            ai_message = response.text
            console.print("\n[AI]:", style="bold blue")
            console.print(Markdown(ai_message))
            
            # Save to chat history (optional feature)
            save_chat_history(user_message, ai_message)
            
        except Exception as e:
            console.print(f"[bold red]Error: {str(e)}[/bold red]")
            console.print("[yellow]Let's continue our conversation...[/yellow]")

if __name__ == "__main__":
    main() 