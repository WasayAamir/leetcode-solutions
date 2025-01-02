import os
import subprocess

# Define the base directory for your solutions
BASE_DIR = os.getcwd()

def create_problem_folder(problem_number, problem_title, difficulty, description, examples, constraints, solution_file="solution.py"):
    # Generate folder name and path
    folder_name = f"{problem_number}-{problem_title.replace(' ', '-').lower()}"
    folder_path = os.path.join(BASE_DIR, folder_name)

    # Create the folder
    os.makedirs(folder_path, exist_ok=True)

    # Create README.md
    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, "w") as readme_file:
        readme_file.write(f"# {problem_title}\n\n")
        readme_file.write(f"![Difficulty: {difficulty}](https://img.shields.io/badge/Difficulty-{difficulty.replace(' ', '-')}-{'brightgreen' if difficulty == 'Easy' else 'orange' if difficulty == 'Medium' else 'red'})\n\n")
        readme_file.write("---\n\n")
        readme_file.write(f"{description}\n\n")
        readme_file.write("---\n\n### Examples:\n")
        for example in examples:
            readme_file.write(f"**Input**: {example['input']}\n")
            readme_file.write(f"**Output**: {example['output']}\n")
            if 'explanation' in example:
                readme_file.write(f"**Explanation**: {example['explanation']}\n")
            readme_file.write("\n---\n\n")
        readme_file.write(f"### Constraints:\n")
        for constraint in constraints:
            readme_file.write(f"- {constraint}\n")
        readme_file.write("\n")

    # Create a placeholder for the solution file
    solution_path = os.path.join(folder_path, solution_file)
    with open(solution_path, "w") as solution_file:
        solution_file.write(f"# Solution for {problem_title}\n\n")

    print(f"Created folder: {folder_name}")
    return folder_path

def git_commit_and_push(folder_path, commit_message):
    # Stage the changes
    subprocess.run(["git", "add", folder_path])

    # Commit the changes
    subprocess.run(["git", "commit", "-m", commit_message])

    # Push the changes
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    # Inputs
    problem_number = input("Enter problem number: ").strip()
    problem_title = input("Enter problem title: ").strip()
    difficulty = input("Enter difficulty (Easy, Medium, Hard): ").strip()
    description = input("Enter problem description: ").strip()
    num_examples = int(input("Enter number of examples: ").strip())

    examples = []
    for _ in range(num_examples):
        example_input = input("Enter example input: ").strip()
        example_output = input("Enter example output: ").strip()
        example_explanation = input("Enter explanation (optional, press Enter to skip): ").strip()
        example = {"input": example_input, "output": example_output}
        if example_explanation:
            example["explanation"] = example_explanation
        examples.append(example)

    constraints = input("Enter constraints (comma-separated): ").strip().split(", ")

    # Create folder and files
    folder_path = create_problem_folder(problem_number, problem_title, difficulty, description, examples, constraints)

    # Commit and push changes
    commit_message = f"Add solution for {problem_number}. {problem_title}"
    git_commit_and_push(folder_path, commit_message)
